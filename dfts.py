import queue
from node import Node


# Function to check if the goal state has been achieved.
def isGoal(state, goal):
    win = goal
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


def ID_DFTS(state, goal, spawnList):
    frontier = queue.LifoQueue()

    root = Node(state, '', 0)
    L = 0  # Max depth

    while True:
        frontier.put(root)
        while True:
            if frontier.empty():
                break

            curNode = frontier.get()
            if isGoal(curNode.STATE, goal):
                return curNode.PATH, curNode

            for child in curNode.CHILDREN(spawnList, L):
                frontier.put(child)

        L += 1
