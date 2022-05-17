# Graph 1
import numpy as np
graph1data = open("Graph1.txt", "r")
graph = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
}
added = []
for line in graph1data:
    key, *value = line.split()
    if key not in added:
        added.append(key)
    neighbour = value[0]
    cost = value[1]
    valueList = [neighbour, cost]
    graph[key].append(valueList)

print('The graph no. 1 is: ')
print(graph)

"""
graph1 = {'A': [['B', 3], ['H', 4]],
'B': [['A', 3], ['C', 4], ['H', 5]],
'H': [['A', 4], ['B', 5], ['G', 2]],
'C': [['B', 4], ['D', 8], ['G', 3]],
'D': [['C', 8], ['E', 2], ['F', 3], ['G', 8]],
'G': [['C', 3], ['D', 8], ['F', 4], ['H', 2]],
'E': [['D', 2]],
'F': [['D', 3], ['G', 4]]
}



graph2 = {'A':  [['B', 2], ['C', 3]],
'B':  [['A', 2], ['D', 2], ['E', 4]],
'C':  [['A', 3], ['E', 2], ['F', 1]],
'D':  [['B', 2], ['G', 3], ['H', 4]],
'E':  [['B', 4], ['C', 2], ['I', 3]],
'F':  [['C', 1], ['I', 5], ['J', 2]],
'G':  [['D', 3]],
'H':  [['D', 4], ['K', 1], ['L', 2]],
'I':  [['E', 3], ['F', 5], ['M', 2], ['N', 2]],
'J':  [['F', 2]],
'K':  [['H', 1]],
'L':  [['H', 2]],
'M':  [['I', 2]],
'N':  [['I', 2]]}

graph3 = {'A': [['B', 8], ['D', 2], ['C', 7]], 'B': [['A', 8], ['D', 1]], 'D': [['B', 1], ['A', 2]], 'C': [['A', 7]]} 

"""


# To calculate path with the cost
def calPathCost(path):
    pathCost = []
    i = 0
    for element in path:
        if i != 0:
            pathCost.append([element[0], pathCost[i - 1][1] + int(path[i][1])])
        else:
            pathCost.append([element[0], 0])
        i += 1

    print(pathCost)

# To display graph in adjacenct matrix


def matrixOnes(graph, count):
    i = 0
    matrix = np.zeros(count*count).reshape(count, count)

    for key, value in graph.items():
        i = ord(key) - 65
        for element in value:
            matrix[i][ord(element[0])-65] = 1
    return matrix

# To display graph in adjacenct matrix with Cost


def matrixCost(graph, count):
    i = 0
    matrix = np.zeros(count*count).reshape(count, count)

    for key, value in graph.items():
        i = ord(key) - 65
        for element in value:
            matrix[i][ord(element[0])-65] = element[1]
    return matrix


queue = []
visited = []
path = []
visit = []


def bfs(start, goal, graph):
    queue.append([start, [start, 0]])  # Add Arad to queue
    # This list has visited nodes with their parent for path tracing
    visited.append([start, start])
    visit.append(start)  # This list contains visited nodes, solely

    # Until goal is found
    while queue and queue[-1] != goal:
        v = queue.pop(0)  # Pop node when all neighbours accessed
        v = v[0]
        # list of neighbours of first element of queue
        if v in graph.keys():
            for neighbour in graph[v]:
                # if the neighbour is not visited then append it to the three lists mentioned below
                # if neighbour[0]
                if neighbour not in visit:
                    queue.append(neighbour)
                    visit.append(neighbour)
                    visited.append([v, neighbour])  # for path tracing

    # Tracing path from goal to the start state
    path = []
    # if the goal exists in the 'visited' list as a child then start appending the route to path
    """
    Note: 'visited' is a multi-dimensional list.
    'element' contains a list from 'visited'
    Slicing that list would give us parent at 0th position (element[0]) & node at 1st pos (element[1])
    """
    for item in visited:
        if item[1][0] == goal:
            node = goal
            for element in reversed(visited):
                if element[1][0] == node:
                    path.append(element[1])
                    node = element[0]
            break
    path.reverse()
    # print(path)

    # matrixOnes
    print(matrixOnes(graph, len(graph.keys())))

    # matrixCost
    print(matrixCost(graph, len(graph.keys())))

    # Calculating Cost
    calPathCost(path)


stack = []
visited = []
path = []
"""
DFS:
stack[]
visited[] would be the path

start in stack[]
start in visited[]

keep doing below until goal found
pick neighbour of last element of stack as key from the dictionary,
if the neighbour is not visited then add to the visited list

print goal
"""


def dfs(start, goal, graph):

    stack.append(start)
    visited.append(start)
    path.append(start)
    found = False

    while stack[-1][0] != goal:
        # list of neighbours of last element of stack
        found = False
        for neighbour in graph[stack[-1]]:
            # looping over neighbours

            # for neighbour in neighbourList:

            # for element in visited:
                if neighbour[0] not in visited:
                    found = True
                    stack.append(neighbour[0])
                    visited.append(neighbour[0])
                    path.append(neighbour)
                    break
            # if all neighbours are visited then pop
        if not found:
            stack.pop(-1)
            path.pop(-1)

    # matrixOnes
    print(matrixOnes(graph, len(graph.keys())))
    # matrixCost
    print(matrixCost(graph, len(graph.keys())))
    # Path Cost
    calPathCost(path)


#dfs("A", "M", graph)

dfs("A", "E", graph)
