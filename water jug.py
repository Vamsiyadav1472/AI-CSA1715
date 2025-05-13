from collections import deque
def water_jug_bfs(a, b, target):
    visited = set()
    q = deque()
    q.append((0, 0, []))  
    while q:
        x, y, path = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]
        if x == target or y == target:
            return path
        next_states = set([
            (a, y),     
            (x, b),     
            (0, y),     
            (x, 0),     
            (0, x+y) if x+y <= b else (x-(b-y), b),  
            (x+y, 0) if x+y <= a else (a, y-(a-x))   
        ])
        for state in next_states:
            if state not in visited:
                q.append((state[0], state[1], path))
    return None
solution = water_jug_bfs(4, 3, 2)
if solution:
    for step in solution:
        print("Jug1:", step[0], "Jug2:", step[1])
else:
    print("No solution")
