from grakel import GraphKernel
from grakel import Graph
from numpy import array
if __name__ == '__main__':

    H2O = Graph([[0, 1, 1], [1, 0, 0], [1, 0, 0]], {0: 'O', 1: 'H', 2: 'H'})
    H3O = Graph([[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], {0: 'O', 1: 'H', 2: 'H', 3: 'H'})
    H2Od = dict()
    H2Od[0] = Graph({'a': {'b': 1., 'c': 1.}, 'b': {'a': 1}, 'c': {'a': 1}})
    H2Od[1] = Graph({('a', 'b'): 1., ('a', 'c'): 1., ('c', 'a'): 1., ('b', 'a'): 1.})
    H2Ot = array([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    H2O_labels = {0: 'O', 1: 'H', 2: 'H'}
    H2O_edge_labels = {(0, 1): 'pcb', (1, 0): 'pcb', (0, 2): 'pcb', (2, 0): 'pcb'}
    adj_graph = Graph(H2Ot, H2O_labels, H2O_edge_labels, "all")
    #==============================================================================
    sp_kernal=GraphKernel(kernel = {"name": "shortest_path"}, normalize=True)
    kernal_m=sp_kernal.fit_transform([adj_graph])
    Sim=sp_kernal.transform([H3O])
    print("the kernal_m is :{m}\n the sim is :{s}".format(m=kernal_m,s=Sim))