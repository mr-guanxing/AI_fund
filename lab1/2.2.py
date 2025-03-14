import copy
from queue import Queue
class Node():
    def __init__(self,state,dist):
        self.state=state
        self.dist = dist

def neighbour(state):
    li=[]
    x,y = find_x(state)
    for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
        if valid(x+i,y+j):
            li.append(switch(state,x,y,i,j))
    return li

def valid(x,y):
    return 0<=x<3 and 0<=y<3

def switch(state, x, y, i, j):
    new_state = copy.deepcopy(state)  # 创建状态的深拷贝
    new_state[x][y], new_state[x + i][y + j] = new_state[x + i][y + j], new_state[x][y]
    return new_state

def find_x(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]=="x":
                return i,j

def bfs(node:Node,record,my_q):
    state = node.state
    if state == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "x"]]:
            return node.dist
    for i in neighbour(state):
        if i in record:
            continue
        record.append(state)
        my_q.put(Node(i,node.dist+1))
    return False
        


input_list = input().strip().split()
init_state = [input_list[i:i+3] for i in range(0, 9, 3)]
record = [init_state]
q = Queue()
q.put(Node(init_state,0))
while not q.empty():
    my_node = q.get()
    print(my_node.dist)
    result = bfs(my_node,record,q)
    if result : 
        print(result)
        break

print(-1)