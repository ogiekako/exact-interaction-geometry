from pathlib import Path
import re

p = Path('EIG_CORE.md')
text = p.read_text()


def strip_sep(s: str) -> str:
    s = s.strip()
    s = re.sub(r'\n---\s*$', '', s).rstrip()
    return s


def parse_numbered_sections(s: str):
    matches = list(re.finditer(r'(?m)^# (\d+)\. ([^\n]+)\n', s))
    if not matches:
        raise RuntimeError('no numbered sections found')
    prefix = s[:matches[0].start()].rstrip()
    out = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(s)
        out[int(m.group(1))] = strip_sep(s[m.start():end])
    return prefix, out


def parse_subsections(section: str, n: int):
    first_nl = section.find('\n')
    header = section[:first_nl]
    body = section[first_nl + 1:]
    pat = re.compile(rf'(?m)^## {n}\.(\d+) ([^\n]+)\n')
    ms = list(pat.finditer(body))
    intro = body[:ms[0].start()].strip() if ms else body.strip()
    subs = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(body)
        subs[int(m.group(1))] = strip_sep(body[m.start():end])
    return header, intro, subs


def build_selected(section: str, old_n: int, new_n: int, title: str, selected, submap=None):
    _, intro, subs = parse_subsections(section, old_n)
    parts = [f'# {new_n}. {title}']
    if intro:
        parts.append(intro)
    for old_sub in selected:
        chunk = subs[old_sub]
        new_sub = submap.get(old_sub, old_sub) if submap else old_sub
        chunk = re.sub(rf'^## {old_n}\.{old_sub} ', f'## {new_n}.{new_sub} ', chunk, count=1)
        parts.append(chunk)
    return '\n\n'.join(parts)


def renumber_whole(section: str, old_n: int, new_n: int, title=None):
    lines = section.splitlines()
    old_title = re.match(rf'^# {old_n}\. (.*)$', lines[0]).group(1)
    lines[0] = f'# {new_n}. {title or old_title}'
    s = '\n'.join(lines)
    s = re.sub(rf'(?m)^## {old_n}\.(\d+) ', rf'## {new_n}.\1 ', s)
    s = re.sub(rf'(?m)^### {old_n}\.(\d+)\.(\d+) ', rf'### {new_n}.\1.\2 ', s)
    return s


def appendix_from_subsections(section: str, old_n: int, appendix: str, title: str, selected, labels=None):
    _, intro, subs = parse_subsections(section, old_n)
    parts = [f'# Appendix {appendix}. {title}']
    if intro:
        parts.append(intro)
    for idx, old_sub in enumerate(selected, 1):
        chunk = subs[old_sub]
        label = labels.get(old_sub, idx) if labels else idx
        chunk = re.sub(rf'^## {old_n}\.{old_sub} ', f'## {appendix}.{label} ', chunk, count=1)
        parts.append(chunk)
    return '\n\n'.join(parts)


app_a_pos = text.index('# Appendix A.')
main_old = text[:app_a_pos]
old_apps = text[app_a_pos:]
app_b_pos_rel = old_apps.index('# Appendix B.')
old_app_a = strip_sep(old_apps[:app_b_pos_rel])
old_app_b = strip_sep(old_apps[app_b_pos_rel:])

prefix, sec = parse_numbered_sections(main_old)
required = set(range(0, 29))
missing = sorted(required - set(sec))
if missing:
    raise RuntimeError(f'missing numbered sections: {missing}')

# Main spine: only material needed to reach the generic EIG/EIG-Core theorems.
main = []
main.append(sec[0])
main.append(sec[1])
main.append(sec[2])
main.append(build_selected(sec[3], 3, 3, 'Contextual reduction', [1, 2, 3]))
main.append(build_selected(sec[4], 4, 4, 'Intrinsic reduced root and root-exactness', [4, 6], {4: 1, 6: 2}))
main.append(build_selected(sec[5], 5, 5, 'The fixed-doctrine invariant: the semantic closure modality', [1, 2, 3, 4, 5]))
main.append(renumber_whole(sec[6], 6, 6))
main.append(build_selected(sec[7], 7, 7, 'Internal free/least universal property', [1, 2, 3]))
main.append(renumber_whole(sec[22], 22, 8, 'Main theorem for EIG Core'))
main.append(renumber_whole(sec[12], 12, 9, 'Universal canonicality principle'))
main.append(renumber_whole(sec[13], 13, 10, 'Doctrine fibres: exact selection theorem'))
main.append(renumber_whole(sec[14], 14, 11, 'Core descent: exact doctrine-free EIG Core theorem'))
main.append(renumber_whole(sec[15], 15, 12, 'Doctrine-free EIG object: the full labelled fibration'))
main.append(renumber_whole(sec[23], 23, 13, 'Main theorem for EIG as a whole'))
main.append(renumber_whole(sec[16], 16, 14, 'Canonicality/no-go structure'))
main.append(renumber_whole(sec[24], 24, 15, 'Canonicality/no-go theorem'))
main.append(renumber_whole(sec[25], 25, 16, 'Why the positive and negative boundaries coincide exactly'))
main.append(renumber_whole(sec[28], 28, 17, 'Summary'))

