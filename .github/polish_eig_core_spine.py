from pathlib import Path
import re

p = Path('EIG_CORE.md')
s = p.read_text()

# Collapse accidental duplicate horizontal rules introduced while moving sections.
s = re.sub(r'\n---\n(?:[ \t]*\n)*---\n', '\n---\n', s)

# Keep a single blank line between a top-level heading and its first paragraph/subheading.
s = re.sub(r'(?m)^(# (?:\d+|Appendix [A-L])\.[^\n]*)\n{3,}', r'\1\n\n', s)

# Remove trailing whitespace without changing mathematical content.
s = '\n'.join(line.rstrip() for line in s.splitlines()) + '\n'

# Presentation gates.
if re.search(r'\n---\n(?:[ \t]*\n)*---\n', s):
    raise RuntimeError('duplicate horizontal rule remains')
if '\\operatorname' in s:
    raise RuntimeError('operatorname reintroduced')
if re.search(r'\[(?:PROVED|CONDITIONAL|DEPENDENT|OPEN|FALSE|STANDARD|DIRECT)[^\]]*\]', s):
    raise RuntimeError('research-progress marker reintroduced')
for stale in ['Theorem 12.1', 'Theorem 16.1', '# Appendix C. Meta-EIG']:
    if stale in s:
        raise RuntimeError(f'stale label remains: {stale}')

p.write_text(s)
