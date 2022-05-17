from ast import Num
from multiprocessing.sharedctypes import Value
import random
import numpy as np

# STEP 1 Functions
def RandomQueenPositionList():
    listA = []
    for i in range(8):
        num = random.randint(1,8)
        listA.append(num)

    return listA

# Creating Board for the List that has Queen Position
def board(list):
    board = np.zeros((8,8))
    # array = array.astype(int)
    temp = 0
    
    for x in list:
        # X is minus 1 because values in the list range from 1 to 8 but array starts from 0....
        board[x-1][temp] = 1
        temp = temp+1
    return board

# STEP 2 Function
def fitnessFunction(board, list):
    #flag = True
    fitness_value = 0
    temp = 0
    
    for x in list:
        #p = array[x-1][temp]
        flag = True
        
        # Check For Rows
        for i in range(8):
            if(board[x-1][i])==1:
                if(i != temp):
                    flag = False
                    break
                    
        # Diagonals   
        
        # Positive Diagonal --> Up 
        if(flag == True):
            r = x-1
            c = temp
            while(r >= 0 and c <= 7):
                if(board[r][c])==1:
                    if(r==(x-1) and c==temp):
                        r = r-1
                        c = c+1
                        continue
                    else:
                        flag = False
                        break
                r = r-1
                c = c+1
        
        # Positive Diagonal --> Downward
        if(flag == True):
            r = x-1
            c = temp
            while(c >= 0 and r <= 7):
                if(board[r][c])==1:
                    if(r==(x-1) and c==temp):
                        r = r+1
                        c = c-1
                        continue
                    else:
                        flag = False
                        break
                r = r+1
                c = c-1
        
        # Negative Diagonal --> Downward 
        if(flag == True):
            r = x-1
            c = temp
            while(r <= 7 and c <= 7):
                if(board[r][c])==1:
                    if(r==(x-1) and c==temp):
                        r = r+1
                        c = c+1
                        continue
                    else:
                        flag = False
                        break
                r = r+1
                c = c+1
        
        # Negative Diagonal --> Upward 
        if(flag == True):
            r = x-1
            c = temp
            while(r >= 0 and c >= 0):
                if(board[r][c])==1:
                    if(r==(x-1) and c==temp):
                        r = r-1
                        c = c-1
                        continue
                    else:
                        flag = False
                        break
                r = r-1
                c = c-1
        
            
        if(flag == True):
            fitness_value += 1
        
        temp += 1
    return fitness_value


#STEP 4 Functions
def mutate(list):
    index = random.randint(0, 7)
    value = random.randint(0, 7)
    
    if(list[index] == value):
        mutate(list)

    list[index] = value
    
    return list


def Crossover(listA, listB):
    newListA = listB[:(len(listB)//2)] + listA[(len(listA)//2):]
    newListB = listA[:(len(listA)//2)] + listB[(len(listB)//2):]
    Crossed = []
    Crossed.append(newListA)
    Crossed.append(newListB)
    return Crossed

# Creating 4 parent list    
listA = RandomQueenPositionList()
listB = RandomQueenPositionList()
listC = RandomQueenPositionList()
listD = RandomQueenPositionList()


# Board
boardA = board(listA)
boardB = board(listB)
boardC = board(listC)
boardD = board(listD)

# fitness 
fitA = fitnessFunction(boardA, listA)
fitB = fitnessFunction(boardB, listB)
fitC = fitnessFunction(boardC, listC)
fitD = fitnessFunction(boardD, listD)



list_of_lists = [listA, listB, listC, listD]

list_of_fitness = [fitA, fitB, fitC, fitD]

i = 0

while(i < 20000):
    
    #Choosing 2 best Parents from List of Fitness/Lists
    
    index_of_p1 = np.argmax(list_of_fitness)
    copy = list_of_fitness.copy()
    copy[index_of_p1] = 0
    index_of_p2 = np.argmax(copy)
    
    p1 = list_of_lists[index_of_p1].copy()
    p2 = list_of_lists[index_of_p2].copy()


    # CrossOver 
    newParent = Crossover(p1, p2)
    newParentA = newParent[0]
    newParentB = newParent[1]         
    # Mutation 
    c1 = mutate(newParentA)
    c2 = mutate(newParentB)
    
    
    # Board
    
    b1 = board(c1)
    b2 = board(c2)
    
    
    f1 = fitnessFunction(b1, c1)
    f2 = fitnessFunction(b2, c2)
    
    
    list_of_lists.append(c1)
    list_of_lists.append(c2)
    
    list_of_fitness.append(f1)
    list_of_fitness.append(f2)

    index_of_r1 = np.argmin(list_of_fitness)
    popr1 = list_of_lists.pop(index_of_r1)
    popindr1 = list_of_fitness.pop(index_of_r1)
    
    
    index_of_r2 = np.argmin(list_of_fitness)
    popr2 = list_of_lists.pop(index_of_r2)
    popindr2 = list_of_fitness.pop(index_of_r2)

    i += 1


    if (max(list_of_fitness) == 8):
        break



solution_index = np.argmax(list_of_fitness)


list_of_lists[solution_index]

newboard = board(list_of_lists[solution_index])


print(fitnessFunction(newboard, list_of_lists[solution_index]))
print(newboard)
    
