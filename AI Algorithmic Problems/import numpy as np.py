import numpy as np
"""
def read_file():
    graph1 = []
    graph2 = []
    graph3 = []
    graph_position = []
    file = open("Assignment2_DataFile.txt", "r")
    contents = file.readlines()

    for position, line in enumerate(contents):
        if (line.startswith("s")):
            graph_position.append(position)

    file.close()
    file = open("Assignment2_DataFile.txt", "r")
    contents = file.readlines()
    graph1_boundary = (contents[graph_position[1] + 2][0], contents[graph_position[1] + 2][2])
    for lines in contents[graph_position[0] + 1: graph_position[1]]:
        graph1.append(lines)
    
    graph2_boundary = (contents[graph_position[3] + 2][0], contents[graph_position[3]+ 2][2])
    for lines in contents[graph_position[2] + 1: graph_position[3]]:
        graph2.append(lines)

    graph3_boundary = (contents[graph_position[5] + 2][0], contents[graph_position[5]+ 2][2])
    for lines in contents[graph_position[4] + 1: graph_position[5]]:
        graph3.append(lines)
        file.close()
    print("graph 1")


def generate_dic(graph):
    graph1 = {
    }
    for line in graph:
        for i in range(0,3,2):
            if line[i] in graph1:
                list = graph1[line[i]]
                if i == 0:
                    list.append((line[i+2], line[4]))
                    graph1[line[i]] = list
                else:
                    list.append((line[i -2], line[4]))
                    graph1[line[i]] = list
            else:
                if i == 0:
                    graph1.update({
                    line[i] : [(line[i+2], line[4])]
                    })
                else:
                    graph1.update({
                        line[i] : [(line[i-2],line[4])]
                        })
        print(graph1)


read_file()
"""
f = open('Assignment2_DataFile.txt','r')
w = open('Assignment2_Output.txt', 'w')

Graphname = []
Dimensions = 0

for row in f:
    if row.startswith('//############# '):
        row = row.split(' ')
        Graphname.append(row[1])
        # print(row[1])
        w.write(row[1])
        w.write('Adjacency matrix\n')
        row = next(f)
        row = next(f)
        Dimensions = int(row)
        Matrix = np.zeros((Dimensions, Dimensions))
        ZeroOneMatrix = np.zeros((Dimensions, Dimensions))
        # print(Matrix)
        row = next(f)
        row = next(f)
        # storing all the edges as it is so I can use them later
        EdgesList = []
        while(row.startswith('//') == False):
            row = row.split(' ')
            Vertice = row[0]
            Edge = row[1]
            Cost = int(row[2])
            EdgesList.append([Vertice, Edge, Cost])
            EdgesList.append([Edge, Vertice, Cost])
            row = next(f)
        Graphname.append(EdgesList)
        # extracting a list of all vertices from the list of whole edges
        VerticesList = []
        for x in EdgesList:
            for y in x:
                if y not in VerticesList and isinstance(y, int) == False:
                    VerticesList.append(y)
        # print('Vertices:')
        # print(VerticesList)
        for v in VerticesList:
            w.write(v + ' ')
        w.write('\n\n')
        # making dictionary of vertices as keys
        VerticesWithEdges = {}
        for x in VerticesList:
            NAME = x
            list = []
            VerticesWithEdges[NAME] = list
        # assigning edges to vertices in dictionary
        for v in VerticesWithEdges:
            for e in EdgesList:
                    if e[0] == v:
                        VerticesWithEdges[v].append([e[1], e[2]])
        # print('Vertices With Edges:')
        # print(VerticesWithEdges)
        for V in VerticesWithEdges:
            for E in VerticesWithEdges.get(V):
                #print(v)
                #print(v[0])
                Matrix[ord(V) - 65][ord(E[0]) - 65] = E[1]
                ZeroOneMatrix[ord(V) - 65][ord(E[0]) - 65] = 1
        ZOM = str(ZeroOneMatrix)
        w.write(ZOM + '\nCosts:\n')
        content = str(Matrix)
        w.write(content + '\n')
        row = next(f)
        # finding out start and end vertices
        StartEndVertices = []
        row = row.split()
        Start = row[0]
        End = row[1]
        StartEndVertices.append([row[0], row[1]])
        w.write('Start Vertex:' + row[0] + '\nEnd Vertex:' + row[1] +'\n')
        # print('Start&End:')
        # print(row[0], row[1])
        Graphname.append(StartEndVertices)

        print(VerticesWithEdges)
