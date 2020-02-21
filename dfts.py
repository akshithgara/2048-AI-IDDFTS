import queue
from grid import grid


# Function to check if the goal state has been achieved.
def isGoal(state, goal):
    win = goal
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


def ID_DFTS(state, goal, spawnList, gridSize):
    frontier = queue.LifoQueue()

    root = grid(state, '', 0, spawnList, gridSize)
    L = 0  # Max depth

    while True:
        # print(L)
        frontier.put(root)
        while True:
            if frontier.empty():
                break

            curNode = frontier.get()

            # print(curNode.STATE)
            if isGoal(curNode.STATE, goal):
                return curNode.PATH, curNode

            for child in curNode.CHILDREN(spawnList, L, gridSize):
                frontier.put(child)

        L += 1