# Appendix A: contextual-reduction variants not needed for the main quotient theorem.
appA = appendix_from_subsections(sec[3], 3, 'A', 'Contextual-reduction variants and higher boundaries', [4, 5, 6, 7])

# Appendix B: examples/calibrations for roots and the concrete REDUCE counterexample.
appB = appendix_from_subsections(sec[4], 4, 'B', 'Root calibrations and reduction counterexamples', [1, 2, 3, 5])

# Appendix C: closure computation rather than closure existence/canonicality.
appC = appendix_from_subsections(sec[5], 5, 'C', 'Closure computation and iteration', [6, 7])

# Appendix D: stronger external packaging, ordered modalities, and coherence.
_, _, s7 = parse_subsections(sec[7], 7)
d1 = re.sub(r'^## 7\.4 ', '## D.1 ', s7[4], count=1)

def demote_whole(section, old_n, label, title):
    lines = section.splitlines()
    lines[0] = f'## {label} {title}'
    s = '\n'.join(lines)
    s = re.sub(rf'(?m)^## {old_n}\.(\d+) ', rf'### {label}.\1 ', s)
    return s

appD = '\n\n'.join([
    '# Appendix D. External completion, modality factorization, and coherence',
    'These constructions refine or present the already-defined simultaneous semantic closure; they are not part of its existence or canonicality proof.',
    d1,
    demote_whole(sec[8], 8, 'D.2', 'Modality stratification as a factorization/computation theorem'),
    demote_whole(sec[9], 9, 'D.3', 'Coherence and the single-monad boundary'),
])

# Appendix E: all downstream recognition/law/operation layers.
appE = '\n\n'.join([
    '# Appendix E. Associated theory, recognition, and external operations',
    'These layers become relevant only after the Core has been constructed. None is used to define the reduced root or the least semantic closure.',
    demote_whole(sec[10], 10, 'E.1', 'Associated EIG theory and the maximal law envelope'),
    demote_whole(sec[11], 11, 'E.2', 'Recognition, density, and external operations'),
])

# Appendix F: recurrent specialization.
_, intro17, s17 = parse_subsections(sec[17], 17)
partsF = ['# Appendix F. Protected recurrent EIG specialization']
if intro17:
    partsF.append(intro17)
for k in sorted(s17):
    chunk = re.sub(rf'^## 17\.{k} ', f'## F.{k} ', s17[k], count=1)
    partsF.append(chunk)
appF = '\n\n'.join(partsF)

# Appendix G: counterexamples plus the compact scope-limit list.
_, intro18, s18 = parse_subsections(sec[18], 18)
partsG = ['# Appendix G. Counterexamples and scope limits']
if intro18:
    partsG.append(intro18)
for i, k in enumerate(sorted(s18), 1):
    chunk = re.sub(r'^## CE(\d+)\. ', rf'## G.\1 ', s18[k], count=1)
    partsG.append(chunk)
scope26 = sec[26]
scope26 = re.sub(r'^# 26\. ', '## G.15 ', scope26, count=1)
partsG.append(scope26)
appG = '\n\n'.join(partsG)

# Appendix H: prior-art boundary.
appH = demote_whole(sec[19], 19, 'H', 'Prior-art boundary and what is project-specific')
appH = re.sub(r'^## H ', '# Appendix H. ', appH, count=1)
appH = re.sub(r'(?m)^### H\.(\d+) ', r'## H.\1 ', appH)

# Appendix I: proof map and editorial reading/publication order.
appI = '\n\n'.join([
    '# Appendix I. Dependency map and repository organization',
    demote_whole(sec[20], 20, 'I.1', 'Proof dependency DAG'),
    demote_whole(sec[21], 21, 'I.2', 'Scope summary'),
    demote_whole(sec[27], 27, 'I.3', 'Canonical repository formulation'),
])

# Existing appendices become J/K.
appJ = old_app_a
appJ = re.sub(r'^# Appendix A\. ', '# Appendix J. ', appJ, count=1)
appJ = re.sub(r'(?m)^## A\.(\d+) ', r'## J.\1 ', appJ)
appK = old_app_b
appK = re.sub(r'^# Appendix B\. ', '# Appendix K. ', appK, count=1)
appK = re.sub(r'(?m)^## B\.(\d+) ', r'## K.\1 ', appK)

out = prefix + '\n\n---\n\n' + '\n\n---\n\n'.join(main)

reading_note = '''### Reading path\n\nSections 2–17 form the linear theoretical spine. They introduce the doctrine, contextual reduction, intrinsic reduced root, least simultaneous semantic closure, its functorial and universal properties, doctrine selection/descent, the doctrine-free EIG package, and the matching canonicality/no-go theorem. The appendices contain alternative computations, calibration examples, recognition machinery, the recurrent specialization, counterexamples, prior-art boundaries, and repository/proof metadata. None of those appendices is needed to follow the generic theorem from assumptions to conclusion.'''
needle = '> **Use reduced-world root extraction and simultaneous semantic closure as the logical spine. Retain every compatible orthogonal theorem only in a form that preserves that spine, the reduced-root ordering, and the specified-solution/invariant no-go boundary.**'
if needle not in out:
    raise RuntimeError('integration-rule needle missing')
