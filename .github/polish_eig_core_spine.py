from pathlib import Path
import re

p = Path('EIG_CORE.md')
s = p.read_text()

# Remove accidental duplicate separator after the preamble.
s = s.replace('\n---\n\n---\n\n# 0.', '\n---\n\n# 0.', 1)

# Replace the old research-synthesis-heavy opening with a direct reading map.
new0 = '''# 0. Scope and reading path

This note gives the generic canonicality architecture of Exact Interaction Geometry (EIG). Its fixed-doctrine spine is

```text
admitted contexts / observations
        -> contextual reduction
        -> intrinsic root in the reduced semantic world
        -> least simultaneous semantic closure
        -> EIGCore(D).
```

Three distinctions organize everything that follows:

1. **fixed-doctrine Core:** for a declared doctrine `D`, the Core is the least admissible `D`-closed semantic structured subtheory containing the reduced root;
2. **reconstruction:** density, nerve recognition, operation reconstruction, process realization, and ordered normal forms are additional theorems, not ingredients of Core canonicality;
3. **doctrine-free canonicality:** selecting a doctrine and descending all doctrine-relative Cores to one semantics-only Core are different universal problems.

Sections 2–17 form the linear theoretical spine from primitive doctrine data to the final EIG/EIG-Core and no-go theorems. The appendices contain alternative computations, calibrations, reconstruction machinery, the recurrent specialization, counterexamples, prior-art boundaries, and proof/repository metadata. None of those appendices is needed to follow the generic theorem from assumptions to conclusion.

---

# 1.'''
s, n = re.subn(r'# 0\. Scope and structural synthesis\n.*?\n---\n\n# 1\.', new0, s, count=1, flags=re.S)
if n != 1:
    raise RuntimeError('failed to rewrite Section 0')

# Fix theorem numbers left behind by section renumbering.
s = s.replace('### Theorem 12.1 — exact specified-solution trichotomy', '### Theorem 9.1 — exact specified-solution trichotomy')
s = s.replace('## Theorem 16.1 — canonicality boundary', '## Theorem 14.1 — canonicality boundary')
s = s.replace('> **Strongest unconditional statement:** internal least semantic closure/reflection.  ', '> **Unconditional statement:** internal least semantic closure/reflection.  ')
s = s.replace('> **Stronger external free-algebra/2-categorical completion:** conditional on a separately proved algebraic presentation, existence theorem, and appropriate faithfulness.', '> **External free-algebra/2-categorical completion:** requires a separately proved algebraic presentation, existence theorem, and appropriate faithfulness.')

# Helpers for current numbered sections.
def top_section(text, n, next_n):
    a = text.index(f'# {n}.')
    b = text.index(f'# {next_n}.', a) if next_n is not None else len(text)
    return a, b, text[a:b].rstrip()

def split_subs(section, n):
    first = section.find('\n')
    header = section[:first]
    body = section[first+1:]
    pat = re.compile(rf'(?m)^## {n}\.(\d+) ([^\n]+)\n')
    ms = list(pat.finditer(body))
    intro = body[:ms[0].start()].strip() if ms else body.strip()
    subs = {}
    for i,m in enumerate(ms):
        end = ms[i+1].start() if i+1 < len(ms) else len(body)
        subs[int(m.group(1))] = body[m.start():end].strip()
    return header, intro, subs

# Section 9: move the walking-arrow calibration out of the conceptual spine.
a9, b9, sec9 = top_section(s, 9, 10)
_, intro9, sub9 = split_subs(sec9, 9)
walk = sub9[2]
prob = re.sub(r'^## 9\.3 ', '## 9.2 ', sub9[3], count=1)
new9 = '# 9. Universal canonicality principle\n\n' + intro9 + '\n\n' + sub9[1] + '\n\n' + prob + '\n\n---\n\n'
s = s[:a9] + new9 + s[b9:]
walk = re.sub(r'^## 9\.2 ', '## G.15 ', walk, count=1)

