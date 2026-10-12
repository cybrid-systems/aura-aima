# Ch. 5 — Adversarial search and games

AIMA 4e §5.2–5.3 (Fig 5.2, 5.3, 5.7). Library: `lib/aima/games.aura`; games in
`lib/problems/fig52.aura` and `lib/problems/tictactoe.aura`.

| Algorithm | Aura | aima-python |
|---|---|---|
| Minimax decision (Fig 5.3) | `minimax-decision` | `minmax_decision` |
| Alpha-beta search (Fig 5.7) | `alpha-beta-search` | `alpha_beta_search` |
| Players / match | `minimax-player`, `alpha-beta-player`, `play-game` | `*_player`, `Game.play_game` |

A Game mirrors the search Problem (a vector of closures plus a stats slot):
`initial actions result utility terminal? to-move`. `game-results` counts
`result()` calls, so the tests check how much alpha-beta prunes, not just which
move it picks.

Covered: the Fig 5.2 two-ply tree (from A, B, C, D), tic-tac-toe positions from
aima-python's tests, and full 3×3 tic-tac-toe from the empty board (alpha-beta
vs alpha-beta is a draw).

Demo: `scripts/run.sh chapters/ch05_games/tictactoe.aura`.
