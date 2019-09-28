from Utils import *
import networkx as nx
from SimRank import *
import numpy as np
import random
from Utils import *
if __name__ == '__main__':
    low_version="F:\GraphSim\jsondata\V1.0"
    high_version="F:\GraphSim\jsondata\V1.1"
    CSVfile="F:\GraphSim"+"\_"+str(random.randint(0,100))+"_outresult.csv"
    base_file_list=[]
    target_file_list=[]
    paiFile=[]
    connectGraph=nx.Graph()
    getfilePath(low_version,base_file_list)
    getfilePath(high_version,target_file_list)
    paiFile=getpairFile(base_file_list,target_file_list)
    connectGraph,A,B=addRoot(paiFile)
    #反向处理图中所有的边
    connectGraph=unDirection(connectGraph)
    #A、B两个节点的相似度，整个矩阵的相似度矩阵
    sim,_allSim=simrank(connectGraph,A,B)
    #相似度矩阵存到CSV文件当中
    writeCSV(connectGraph,_allSim,CSVfile)
    #求出每行最大值出现的节点位置
    max_index=np.argmax(_allSim,axis=1)#
    print("connected!")



