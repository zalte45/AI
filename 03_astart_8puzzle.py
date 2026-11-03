import heapq

def h(s, goal):
    return sum(abs(i // 3 - goal.index(x) // 3) +
               abs(i % 3 - goal.index(x) % 3)
               for i, x in enumerate(s) if x != 0)


def astar(start, goal):
    q = [(h(start, goal), 0, start, [])]
    visited = set()

    while q:
        f, g, s, path = heapq.heappop(q)

        if s == goal:
            return path + [s]

        if s not in visited:
            visited.add(s)
            i = s.index(0)

            for j in [i - 3, i + 3, i - 1, i + 1]:
                if 0 <= j < 9 and (i // 3 == j // 3 or i % 3 == j % 3):
                    n = list(s)
                    n[i], n[j] = n[j], n[i]
                    n = tuple(n)

                    heapq.heappush(q, (g + 1 + h(n, goal), g + 1, n, path + [s]))

    return None


# Initial and final states
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = astar(start, goal)

# Print solution
if result:
    print("Solution Found")
    print("Number of Moves:", len(result) - 1)

    for step, s in enumerate(result):
        print(f"\nStep: {step}")
        print(s[:3])
        print(s[3:6])
        print(s[6:])

else:
    print("No solution")
