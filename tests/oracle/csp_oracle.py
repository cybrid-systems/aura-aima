# Expected values for tests/test_csp*.aura, computed with aima-python
# (MIT, https://github.com/aimacode/aima-python, checked at f104e03). Not vendored:
#   cd aima-python && python3 /path/to/aura-aima/tests/oracle/csp_oracle.py
# aima-python breaks MRV / min-conflicts ties at random (argmin_random_tie); the
# Aura port breaks them by taking the first minimum, so we patch that here.
import sys; sys.path.insert(0, '.')
import aima.csp as C
C.argmin_random_tie = lambda seq, key=lambda x: x: min(list(seq), key=key)
def fresh_aus(): return C.MapColoringCSP(list('RGB'), "SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: ")
a = fresh_aus(); print('aus vars', a.variables)
print('aus neighbors', {k: a.neighbors[k] for k in a.variables})
sel = [('first', C.first_unassigned_variable), ('mrv', C.mrv)]
ordv = [('unordered', C.unordered_domain_values), ('lcv', C.lcv)]
inf = [('none', C.no_inference), ('fc', C.forward_checking)]
def show(r, vars_): return None if r is None else [r[v] for v in vars_]
for mk, name in [(fresh_aus, 'aus'), (lambda: C.NQueensCSP(8), 'q8'), (lambda: C.NQueensCSP(4), 'q4'), (lambda: C.NQueensCSP(3), 'q3')]:
    for sn, s in sel:
        for on, o in ordv:
            for i_n, i in inf:
                p = mk(); r = C.backtracking_search(p, s, o, i)
                print(name, sn, on, i_n, show(r, p.variables), p.nassigns, p.nchecks)
# AC-3: final domains are order independent
for label, pre in [('plain', {}), ('WA=R,SA=G', {'WA': 'R', 'SA': 'G'}), ('WA=R,NT=G,Q=R', {'WA':'R','NT':'G','Q':'R'})]:
    p = fresh_aus(); p.support_pruning()
    for v, x in pre.items(): p.curr_domains[v] = [x]
    ok, _ = C.AC3(p)
    print('ac3', label, ok, {v: sorted(p.curr_domains[v]) for v in p.variables} if ok else None)
p = C.MapColoringCSP(list('RG'), "A: B C; B: C"); p.support_pruning(); print('ac3 triangle-2col', C.AC3(p)[0])
