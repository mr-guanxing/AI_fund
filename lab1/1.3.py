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


def dijkstra(graph, start_node: Node):
    start_node.distance = 0  
    priority_queue = [(0, start_node)]  
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node.colour == "black":
            continue
        current_node.colour = "black"
        for neighbor, weight in current_node.edge_cost_dic.items():
            if neighbor.colour != "black": 
                new_distance = current_distance + weight
                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
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
r= result[n]
if r == float('inf'):
    print(-1)
else:
    print(r)

