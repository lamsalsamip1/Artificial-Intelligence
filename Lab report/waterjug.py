def water_jug_problem(capacity1, capacity2, target):
    # initial state (x, y) where x and y are the amounts of water in the two jugs
    state = (0, 0)
    parent = {}
    frontier = [state]
    while frontier:
        state = frontier.pop(0)
        if state == (target, 0) or state == (0, target):
            # goal state reached
            path = [state]
            while state in parent:
                state = parent[state]
                path.append(state)
            path.reverse()
            return path
        x, y = state
        # generate all possible successor states
        states = [(capacity1, y), (x, capacity2), (0, y), (x, 0), (min(x + y, capacity1), max(0, x + y - capacity1)), (max(0, y + x - capacity2), min(y + x, capacity2))]
        for new_state in states:
            if new_state not in parent:
                parent[new_state] = state
                frontier.append(new_state)
    return None

# example
capacity1 = 4
capacity2 = 3
target = 2
path = water_jug_problem(capacity1, capacity2, target)
if path is None:
    print("No solution found.")
else:
    for state in path:
        print(state)