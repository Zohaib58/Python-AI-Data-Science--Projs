# Queue: [Odarea, Farara, Reminu Viliea, Lugoj]
# Visited: [Arad, Zerind, Sibiu, Timi]


graph = {'Odarea': ['Zerind', 'Sibiu'], 
'Zerind': ['Odarea', 'Sibiu', 'Arad'], 
'Arad': ['Zerind', 'Sibiu', 'Timisoara'], 
'Sibiu': ['Odarea', 'Arad', 'Farara', 'Rimnieu Vilea'], 
'Timisoara': ['Arad', 'Lugoj'], 
'Lugoj': ['Timisoara', 'Mehadia'], 
'Mehadia': ['Lugoj', 'Dobreta'], 
'Rimnieu Vilea': ['Sibiu', 'Pitesti', 'Craiova'], 
'Craiova': ['Rimnieu Vilea', 'Pitesti', 'Dobreta'], 
'Pitesti': ['Rimnieu Vilea', 'Craiova', 'Bucharest'], 
'Farara': ['Sibiu', 'Bucharest'], 
'Bucharest': ['Farara', 'Pitesti', 'Giurgui', 'Urzieeni'], 
'Urzieeni': ['Bucharest', 'Hirsova'], 
'Neamt': ['Iasi'], 
'Iasi': ['Neamt', 'Vaslui'], 
'Vaslui': ['Iasi', 'Hirsova'], 
'Hirsova': ['Vaslui', 'Eforie'], 
'Eforie': ['Hirsova'], 'Dobreta': ['Mehadia', 'Craiova'],
'Giurgui' : ['Bucharest']}

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

#ids("Arad", "Bucharest", graph, 10)
ids("Arad", "Bucharest", graph, 10)




