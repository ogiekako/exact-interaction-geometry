# Historical Boolean-only draft — superseded

This directory records the **first** standalone draft obtained from the four-row Boolean-rank counterexample.

It has been superseded by the stronger canonical note:

[`../source-pair-augmentation/`](../source-pair-augmentation/)

which gives explicit counterexamples to the Parnas--Shraibman Section-6 source-pair question for **both Boolean rank and binary rank**, together with an exact verifier and binary row-minimality on at most four rows.

The Boolean construction remains unchanged:

```text
A = {3,7,15}
U = {3,5,8}
V = {3,5,12}
```

with

```text
rank_bool(A)=3,
rank_bool(A|U|V)=4,
rank_bool(A|u|v)=3 for every u in U, v in V.
```

`paper.tex` in this directory is retained only for discovery/publication provenance. **Do not use it as the current submission draft.**
