# Expected values for tests/test_mdp.aura, computed with aima-python
# (MIT, https://github.com/aimacode/aima-python, checked at f104e03). Not vendored:
#   cd aima-python && python3 /path/to/aura-aima/tests/oracle/mdp_oracle.py
# States are printed in sorted (x, y) order. Policy iteration is run from 5 random
# initial policies plus the all-East policy; all must agree (the Aura port starts
# from the first action, East).
import sys, random; sys.path.insert(0, '.')
from aima.mdp import *
N = {(1, 0): 'E', (0, 1): 'N', (-1, 0): 'W', (0, -1): 'S', None: '.'}
def envs():
    return [('fig17', [[-0.04, -0.04, -0.04, +1], [-0.04, None, -0.04, -1], [-0.04, -0.04, -0.04, -0.04]], [(3, 2), (3, 1)]),
            ('r-0.1', [[-0.1, -0.1, -0.1, +1], [-0.1, None, -0.1, -1], [-0.1, -0.1, -0.1, -0.1]], [(3, 2), (3, 1)]),
            ('r-2', [[-2, -2, -2, +1], [-2, None, -2, -1], [-2, -2, -2, -2]], [(3, 2), (3, 1)]),
            ('6x5', [[-1.0, -0.1, -0.1, -0.1, -0.1, 0.5], [-0.1, None, None, -0.5, -0.1, -0.1], [-0.1, None, 1.0, 3.0, None, -0.1],
                     [-0.1, -0.1, -0.1, None, None, -0.1], [0.5, -0.1, -0.1, -0.1, -0.1, -1.0]], [(2, 2), (3, 2), (0, 4), (5, 0)])]
for name, g, t in envs():
    m = GridMDP([r[:] for r in g], terminals=t)
    S = sorted(m.states)
    for eps in (0.001, 0.01):
        U = value_iteration(m, eps)
        print(name, 'vi', eps, ' '.join('%.6f' % U[s] for s in S))
    pol = best_policy(m, value_iteration(m, 0.001))
    print(name, 'best', ''.join(N[pol[s]] for s in S))
    pis = set()
    for seed in range(5):
        random.seed(seed); p = policy_iteration(GridMDP([r[:] for r in g], terminals=t)); pis.add(''.join(N[p[s]] for s in S))
    print(name, 'pi', sorted(pis))
    print(name, 'states', S)
