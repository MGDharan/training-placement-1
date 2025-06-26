import heapq

def a_star(start, goal, h, neighbors):
    open_set = [(0 + h(start), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in neighbors(current):
            temp_g = cost + 1
            if temp_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f = temp_g + h(neighbor)
                heapq.heappush(open_set, (f, temp_g, neighbor))
