# Expected values for tests/test_search*.aura, computed with aima-python
# (MIT, https://github.com/aimacode/aima-python, checked at f104e03).
# Not vendored: run from an aima-python checkout:
#   cd aima-python && python3 /path/to/aura-aima/tests/oracle/search_oracle.py
# Output columns: searcher path cost succs goal_tests states (InstrumentedProblem).
import sys; sys.path.insert(0,'.')
from aima.search import *
def run(name, s, p):
    ip = InstrumentedProblem(p); n = s(ip)
    if n is None or n=='cutoff': print(name, n, ip.succs, ip.goal_tests, ip.states); return
    print(name, ' '.join(map(str,n.path_states())), n.path_cost, ip.succs, ip.goal_tests, ip.states)
gs=[('bfs-tree',breadth_first_tree_search),('bfs-graph',breadth_first_graph_search),('dfs-graph',depth_first_graph_search),
    ('ucs',uniform_cost_search),('greedy',lambda p: best_first_graph_search(p, p.h)),('astar',astar_search),('ids',iterative_deepening_search),('dls50',depth_limited_search)]
for (a,b,g) in [('Arad','Bucharest',romania_map),('Oradea','Neamt',romania_map),('Q','WA',australia_map)]:
    print('##',a,b)
    for nm,s in gs:
        if g is australia_map and nm in('greedy','astar'): continue
        run(nm,s,GraphProblem(a,b,g))
print('## 8puzzle')
for nm,s in [('bfs-graph',breadth_first_graph_search),('ucs',uniform_cost_search),('astar',astar_search)]:
    p=EightPuzzle((2,4,3,1,5,6,7,8,0)); ip=InstrumentedProblem(p); n=s(ip)
    print(nm, n.solution(), n.path_cost, ip.succs, ip.goal_tests, ip.states)
print('## neighbors')
for k in romania_map.graph_dict: print(k, [(b,d) for b,d in romania_map.graph_dict[k].items()])
print('## loc', romania_map.locations)
for k in australia_map.graph_dict: print(k, list(australia_map.graph_dict[k].items()))
print('## grid')
walls=[(2,0),(2,1),(2,2),(2,3)]
for nm,s in [('bfs-graph',breadth_first_graph_search),('ucs',uniform_cost_search),('astar',astar_search),('dfs-graph',depth_first_graph_search)]:
    for (g,obs) in [((4,0),walls),((4,4),[(3,4),(4,3)])]:
        ip=InstrumentedProblem(GridProblem((0,0),g,5,5,obstacles=obs)); n=s(ip)
        print(nm,g, None if n is None else (n.path_states(), n.path_cost), ip.succs, ip.goal_tests, ip.states)
print('## ep2')
for st in [(1,2,3,4,5,6,0,7,8)]:
    ip=InstrumentedProblem(EightPuzzle(st)); n=astar_search(ip); print(n.solution(), ip.succs, ip.goal_tests, ip.states)
