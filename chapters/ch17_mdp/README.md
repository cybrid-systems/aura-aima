# Ch. 17 — Making complex decisions (MDPs)

AIMA 4e §17.1–17.2 (Fig 17.1, 17.4, 17.7; Eq 17.4). Library: `lib/aima/mdp.aura`.

| Algorithm | Aura | aima-python |
|---|---|---|
| Grid MDP (0.8 intended / 0.1 each side) | `make-grid-mdp` | `GridMDP` |
| Value iteration (Fig 17.4) | `value-iteration` | `value_iteration` |
| Greedy policy (Eq 17.4) | `best-policy` | `best_policy` |
| Policy evaluation, k = 20 sweeps | `policy-evaluation!` | `policy_evaluation` |
| Policy iteration (Fig 17.7) | `policy-iteration` | `policy_iteration` |
| Q-value | `q-value` | `q_value` |

Tests (`tests/test_mdp.aura`): the Fig 17.1 4×3 world with R = −0.04, −0.1 and −2,
plus aima-python's 6×5 grid with four terminals. For each grid:
- value-iteration utilities at ε = 0.001 and 0.01 (all states, within 1e-6);
- the greedy policy;
- the policy from policy iteration.

Utilities and policies match aima-python exactly. For example, the Fig 17.1
utilities are U(0,0)=0.2963, U(2,2)=0.7954, and the policy, listed in sorted (x, y)
state order, is `NNEEENNEW..` (`.` marks the terminals).

Differences from aima-python:
- Policy iteration starts from "East everywhere" instead of a random policy. The
  oracle checks that 5 random starts converge to the same policy.
- States are visited in sorted (x, y) order (Python iterates a set). This only
  matters for in-place policy evaluation, and the policies are unaffected.

Run: `scripts/run.sh chapters/ch17_mdp/grid_4x3.aura`.