out = out.replace(needle, needle + '\n\n' + reading_note, 1)

out += '\n\n---\n\n' + '\n\n---\n\n'.join([appA, appB, appC, appD, appE, appF, appG, appH, appI, appJ, appK]) + '\n'

# Cross-reference repair. Specific subsection moves first, then whole-section renumbering.
ref_map = [
    ('Section 3.4', 'Appendix A.1'), ('Section 3.5', 'Appendix A.2'), ('Section 3.6', 'Appendix A.3'), ('Section 3.7', 'Appendix A.4'),
    ('Section 4.1', 'Appendix B.1'), ('Section 4.2', 'Appendix B.2'), ('Section 4.3', 'Appendix B.3'), ('Section 4.5', 'Appendix B.4'),
    ('Section 4.4', 'Section 4.1'), ('Section 4.6', 'Section 4.2'),
    ('Section 5.6', 'Appendix C.1'), ('Section 5.7', 'Appendix C.2'),
    ('Section 7.4', 'Appendix D.1'),
    ('Section 8.1', 'Appendix D.2.1'), ('Section 8.2', 'Appendix D.2.2'), ('Section 8.3', 'Appendix D.2.3'), ('Section 8.4', 'Appendix D.2.4'), ('Section 8.5', 'Appendix D.2.5'),
    ('Section 9.1', 'Appendix D.3.1'), ('Section 9.2', 'Appendix D.3.2'), ('Section 9.3', 'Appendix D.3.3'), ('Section 9.4', 'Appendix D.3.4'), ('Section 9.5', 'Appendix D.3.5'),
    ('Section 10', 'Appendix E.1'), ('Section 11', 'Appendix E.2'),
    ('Section 12', 'Section 9'), ('Section 13', 'Section 10'),
    ('Section 14.5', 'Section 11.5'), ('Section 14', 'Section 11'),
    ('Section 15', 'Section 12'), ('Section 16', 'Section 14'),
    ('Section 17.10', 'Appendix F.10'), ('Section 17', 'Appendix F'),
    ('Section 19.4', 'Appendix H.4'), ('Section 19', 'Appendix H'),
    ('Section 20', 'Appendix I.1'), ('Section 21', 'Appendix I.2'),
    ('Section 22', 'Section 8'), ('Section 23', 'Section 13'), ('Section 24', 'Section 15'), ('Section 25', 'Section 16'),
    ('Section 26', 'Appendix G.15'), ('Section 27', 'Appendix I.3'), ('Section 28', 'Section 17'),
]
for a, b in ref_map:
    out = out.replace(a, b)

# Repair references to old appendix labels.
out = out.replace('Appendix A.', 'Appendix J.') if False else out

# Remove stale research-log wording that became especially distracting after reordering.
out = out.replace('# 17. Protected recurrent EIG: currently justified specialization', '# 17. Protected recurrent EIG specialization')
out = out.replace('The strongest fixed-doctrine object is not only one root-generated class.', 'The fixed-doctrine invariant is not only one root-generated class.')
out = out.replace('The strongest unconditional statement:', 'The unconditional statement:')
out = out.replace('Strongest conclusion', 'Conclusion')

# Main-text linearity gates.
for forbidden in ['# 8. Modality stratification', '# 10. Associated EIG theory', '# 11. Recognition, density', '# 17. Protected recurrent EIG', '# 18. Sharp counterexample', '# 19. Prior-art', '# 20. Proof dependency', '# 21. Scope summary', '# 26. Scope limits', '# 27. Canonical repository formulation']:
    if forbidden in out:
        raise RuntimeError(f'stale old top-level section remains: {forbidden}')

# Ensure appendices and main theorem spine exist exactly once.
for required_text in [
    '# 8. Main theorem for EIG Core',
    '# 13. Main theorem for EIG as a whole',
    '# 15. Canonicality/no-go theorem',
    '# 17. Summary',
    '# Appendix E. Associated theory, recognition, and external operations',
    '# Appendix F. Protected recurrent EIG specialization',
    '# Appendix G. Counterexamples and scope limits',
]:
    if out.count(required_text) != 1:
        raise RuntimeError(f'expected exactly one {required_text!r}, got {out.count(required_text)}')

# No progress markers or unsupported GitHub math syntax should return.
if re.search(r'\[(?:PROVED|CONDITIONAL|DEPENDENT|OPEN|FALSE|STANDARD|DIRECT)[^\]]*\]', out):
    raise RuntimeError('research-progress marker reintroduced')
if '\\operatorname' in out:
    raise RuntimeError('operatorname reintroduced')

p.write_text(out)
