import copy

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
    new_state = copy.deepcopy(state)  
    new_state[x][y], new_state[x + i][y + j] = new_state[x + i][y + j], new_state[x][y]
    return new_state

def find_x(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]=="x":
                return i,j

def dfs(state, record,lifespan):
    # print(state)
    record.append(state)
    if lifespan:
        if state == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "x"]]:
            return True
        for i in neighbour(state):
            if i in record:
                continue
            if dfs(i, record,lifespan-1):  
                return True
        return False
    return False

input_list = input().strip().split()
init_state = [input_list[i:i+3] for i in range(0, 9, 3)]

i=35
record = []
if dfs(init_state,record,i):
    print(1)
else:
    print(0)
