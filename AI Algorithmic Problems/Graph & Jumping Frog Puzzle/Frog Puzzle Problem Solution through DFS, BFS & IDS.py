def states(s):

    arr = []
    for i in range(2, 7):
        if (s[i] == 'A' and s[i + 1] == '_'):
            new_state = s
            new_state = new_state[:i + 1] + 'A' + new_state[i + 2:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
        if (s[i] == 'A' and s[i + 2] == '_'):
            new_state = s
            new_state = new_state[:i + 2] + 'A' + new_state[i + 3:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
        if (s[i] == 'B' and s[i + 1] == '_'):
            new_state = s
            new_state = new_state[:i + 1] + 'B' + new_state[i + 2:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
        if (s[i] == 'B' and s[i + 2] == '_'):
            new_state = s
            new_state = new_state[:i + 2] + 'B' + new_state[i + 3:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])

    for i in range(6, 1, -1):
        if (s[i] == 'X' and s[i - 1] == '_'):
            new_state = s
            new_state = new_state[:i - 1] + 'X' + new_state[i:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
        if (s[i] == 'X' and s[i - 2] == '_'):
            new_state = s
            new_state = new_state[:i - 2] + 'X' + new_state[i - 1:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
        if (s[i] == 'Y' and s[i - 1] == '_'):
            new_state = s
            new_state = new_state[:i - 1] + 'Y' + new_state[i:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
        if (s[i] == 'Y' and s[i - 2] == '_'):
            new_state = s
            new_state = new_state[:i - 2] + 'Y' + new_state[i - 1:]
            new_state = new_state[:i] + '_' + new_state[i + 1:]
            arr.append(new_state[2:-2])
    return arr

## This above part is from the example code of TA

queue = []
graph = {

}

queue.append("AB_XY")

while (len(queue) > 0):
    node = queue.pop(0)
    array = states("**" + node + "**")
    for state in array:
        queue.append(state)
    d = {node: array}
    graph.update(d)
c = 0
"""
print('Following is generated graph')
for key, value in graph.items():
    rint(key, ':', value)

print()
"""
queue = []
visited = []
path = []
visit= []
def bfs(start, goal, graph):
    queue.append(start) # Add Arad to queue
    visited.append([start, start]) # This list has visited nodes with their parent for path tracing
    visit.append(start)  # This list contains visited nodes, solely
    
    # Until goal is found
    while queue and queue[-1] != goal:
        v = queue.pop(0) # Pop node when all neighbours accessed
        
        # list of neighbours of first element of queue
        for neighbour in graph[v]:
            # if the neighbour is not visited then append it to the three lists mentioned below
            if neighbour not in visit:
                queue.append(neighbour)
                visit.append(neighbour)
                visited.append([v, neighbour]) # for path tracing

    # Tracing path from goal to the start state
    path = []
    # if the goal exists in the 'visited' list as a child then start appending the route to path
    """
    Note: 'visited' is a multi-dimensional list.
    'element' contains a list from 'visited'
    Slicing that list would give us parent at 0th position (element[0]) & node at 1st pos (element[1])
    """
    for item in visited:
        if item[1] == goal:
            node = goal
            for element in reversed(visited):
                if element[1] == node:
                    path.append(element[1])
                    node = element[0]
            break
    path.reverse()
    print(path)





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

    while (stack[-1] != goal):
        # list of neighbours of last element of stack
        found = False
        for neighbour in graph[stack[-1]]:
            # looping over neighbours
            
            #for neighbour in neighbourList:
            
            if neighbour not in visited:
                found = True
                stack.append(neighbour)
                visited.append(neighbour)
                path.append(neighbour)
                break
            # if all neighbours are visited then pop
        if not found:
            stack.pop(-1)
            path.pop(-1)
    print(path)

def ids(start, goal, places, limit):
    stack = []
    visited = []
    path = []
    stack.append(start)
    visited.append(start)
    path.append(start)
    found = True
    limit2 = 0

    while (stack[-1] is not goal or stack) and (limit2 < limit):
        for node in places[stack[-1]]:
            found = False

            if node not in visited:
                limit2 = limit2 + 1
                found = True
                stack.append(node)
                visited.append(node)
                path.append(node)
                break

        if not found:
            stack.pop(-1)
            path.pop(-1)

    if (path.pop(-1) == goal) and (limit > limit2):
        path.append(goal)
        print(path)

    else:
        print("Increase your limit")

dfs('AB_XY', 'XY_AB', graph)

bfs('AB_XY', 'XY_AB', graph)

