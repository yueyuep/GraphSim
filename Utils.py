import networkx as nx
import os
from ParseFile import *
import pandas as pd
import numpy as np
import networkx as nx
from collections import Iterable
from grakel import Graph
from grakel import GraphKernel
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
def getpairMethodGraph(basefileList,targetfileList):
    # {文件名：{（函数名_v1.0,函数名_v1.1）:[methodgraph1,methodgraph2.......}}
    pairfileList=getpairFile(basefileList,targetfileList)
    pairMethod = {}
    for paifile in pairfileList:
        filename=paifile[0]
        base=paifile[0]
        target=paifile[1]
        baseMethodGraph=ParseFile(base)
        targetMethodGraph=ParseFile(target)
        baseMethodGraphList=baseMethodGraph.getMethodGraph()
        targetMethodGraphList=targetMethodGraph.getMethodGraph()
        #两个文件的函数数目一样的时候
        if len(baseMethodGraphList)==len(targetMethodGraphList):
            tempdic={}
            for B,T in itertools.product(baseMethodGraphList,targetMethodGraphList):
                #为对应的函数名
                if B[0]==T[0]:
                    filename1=B[0]+"_"+baseMethodGraph.getVersion()
                    filename2=B[0]+"_"+targetMethodGraph.getVersion()
                    Bgraph=B[2]

                    Tgraph=T[2]

                    key=(filename1,filename2)
                    value=[Bgraph,Tgraph]
                    tempdic[key]=value

        else:
            pass
        pairMethod[filename]=tempdic
    return pairMethod




def addRoot(pairList):
    """
    #为文件添加根结点root，将两个版本对应得文件用root连接起来
    :param pairList:
    :return:
    """
    graph2graph=[]
    root="Root"
    for pair in pairList:
        g=nx.DiGraph()
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
def unDirection(G):
    #将图中的节点进行反向处理
    #(node ,node ,eges)
    for edge in G.edges(data=True):
        u=edge[0]
        v=edge[1]
        e=G.get_edge_data(u,v)
        G.remove_edge(u,v)
        G.add_edge(v,u,e)
    return G
def list2dic(list):
    dic={}
    for tup in list:
        pnode=tup[0]
        indic=tup[1]
        dic[pnode]=indic
    return dic
def getadjlist(graph):
    num=len(graph.nodes())#结点的个数
    tabel=[]
    #建立索引表
    for node in graph.nodes():
        tabel.append(node)
    #建立邻接矩阵
    adjlist=np.zeros(shape=(num,num))
    node_name={}
    edge_label={}
    #返回3元组（u,v,attri）
    for dic1 in graph.edges(data=True):
        u=dic1[0]
        u_index=tabel.index(u)
        v=dic1[1]
        v_index=tabel.index(v)
        #邻接矩阵添1
        adjlist[u_index][v_index]=1
        #添加结点结点名字标签
        node_name[u_index] = u
        node_name[v_index] = v
        #添加边关系:connecting
        attr=dic1[2]
        edgename=[item for item in attr.values()][0]
        edge_label[(u_index,v_index)]=edgename
    return adjlist,node_name,edge_label
def getMethodSim(pairMethodGraph):
    sim={}
    for filekey in pairMethodGraph.keys():
        file=pairMethodGraph[filekey]
        _sim={}
        for keytupe in file.keys():
            keytupe=tuple(keytupe)
            method=file[keytupe]
            basegraph=method[0]
            targetgraph=method[1]
            adj1, node_label1, edge_label1 = getadjlist(basegraph)
            adj2, node_label2, edge_label2 = getadjlist(targetgraph)
            sp_kernal = GraphKernel(kernel={"name": "shortest_path"}, normalize=True)
            g1 = Graph(adj1, node_label1, edge_label1)
            g2 = Graph(adj2, node_label2, edge_label2)
            tp = sp_kernal.fit_transform([g1])
            sim = sp_kernal.transform([g2])
            _sim[keytupe]=sim
        sim[file] = _sim










































