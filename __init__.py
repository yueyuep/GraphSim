from Utils import *
import networkx as nx
from SimRank import *
from Utils import *
if __name__ == '__main__':
    low_version="F:\GraphSim\jsondata\V1.0"
    high_version="F:\GraphSim\jsondata\V1.1"
    CSVfile="F:\GraphSim\outresult.csv"
    base_file_list=[]
    target_file_list=[]
    paiFile=[]
    connectGraph=nx.Graph()
    getfilePath(low_version,base_file_list)
    getfilePath(high_version,target_file_list)
    paiFile=getpairFile(base_file_list,target_file_list)
    connectGraph,A,B=addRoot(paiFile)
    sim,_allSim=simrank(connectGraph,A,B)
    writeCSV(connectGraph,_allSim,CSVfile)
    print("connected!")



