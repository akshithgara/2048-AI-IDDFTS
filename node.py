# Akshith Ga ra
# 2048 AI
# CS5400

from grid import grid


class Node:
    def __init__(self, state, path, spawn):
        self.STATE = state  # The given 2048 initial state.
        self.PATH = path
        self.SPAWN = spawn  # Stores the current spawn value from the given list.

    def CHILDREN(self, sl, depth):  # Function to try out all the moves and add it to the childList.
        if len(self.PATH) >= depth:
            return []

        childList = []
        for direction in ['Up', 'Down', 'Left', 'Right']:
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout, spawn_list=sl)
            if grid.move(curGrid, direction, self.SPAWN):
                # Generate the state for the child
                childState = []
                for line in curGrid.get_current_grid():
                    childState.append(line)
                child = Node(childState, ''.join([self.PATH, direction[0]]), self.SPAWN + 1)
                childList.append(child)

        return childList
