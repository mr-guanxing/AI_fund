from queue import Queue
class Node():
    def __init__(self,number):
        self.number = number
        self.edgelist=[]
        self.colour = "white"
        self.distence = 0

    def add_edge(self,node):
        self.edgelist.append(node)

class Graph():
    def __init__(self,number):
        self.nodes = [ Node(i) for i in range(1,number+1)]

def BFS(node:Node,my_q):
    node.colour = "gray"
    for i in node.edgelist:
        if i.colour == "white":
            i.colour = "gray"
            my_q.put(i)
            i.distence = node.distence+1
    node.colour = "black"


n, m = map(int, input().split())
q = Queue()
# 初始化一个列表来存储边的信息
my_graph = Graph(n)

# 读取接下来的 m 行，每行包含两个整数 u 和 v
for i in range(m):
    u, v = map(int, input().split())
    my_graph.nodes[u-1].edgelist.append(my_graph.nodes[v-1])

q.put(my_graph.nodes[0])

while not q.empty():
    my_node = q.get()
    BFS(my_node,q)

dis = my_graph.nodes[n-1].distence
if dis == 0 and n!=1:
    print(-1)
else:
    print(dis)




