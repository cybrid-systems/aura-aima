# Ch. 3 — Solving problems by searching

AIMA 4e §3.3–3.5 (Fig. 3.7, 3.11, 3.14, 3.17, 3.18). Library code: `lib/aima/search.aura`,
`lib/aima/pq.aura`; problems in `lib/problems/`.

| Algorithm | Aura | aima-python |
|---|---|---|
| Breadth-first tree search | `breadth-first-tree-search` | `breadth_first_tree_search` |
| Depth-first tree search | `depth-first-tree-search` | `depth_first_tree_search` |
| Breadth-first graph search (Fig 3.11, early goal test) | `breadth-first-graph-search` | `breadth_first_graph_search` |
| Depth-first graph search | `depth-first-graph-search` | `depth_first_graph_search` |
| Best-first graph search on f | `best-first-graph-search` | `best_first_graph_search` |
| Uniform-cost (Fig 3.14) | `uniform-cost-search` | `uniform_cost_search` |
| Greedy best-first (f = h) | `greedy-best-first-search` | `best_first_graph_search(p, p.h)` |
| A* (f = g + h) | `astar-search` | `astar_search` |
| Depth-limited (Fig 3.17) | `depth-limited-search` | `depth_limited_search` |
| Iterative deepening (Fig 3.18) | `iterative-deepening-search` | `iterative_deepening_search` |

Problems: Romania (Arad→Bucharest, Oradea→Neamt, straight-line h from map
coordinates), Australia (Q→WA, unit costs), 8-puzzle (misplaced-tiles h), 5×5 grid
with walls (Manhattan h, plus an unreachable goal).

Every problem is instrumented like aima-python's `InstrumentedProblem`:
`search-succs` (= node expansions), `search-goal-tests`, `search-states`
(successor states generated). The tests require these counters, not only the
path and cost, to equal aima-python — which pins down frontier order,
tie-breaking (f, insertion counter) and frontier replacement.

Run the demo: `scripts/run.sh chapters/ch03_search/romania.aura`.
