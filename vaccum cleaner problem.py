def vacuum_world(loc, state_A, state_B):
    actions = []
    if loc == 'A':
        if state_A == 'Dirty':
            actions.append("Suck")
            state_A = 'Clean'
        actions.append("Move Right")
        if state_B == 'Dirty':
            actions.append("Suck")
            state_B = 'Clean'
    else:
        if state_B == 'Dirty':
            actions.append("Suck")
            state_B = 'Clean'
        actions.append("Move Left")
        if state_A == 'Dirty':
            actions.append("Suck")
            state_A = 'Clean'
    return actions, state_A, state_B
actions, final_A, final_B = vacuum_world('A', 'Dirty', 'Dirty')
print("Actions:", actions)
print("Final State: A =", final_A, ", B =", final_B)
