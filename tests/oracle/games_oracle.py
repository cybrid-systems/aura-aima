# Expected values for tests/test_games*.aura, computed with aima-python
# (MIT, https://github.com/aimacode/aima-python, checked at f104e03). Not vendored:
#   cd aima-python && python3 /path/to/aura-aima/tests/oracle/games_oracle.py
# Move lists are row-major sorted (aima's test gen_state uses set order; we fix it).
# "results" = number of game.result() calls (successor states generated).
import sys; sys.path.insert(0, '.')
from aima.games import *

class Counted:
    def __init__(s, g): s.g = g; s.n = 0
    def __getattr__(s, a): return getattr(s.g, a)
    def result(s, st, m): s.n += 1; return s.g.result(st, m)

def gen_state(to_move, xs, os_):
    moves = sorted(set((x, y) for x in range(1, 4) for y in range(1, 4)) - set(xs) - set(os_))
    board = {}
    for p in xs: board[p] = 'X'
    for p in os_: board[p] = 'O'
    return GameState(to_move=to_move, utility=0, board=board, moves=moves)

for s in 'ABCD':
    for nm, f in [('minimax', minmax_decision), ('alphabeta', alpha_beta_search)]:
        g = Counted(Fig52Game()); print('fig52', s, nm, f(s, g), g.n)
print('fig52 play', Fig52Game().play_game(alpha_beta_player, alpha_beta_player))
cases = [('X', [(1,1),(3,3)], [(1,2),(3,2)]), ('O', [(1,1),(3,1),(3,3)], [(1,2),(3,2)]),
         ('O', [(1,1)], []), ('X', [(1,1),(3,1)], [(2,2),(3,1)]),
         ('X', [], [])]
for c in cases:
    for nm, f in [('minimax', minmax_decision), ('alphabeta', alpha_beta_search)]:
        if nm == 'minimax' and len(c[1]) + len(c[2]) < 2: continue
        g = Counted(TicTacToe()); print('ttt', c, nm, f(gen_state(*c), g), g.n)
t = TicTacToe(); t.initial = gen_state('X', [], [])
print('ttt play ab-vs-ab', t.play_game(alpha_beta_player, alpha_beta_player))
