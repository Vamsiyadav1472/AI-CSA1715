from collections import deque
def is_valid(m1, c1, m2, c2):
    return all(x >= 0 and x <= 3 for x in [m1, c1, m2, c2]) and \
           (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2)
def bfs():
    start = (3, 3, 0, 0, 1)
    goal = (0, 0, 3, 3, 0)
    queue = deque([(start, [])])
    visited = set()
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    while queue:
        (m1, c1, m2, c2, boat), path = queue.popleft()
        if (m1, c1, m2, c2, boat) in visited:
            continue
        visited.add((m1, c1, m2, c2, boat))
        if (m1, c1, m2, c2, boat) == goal:
            return path + [(m1, c1, m2, c2, boat)]
        for m, c in moves:
            if boat:
                nm1, nc1, nm2, nc2 = m1 - m, c1 - c, m2 + m, c2 + c
                nb = 0
            else:
                nm1, nc1, nm2, nc2 = m1 + m, c1 + c, m2 - m, c2 - c
                nb = 1
            if is_valid(nm1, nc1, nm2, nc2):
                queue.append(((nm1, nc1, nm2, nc2, nb), path + [(m1, c1, m2, c2, boat)]))
result = bfs()
for step in result:
    print(f"Left M:{step[0]} C:{step[1]} | Right M:{step[2]} C:{step[3]} | Boat: {'Left' if step[4] else 'Right'}")
