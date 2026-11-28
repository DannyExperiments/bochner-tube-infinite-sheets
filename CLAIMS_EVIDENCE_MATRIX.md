# Claims and evidence

| Item | Evidence |
| --- | --- |
| Main theorem | [Complete analytic proof](paper/manuscript.tex) |
| Original statement | [Primary edition](https://diva-portal.org/smash/get/diva2:2043979/FULLTEXT01.pdf#page=2) |
| Selected independent calculations | [Python replay](verification/src/replay.py) |
| Literature collision check | [Dated scan](audits/public_safe_reports/LITERATURE_AUDIT.md) |

**Partial formalization.** The quadratic separating polynomial factors on the affine seed; the second factor has positive real part along the circle. The explicit logarithmic trace exponentiates to the polynomial factor expression, and its values after successive full turns differ by multiples of 2πi and are pairwise distinct. The construction, continuation and identification of these lifts inside the envelope of holomorphy, including gluing the full exterior, are in the manuscript. [Lean source](formal/closing/Certificate.lean)
