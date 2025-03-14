import copy
import heapq
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
            

def dijkstra(start):
    priority_queue = [(0, start)]  
    record = []
    while priority_queue:
        current_distance, current_state = heapq.heappop(priority_queue)
        # print(current_distance)
        if current_state == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "x"]]:
            return current_distance
        
        if current_state in record:
            continue
        record.append(current_state)
        for neighbor in neighbour(current_state):
            weight = 1
            if neighbor  not in record: 
                new_distance = current_distance + weight
                heapq.heappush(priority_queue, (new_distance, neighbor))
    return -1

input_list = input().strip().split()
init_state = [input_list[i:i+3] for i in range(0, 9, 3)]
print(dijkstra(init_state))

