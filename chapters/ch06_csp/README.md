# Ch. 6 — Constraint satisfaction problems

AIMA 4e §6.2–6.4 (Fig 6.3, 6.5, 6.8). Library: `lib/aima/csp.aura`; problems in
`lib/problems/map-coloring.aura` and `make-nqueens-csp`.

| Algorithm | Aura | aima-python |
|---|---|---|
| Backtracking search (Fig 6.5) | `backtracking-search` | `backtracking_search` |
| Variable order: first / MRV | `first-unassigned-variable`, `mrv` | same names |
| Value order: unordered / LCV | `unordered-domain-values`, `lcv` | same names |
| Inference: none / forward checking | `no-inference`, `forward-checking` | same names |
| AC-3 (Fig 6.3) | `ac3` | `AC3` |
| Min-conflicts (Fig 6.8) | `min-conflicts` (seeded LCG) | `min_conflicts` |

Tests:
- Backtracking: all 8 combinations of {first, MRV} × {unordered, LCV} × {none, FC} on
  Australia (3 colours), 8-queens, 4-queens and 3-queens (no solution). The solution
  and aima-python's `nassigns` / `nchecks` counters must match. That pins down
  value order after restore, which mirrors Python's list.remove / append.
- AC-3: fixpoint domains for 3 pre-assignments, an inconsistent case, and a 2-colour
  triangle (which AC-3 cannot refute, as in aima-python).
- Min-conflicts: valid solutions for Australia, 8- and 20-queens with two seeds.

Differences from aima-python:
- MRV ties go to the first minimum, so counters are comparable; the oracle patches
  `argmin_random_tie` the same way.
- Min-conflicts value ties stay random (seeded): with first-minimum ties it cycles and
  never solves 8-queens, in aima-python too.
- AC-3 processes arcs FIFO. aima-python orders them by domain size, which changes
  nchecks but not the fixpoint.
- Like aima-python's parse_neighbors, Tasmania ("T: ") is dropped from the
  Australia CSP.
