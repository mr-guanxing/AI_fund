import heapq

class Node:
    def __init__(self, state, dist, path):
        self.state = state
        self.dist = dist
        self.path = path

    def __lt__(self, other):
        return self.dist < other.dist

def to_string(state):
    return ''.join(''.join(row) for row in state)

def to_list(state_str):
    return [list(state_str[i:i+3]) for i in range(0, 9, 3)]

def find_x(state_str):
    index = state_str.index('x')
    return index // 3, index % 3

def valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_neighbors(state_str):
    neighbors = []
    x, y = find_x(state_str)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if valid(nx, ny):
            new_state = list(state_str)
            new_state[x * 3 + y], new_state[nx * 3 + ny] = new_state[nx * 3 + ny], new_state[x * 3 + y]
            neighbors.append((''.join(new_state), (dx, dy)))
    return neighbors

def inversion_number(state):
    state_str = to_string(state)
    state_str = state_str.replace("x", "")  
    inv_count = 0
    for i in range(len(state_str)):
        for j in range(i + 1, len(state_str)):
            if state_str[i] > state_str[j]:
                inv_count += 1
    return inv_count

def is_solvable(state):
    return inversion_number(state) % 2 == 0

def Cost(state_str):
    target_pos = {str(i): (i // 3, i % 3) for i in range(1, 9)}
    target_pos["x"] = (2, 2)  
    cost = 0
    for i in range(3):
        for j in range(3):
            element = state_str[i * 3 + j]
            tx, ty = target_pos[element]
            cost += abs(tx - i) + abs(ty - j)
    return cost

def a_star(start_state):
    start_str = to_string(start_state)
    target_str = "12345678x"
    priority_queue = [Node(start_str, Cost(start_str), "")]
    visited = set()
    visited.add(start_str)

    while priority_queue:
        current = heapq.heappop(priority_queue)
        if current.state == target_str:
            return current.path

        for neighbor, move in get_neighbors(current.state):
            if neighbor not in visited:
                visited.add(neighbor)
                new_cost = current.dist - Cost(current.state) + Cost(neighbor) + 1
                new_path = current.path + {(-1,0): "u", (1,0): "d", (0,-1): "l", (0,1): "r"}[move]
                heapq.heappush(priority_queue, Node(neighbor, new_cost, new_path))

    return "unsolvable"

input_list = input().strip().split()
init_state = [input_list[i:i+3] for i in range(0, 9, 3)]

if is_solvable(init_state):
    print(a_star(init_state))
else:
    print("unsolvable")