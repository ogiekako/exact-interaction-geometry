from pathlib import Path
import re

p = Path('EIG_CORE.md')
s = p.read_text()

replacements = {
    'This note states the generic EIG Core / EIG canonicality architecture, its exact hypotheses, reconstruction gates, and no-go boundaries.':
        'This note states the generic EIG Core / EIG canonicality architecture, its exact hypotheses, reconstruction conditions, and no-go boundaries.',
    'The strongest safe classification is as follows.':
        'The recurrent specialization is organized as follows.',
    '## 17.9 Strongest historical equivalence endpoint':
        '## 17.9 Historical equivalence endpoint',
    'followed by the previously audited process-nerve equivalence on its stated essential image.':
        'followed by the process-nerve equivalence on its stated essential image used in the recurrent specialization.',
    'Effectivity and Beck-Chevalley/base-change preservation remain separate gates.':
        'Effectivity and Beck-Chevalley/base-change preservation are separate conditions.',
    '                       +--> B4 density gate\n                       +--> B5 maximal law envelope / definability gate\n                       +--> B6 operation restriction / exactness gate':
        '                       +--> B4 density condition\n                       +--> B5 maximal law envelope / definability condition\n                       +--> B6 operation restriction / exactness condition',
    'Density, nervousness, law definability, operation exactness, and process/model reconstruction are downstream gates and do not weaken the fixed-doctrine canonicality theorem.':
        'Density, nervousness, law definability, operation exactness, and process/model reconstruction are downstream conditions and do not weaken the fixed-doctrine canonicality theorem.',
    '> supplemented only by independently certified density, law-recognition, operation-exactness, descent, and realization data.':
        '> supplemented, where available, by separately stated density, law-recognition, operation-exactness, descent, and realization data.',
    'It is the full doctrine fibration labelled by the EIG outputs that have actually been proved, in particular the core-labelled fibre':
        'It is the full doctrine fibration labelled by the EIG outputs established under their stated hypotheses, in particular the core-labelled fibre',
    '> The full labelled doctrine fibration remains the uncollapsed canonical output when point selection/descent is not established. Empty invariant-solution spaces are genuine no-go theorems. Raw noncontractibility by itself is not.':
        '> The full labelled doctrine fibration remains the uncollapsed canonical output when point selection/descent is not determined by the declared problem. Empty invariant-solution spaces are genuine no-go theorems. Raw noncontractibility by itself is not.',
    '10. Separately audit density, law recognition, operation exactness, and process realization.':
        '10. State density, law recognition, operation exactness, and process realization separately, with their own hypotheses.',
    '15. Present the recurrent SYNC/STORE/SPACE/SEQ row as a specialization whose ordered factorization remains conditional until its exact lemma is proved.':
        '15. Present the recurrent SYNC/STORE/SPACE/SEQ row as a specialization, and assert its ordered factorization only under the Section 17.10 factorization hypotheses.',
}
for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new)

# GitHub block math: normalize legacy display delimiters even inside blockquotes.
out = []
legacy = 0
for line in s.splitlines(keepends=True):
    body = line[:-1] if line.endswith('\n') else line
    ending = '\n' if line.endswith('\n') else ''
    m = re.fullmatch(r'(\s*(?:>\s*)?)\\[\[\]]\s*', body)
    if m:
        out.append(m.group(1) + '$$' + ending)
        legacy += 1
    else:
        out.append(line)
s = ''.join(out)

# Presentation gates.
status_pat = re.compile(r'\[(?:STANDARD|DIRECT|PROVED|CONDITIONAL|DEPENDENT|OPEN|FALSE|NOT ESTABLISHED)[^\]]*\]')
if status_pat.search(s):
    raise SystemExit('research-progress marker remains in EIG_CORE.md')
if re.search(r'(?m)^\s*(?:>\s*)?\\[\[\]]\s*$', s):
    raise SystemExit('legacy GitHub display-math delimiter remains in EIG_CORE.md')
if '\\operatorname' in s:
    raise SystemExit('unsupported operatorname remains in EIG_CORE.md')
if 'remains conditional until its exact lemma is proved' in s:
    raise SystemExit('legacy open-program wording remains')

p.write_text(s)
print(f'normalized {legacy} legacy blockquoted display delimiters')
