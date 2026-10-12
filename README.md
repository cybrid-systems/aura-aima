# aura-aima

Algorithms from Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA),
rewritten in [Aura](https://github.com/cybrid-systems/aura) — search, games, CSP, MDP —
to exercise Aura on textbook-sized programs and file the bugs found.
Sibling of [aura-rl-sutton](https://github.com/cybrid-systems/aura-rl-sutton).

Reference implementation: [aimacode/aima-python](https://github.com/aimacode/aima-python)
(MIT). Nothing from it is vendored here: algorithms are rewritten from the book's
pseudocode, following aima-python's control flow so that results line up. Expected
values come from `tests/oracle/*.py`, run against an aima-python checkout; the
numbers are copied into the Aura tests.

## Status

| Part | AIMA | State |
|---|---|---|
| Search | ch. 3 | **done** — BFS/DFS (tree + graph), UCS, greedy, A*, DLS, IDS; 8-puzzle, Romania, Australia, grid |
| Games | ch. 5 | **done** — minimax, alpha-beta, Fig 5.2 tree, tic-tac-toe (positions + full game) |
| CSP | ch. 6 | **done** — backtracking (first/MRV, unordered/LCV, none/FC), AC-3, min-conflicts; Australia + n-queens |
| MDP | ch. 17 | next |

See `STATE.txt` (machine-readable) and `IMPROVEMENTS.md` (Aura notes).

## Running

All code runs in Aura's **Soft** face: `AURA_SANDBOX=off AURA_PIPELINE_STRICT=0`
(`scripts/env.sh` sets both, plus `AURA_PATH`).

```sh
export AURA_BIN=$HOME/aura/build-rel/aura   # RelWithDebInfo build recommended
scripts/run_tests.sh                         # all tests/*.aura
scripts/run.sh chapters/ch03_search/romania.aura
```

## Layout

```
lib/aima/        search.aura (Problem/Node/searchers), pq.aura (heap), check.aura
lib/aima/        games.aura (Game, minimax, alpha-beta, play-game), csp.aura, list.aura (lmap)
lib/problems/    graph.aura (Romania, Australia), eight-puzzle.aura, grid.aura, fig52.aura, tictactoe.aura, map-coloring.aura
chapters/        per-chapter demos + notes
tests/           test_*.aura; tests/oracle/ aima-python scripts and their output
```

---

## 中文说明

把 AIMA（《人工智能：一种现代方法》）里的算法用 Aura 重写：搜索、博弈、CSP、MDP。目的是用教科书规模的程序压一压 Aura，发现问题就提到 cybrid-systems/aura。和 aura-rl-sutton 是同一套做法。

参照实现是 aima-python（MIT），**没有拷贝它的代码**：算法按书里的伪代码自己写，控制流跟 aima-python 对齐，这样结果能逐项对上。期望值由 `tests/oracle/*.py` 在 aima-python 仓库里跑出来，再抄进 Aura 测试。

进度：第 3 章搜索已完成（BFS/DFS 树/图搜索、UCS、贪心、A*、DLS、IDS；8 数码、罗马尼亚、澳大利亚地图、网格）。测试不只对路径和代价，还对 aima-python `InstrumentedProblem` 的三个计数（扩展数 / 目标测试数 / 生成状态数），这样边界顺序和平局规则也被钉死。第 5 章博弈也已完成：minimax、alpha-beta、图 5.2 博弈树、井字棋（残局 + 空棋盘整局），对的是走法和 result() 调用次数。第 6 章 CSP 也已完成：回溯（MRV/LCV/前向检查）、AC-3、最小冲突，在澳大利亚地图着色和 N 皇后上对 aima-python 的解与 nassigns/nchecks 计数。下一步是第 17 章 MDP。

运行方式见上：Soft 模式（`AURA_SANDBOX=off AURA_PIPELINE_STRICT=0`），用 `AURA_BIN` 指向 Aura 可执行文件。

## License

Apache-2.0. aima-python is MIT and is cited, not included.