# Section 11: keep the factorization theorem and abstract independence statement;
# move examples and Kan shadows to appendices.
a11, b11, sec11 = top_section(s, 11, 12)
_, intro11, sub11 = split_subs(sec11, 11)
sel_descent = sub11[4]
isotropy = sub11[5]
kan = sub11[6]
main_independence = '''## 11.4 Selection and descent are independent

A doctrine section `s` yields a selected core `Ks`, but does not imply a factorization

$$
\bar K U\simeq K.
$$

Conversely, a common-Core factorization can exist even when no invariant doctrine selector exists. Thus doctrine selection and Core descent are logically independent universal problems. Appendix G.16 and Appendix G.7 give explicit witnesses in the two directions.'''
new11 = '# 11. Core descent: exact doctrine-free EIG Core theorem\n\n' + intro11 + '\n\n' + '\n\n'.join(sub11[i] for i in [1,2,3]) + '\n\n' + main_independence + '\n\n---\n\n'
s = s[:a11] + new11 + s[b11:]
sel_descent = re.sub(r'^## 11\.4 ', '## G.16 ', sel_descent, count=1)
isotropy = re.sub(r'^## 11\.5 ', '## G.17 ', isotropy, count=1)
kan = re.sub(r'^## 11\.6 ', '## E.3 ', kan, count=1)

# Add Kan-extension shadows at the end of Appendix E, before Appendix F.
appF = s.index('# Appendix F.')
sep = s.rfind('\n---\n\n', 0, appF)
if sep < 0:
    raise RuntimeError('separator before Appendix F not found')
s = s[:sep] + '\n\n' + kan + s[sep:]

# Normalize Appendix G headings, add the moved concrete examples, and shift Scope limits.
g_start = s.index('# Appendix G.')
h_start = s.index('# Appendix H.', g_start)
g = s[g_start:h_start]
for i in range(1, 15):
    g = g.replace(f'## CE{i}.', f'## G.{i}')
g = g.replace('## G.15 Scope limits', '## G.18 Scope limits')
insert = g.index('## G.18 Scope limits')
g = g[:insert].rstrip() + '\n\n' + walk + '\n\n' + sel_descent + '\n\n' + isotropy + '\n\n' + g[insert:]
s = s[:g_start] + g + s[h_start:]

# References to the moved concrete examples.
s = s.replace('Section 11.5', 'Appendix G.17')

# The original document also had a third appendix; move it after the new A-K range.
meta = '# Appendix C. Meta-EIG under the same canonicality discipline'
if meta in s:
    pos = s.index(meta)
    tail = s[pos:]
    tail = tail.replace(meta, '# Appendix L. Meta-EIG under the same canonicality discipline', 1)
    tail = re.sub(r'(?m)^## C\.(\d+) ', r'## L.\1 ', tail)
    s = s[:pos] + tail

# Publication/presentation gates.
for old in ['Theorem 12.1', 'Theorem 16.1', '# Appendix C. Meta-EIG']:
    if old in s:
        raise RuntimeError(f'stale label remains: {old}')
if s.count('# Appendix C.') != 1:
    raise RuntimeError('Appendix C should occur exactly once after relabeling Meta-EIG')
for req in ['# Appendix L. Meta-EIG under the same canonicality discipline', '## G.15 Why raw moduli noncontractibility is not an absolute no-go', '## G.16 Selection and descent are independent', '## G.17 Coherent isotropy can obstruct descent', '## E.3 Kan-extension shadows']:
    if req not in s:
        raise RuntimeError(f'missing moved material: {req}')
if '\\operatorname' in s:
    raise RuntimeError('operatorname reintroduced')
if re.search(r'\[(?:PROVED|CONDITIONAL|DEPENDENT|OPEN|FALSE|STANDARD|DIRECT)[^\]]*\]', s):
    raise RuntimeError('research-progress marker reintroduced')

p.write_text(s)
