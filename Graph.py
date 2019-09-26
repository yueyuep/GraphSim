import networkx as nx
class ParseGraph:
    node_num=0
    succs=[]
    attribute={}
    methodName=""
    Version=""
    callMethodNameReferTo={}
    g=nx.DiGraph()
    def __init__(self,method):
        graph=nx.DiGraph()
        self.node_num=method["n_num"]
        self.succs=method["succs"]
        self.attribute=method["Attribute"]
        self.callMethodNameReferTo=method["callMethodNameReferTo"]
        self.methodName=method["MethodName"]
        self.Version=method["Version"]
    def Parse(self):#处理单个函数的调用关系
        g = nx.Graph()
        # 添加节点间前后继关系，单个文件内
        for i,node in zip(range(self.node_num),self.succs):
            for j in node:
                if i==0:
                    #添加函数名字指向下属节点的边关系
                    methodNode=self.Version+"_"+self.methodName#文件名+版本名来统一节点
                    u = str(i) + "_" + self.Version + "_" + self.methodName
                    v=str(j) + "_" + self.Version + "_" + self.methodName
                    g.add_edge(methodNode, u, {"connection": "include"})  # 函数名包含属下节点关系
                    g.add_edge(u, v, {"connection": "succes"})  # 后继节点类型
                else:
                    #函数内各种节点的关系
                    u = str(i) + "_" + self.Version + "_" + self.methodName
                    v = str(j) + "_" + self.Version + "_" + self.methodName
                    g.add_edge(u, v, {"connection": "succes"})  # 后继节点类型
                    # g.add_node()

        #添加函数调用节点，用文件名节点代替表示
        for callnode in self.callMethodNameReferTo.keys():
            callednamedic=self.callMethodNameReferTo[callnode]
            calledfilename=list(callednamedic.keys())[0]#被调用函数所在的文件名
            calledmethodname=callednamedic[calledfilename]+"_"+self.Version+"_"+self.methodName#被调用函数的名字
            recallnode=str(callnode)+"_"+self.Version+"_"+self.methodName
            g.add_edge(recallnode,calledmethodname,{"connection":"call"})
        self.g=g
        return g








