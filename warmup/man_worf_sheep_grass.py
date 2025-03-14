from collections import deque

# 初始状态：左边有羊、狼、菜，右边为空，船在左边
initial_state = ({"F", "C", "G", "W"}, set(), True)

# 目标状态：左边为空，右边有羊、狼、菜，船在右边
goal_state = (set(), {"F", "C", "G", "W"}, False)

# 检查状态是否合法
def is_valid_state(state):
    left, right, boat = state
    # 检查左边是否安全
    if "C" in left and "G" in left and "F" not in left:  # 羊和狼在左边，没有人在场
        return False
    if "C" in left and "W" in left and "F" not in left:  # 羊和菜在左边，没有人在场
        return False
    # 检查右边是否安全
    if "C" in right and "G" in right and "F" not in right:  # 羊和狼在右边，没有人在场
        return False
    if "C" in right and "W" in right and "F" not in right:  # 羊和菜在右边，没有人在场
        return False
    return True

# 获取下一个合法状态
def get_next_states(state):
    left, right, boat = state
    next_states = []
    # 如果船在左边
    if boat:
        for item in left:
            new_left = left.copy()
            new_right = right.copy()
            new_left.remove(item)
            new_right.add(item)
            if item == "F":  # 如果移动的是人，船也移动
                new_state = (new_left, new_right, False)
            else:  # 如果移动的是物品，人必须陪同
                new_left.remove("F")
                new_right.add("F")
                new_state = (new_left, new_right, False)
            if is_valid_state(new_state):
                next_states.append(new_state)
    # 如果船在右边
    else:
        for item in right:
            new_left = left.copy()
            new_right = right.copy()
            new_right.remove(item)
            new_left.add(item)
            if item == "F":  # 如果移动的是人，船也移动
                new_state = (new_left, new_right, True)
            else:  # 如果移动的是物品，人必须陪同
                new_right.remove("F")
                new_left.add("F")
                new_state = (new_left, new_right, True)
            if is_valid_state(new_state):
                next_states.append(new_state)
    return next_states

# 使用 BFS 搜索路径
def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [initial_state])])  # 队列存储当前状态和路径
    visited = set()  # 记录已访问的状态
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path  # 找到目标状态，返回路径
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

# 打印路径
def print_path(path):
    for i, state in enumerate(path):
        left, right, boat = state
        boat_side = "Left" if boat else "Right"
        print(f"Step {i + 1}: Left={left}, Right={right}, Boat={boat_side}")

# 执行搜索
path = bfs(initial_state, goal_state)
if path:
    print("找到解决方案：")
    print_path(path)
else:
    print("没有找到解决方案。")