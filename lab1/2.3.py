import heapq

class Node:
    def __init__(self, state, dist):
        self.state = state
        self.dist = dist

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
            neighbors.append(''.join(new_state))
    return neighbors

def dijkstra(start_state):
    start_str = to_string(start_state)
    target_str = "12345678x"
    priority_queue = [Node(start_str, 0)]
    visited = set()
    visited.add(start_str)

    while priority_queue:
        current = heapq.heappop(priority_queue)
        if current.state == target_str:
            return current.dist

        for neighbor in get_neighbors(current.state):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(priority_queue, Node(neighbor, current.dist + 1))

    return -1

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

input_list = input().strip().split()
init_state = [input_list[i:i+3] for i in range(0, 9, 3)]

if is_solvable(init_state):
    print(dijkstra(init_state))
else:
    print(-1)