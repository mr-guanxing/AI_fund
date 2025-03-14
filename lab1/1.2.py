import heapq

class Node():
    def __init__(self, number):
        self.number = number
        self.edge_cost_dic = {}  
        self.colour = "white"   
        self.distance = float('inf') 

    def add_edge(self, node, weight):
        self.edge_cost_dic[node] = weight


class Graph():
    def __init__(self, number):
        self.nodes = [Node(i) for i in range(1, number + 1)]

def find_min(dislist):
    if not dislist:  
        return None, None

    min_index = 0
    for i in range(len(dislist)):
        if dislist[i][0] < dislist[min_index][0]:
            min_index = i

    min_dst, node = dislist.pop(min_index)
    return min_dst, node

def dijkstra(graph, start_node: Node):
    start_node.distance = 0  
    dist_list = [(0, start_node)]  
    while dist_list:
        current_distance, current_node = find_min(dist_list)
        if current_node.colour == "black":
            continue
        current_node.colour = "black"
        for neighbor, weight in current_node.edge_cost_dic.items():
            if neighbor.colour != "black": 
                new_distance = current_distance + weight
                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    dist_list.append((new_distance, neighbor))
    return {node.number: node.distance for node in graph.nodes}



n, m = map(int, input().split())
my_graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    node_u = my_graph.nodes[u - 1]
    node_v = my_graph.nodes[v - 1]

    if node_v in node_u.edge_cost_dic:
        node_u.edge_cost_dic[node_v] = min(node_u.edge_cost_dic[node_v], w)
    else:
        node_u.edge_cost_dic[node_v] = w

start_node = my_graph.nodes[0]  
result = dijkstra(my_graph, start_node)
print(result[n])
