
import heapq

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )
            result.append(new_state)

    return result

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def astar(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))
    visited = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == goal:
            print("Goal Reached!")
            for row in state:
                print(row)
            return

        visited.add(to_tuple(state))

        for next_state in neighbors(state):
            if to_tuple(next_state) not in visited:
                heapq.heappush(
                    pq,
                    (
                        g + 1 + heuristic(next_state),
                        g + 1,
                        next_state
                    )
                )

start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

astar(start)
