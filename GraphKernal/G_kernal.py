from grakel import Graph
from grakel import GraphKernel
import networkx as nx
from Utils import *
from numpy import array
from grakel import graph_from_networkx
if __name__ == '__main__':
    low_version = "F:\GraphSim\jsondata\V1.0"
    high_version = "F:\GraphSim\jsondata\V1.1"
    base_file_list = []
    target_file_list = []
    pairfileList=[]
    getfilePath(low_version,base_file_list)
    getfilePath(high_version,target_file_list)
    PairMethodGraph=getpairMethodGraph(base_file_list,target_file_list)
    SIm=getMethodSim(PairMethodGraph)

    print("kernal_Done!")


