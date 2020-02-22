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
    bound = 0  # Max depth
    natural_failure = False
    while not natural_failure:
        frontier.put(root)
        while True:
            if frontier.empty():
                break

            curNode = frontier.get()

            if isGoal(curNode.STATE, goal):
                return curNode.PATH, curNode
            children = curNode.CHILDREN(spawnList, bound, gridSize)
            if len(curNode.PATH) < bound:
                if not children:
                    natural_failure=True
                else:
                    for child in children:
                        natural_failure = False
                        frontier.put(child)
        bound += 1
