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

    pairfileList=getpairFile(base_file_list,target_file_list)
    for pair in pairfileList:
        basefile=pair[0]
        targetfile=pair[1]
        g1=ParseFile(basefile)
        g2=ParseFile(targetfile)
        #basefileGraph、targetfileGraph分别为待比较结点得图
        _basefileGraph=g1.connectFile()
        _targetfileGraph=g2.connectFile()
        adj1,node_label1,edge_label1=getadjlist(_basefileGraph)
        adj2,node_label2,edge_label2=getadjlist(_targetfileGraph)
        sp_kernal=GraphKernel(kernel={"name": "shortest_path"}, normalize=True)
        g1=Graph(adj1,node_label1,edge_label1)
        g2=Graph(adj2,node_label2,edge_label2)
        tp=sp_kernal.fit_transform([g1])
        sim=sp_kernal.transform([g2])
    print("kernal_Done!")


