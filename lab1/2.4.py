import copy
import heapq
class Node():
    def __init__(self,state,dist):
        self.state=state
        self.dist = dist

def neighbour(state):
    dic={(0,1):"r",(0,-1):"l",(1,0):"u",(-1,0):"d"}
    li=[]
    li2=[]
    x,y = find_x(state)
    for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
        if valid(x+i,y+j):
            li.append(switch(state,x,y,i,j))
            li2.append(dic[(i,j)])
    return li,li2

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
            
def Cost(state):
    cost = 0
    for i in range(1,9):
        tx,ty = (i-1)//3,(i-1)%3
        x,y = find_element(state,str(i))
        cost += abs(tx-x)+abs(ty-y)
    return cost

def find_element(state,element):
    for i in range(3):
        for j in range(3):
            if state[i][j]==element:
                return i,j
            

def a_star(start):
    priority_queue = [(Cost(start),0,"",start)]  
    record = []
    while priority_queue:
        current_cost,current_distance,current_path,current_state = heapq.heappop(priority_queue)
        if current_state == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "x"]]:
            return current_distance,current_path
        
        if current_state in record:
            continue
        record.append(current_state)
        for neighbor,op in zip(*neighbour(current_state)):
            if neighbor  not in record: 
                new_distance = current_distance + 1
                heapq.heappush(priority_queue, (new_distance+Cost(neighbor),new_distance,current_path+op,neighbor))
    return -1,"unsolvable"

input_list = input().strip().split()
init_state = [input_list[i:i+3] for i in range(0, 9, 3)]
print(a_star(init_state)[1])
# print(Cost(init_state))
