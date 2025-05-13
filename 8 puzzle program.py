import heapq
goal = [[1,2,3],[4,5,6],[7,8,0]]
def manhattan(s):
    return sum(abs(i - (v-1)//3) + abs(j - (v-1)%3)
               for i, row in enumerate(s)
               for j, v in enumerate(row) if v)
def neighbors(s):
    x, y = [(i, row.index(0)) for i, row in enumerate(s) if 0 in row][0]
    moves = [(x+dx, y+dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]]
    result = []
    for nx, ny in moves:
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [r[:] for r in s]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)
    return result
def a_star(start):
    heap = [(manhattan(start), 0, start, [])]
    seen = set()
    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state == goal: return path + [state]
        key = tuple(map(tuple, state))
        if key in seen: continue
        seen.add(key)
        for n in neighbors(state):
            heapq.heappush(heap, (g+1+manhattan(n), g+1, n, path+[state]))
    return None
def print_path(p):
    for s in p:
        for r in s: print(r)
        print()
start = [[1,2,3],[4,0,6],[7,5,8]]
sol = a_star(start)
print("Moves:", len(sol)-1)
print_path(sol)
