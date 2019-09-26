import networkx as nx
import os
from ParseFile import *
import pandas as pd
import numpy as np
def reNodeName(baseGraph,graph):
    basenodename_List=baseGraph.nodes()
    basenodename_number_List=[]
    for element in basenodename_List:
        if isinstance(element,int):
            basenodename_number_List.append()
    maxnum=max(basenodename_number_List)#找到最大节点的数，在这个基础上进行增加
def getfilePath(path,fileList):
    for item in os.listdir(path):
        current=os.path.join(path,item)
        if os.path.isfile(current):
            fileList.append(current)
        else:
            getfilePath(current,fileList)

def getpairFile(basefileList,targetfileList):
    #只处理文件数目没有变化
    pairfile=[]
    for base in basefileList:
        base_split=base.split("\\")
        base_name=base_split[len(base_split)-1]
        for target in targetfileList:
            target_split=target.split("\\")
            target_name=target_split[len(target_split)-1]
            if base_name==target_name:
                list=[base,target]
                pairfile.append(list)
    return pairfile
def addRoot(pairList):
    graph2graph=[]
    root="Root"
    for pair in pairList:
        g=nx.Graph()
        g1=ParseFile(pair[0])
        g2=ParseFile(pair[1])
        basefileGraph=g1.connectFile()
        targetfileGraph=g2.connectFile()
        basefileGraph_node=g1.getfileName()+"_"+g1.getVersion()#v1.0的文件节点
        targetfileGraph_node=g2.getfileName()+"_"+g2.getVersion()#v1.1的文件节点
        g.add_edges_from(basefileGraph.edges(data=True))
        g.add_edges_from(targetfileGraph.edges(data=True))
        g.add_edge(root,basefileGraph_node,{"connecting":"include"})
        g.add_edge(root, targetfileGraph_node, {"connecting": "include"})
    return g,basefileGraph_node,targetfileGraph_node

def writeCSV(G,sim,resiltUrl):
    label=list(G.nodes())
    dataframe=pd.DataFrame(sim,columns=label,index=label)
    dataframe.to_csv(resiltUrl)





















