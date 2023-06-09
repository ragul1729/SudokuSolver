from collections import defaultdict

def getInput():
    for i in range(9):
        row=list(map(str,input().split()))
        sudokuGrid.append(row)
    for i in range(9):
        for j in range(9):
            if sudokuGrid[i][j] !='.':
                sudokuGrid[i][j]=int(sudokuGrid[i][j])

def fillRowDict():
    for i in range(9):
        for j in range(9):
            if sudokuGrid[i][j] != '.':
                rowDict[i].add(sudokuGrid[i][j])
            else:
                emptyCellsRow[i].add(j)

def fillColDict():
    for i in range(9):
        for j in range(9):
            if sudokuGrid[j][i] != '.':
                colDict[i].add(sudokuGrid[j][i])
            else:
                emptyCellsCol[i].add(j)

def getGridMap():
    file1 = open(r"C:\Users\Sys\PycharmProjects\pythonProject\gridMap.txt", "r")
    for line in file1.readlines():
        ind=line.split(' ')
        gridMap[int(ind[0])][int(ind[1])]=int(ind[2][0])

def fillBlocks():
    for i in range(9):
        for j in range(9):
            if sudokuGrid[i][j] != '.':
                blocks[gridMap[i][j]].add(sudokuGrid[i][j])
            else:
                emptyCellsBlock[gridMap[i][j]].append((i,j))


def fillPossibleAns():
    for i in range(9):
        for j in range(9):
            if sudokuGrid[i][j]=='.':
                for k in range(1,10):
                    if k not in rowDict[i] and k not in colDict[j] and k not in blocks[gridMap[i][j]]:
                        possibleAns[i][j].add(k)
                key=str(i)+" "+str(j)
                numPossibleAns[key]=len(possibleAns[i][j])

def findNextCell():
    leastVal=min(numPossibleAns.values())
    for k in numPossibleAns.keys():
        if numPossibleAns[k]==leastVal:
            return k

def modifyDS(n,a,b,modifiedVal):
    for j in emptyCellsRow[a]:
        if n in possibleAns[a][j]:
            modifiedVal[1].append(j)
            possibleAns[a][j].remove(n)
    for i in emptyCellsCol[b]:
        if n in possibleAns[i][b]:
            modifiedVal[2].append(i)
            possibleAns[i][b].remove(n)
    for (i,j) in emptyCellsBlock[gridMap[a][b]]:
        if n in possibleAns[i][j]:
            modifiedVal[3].append((i,j))
            possibleAns[i][j].remove(n)

def undoModifyDS(n,a,b,modifiedVal):
    for j in modifiedVal[1]:
        possibleAns[a][j].add(n)
    for i in modifiedVal[2]:
        possibleAns[i][b].add(n)
    for (i,j) in modifiedVal[3]:
        possibleAns[i][j].add(n)
    """
    for j in emptyCellsRow[a]:
        possibleAns[a][j].add(n)
    for i in emptyCellsCol[b]:
        possibleAns[i][b].add(n)
    for (i,j) in emptyCellsBlock[gridMap[a][b]]:
        possibleAns[i][j].add(n)
    """

def printSolvedGrid():
    for row in solvedGrid:
        for ele in row:
            print(ele,end=' ')
        print('')

def solvePuzzle():
    global solvedGrid
    if len(numPossibleAns)==0:
        return True
    res=False
    lowestPossCell = findNextCell()
    val = numPossibleAns[lowestPossCell]
    numPossibleAns.pop(lowestPossCell)
    a, b = map(int, lowestPossCell.split())
    emptyCellsRow[a].remove(b)
    emptyCellsCol[b].remove(a)
    emptyCellsBlock[gridMap[a][b]].remove((a,b))
    for n in possibleAns[a][b]:
        sudokuGrid[a][b]=n
        #rowDict[a].add(n)
        #colDict[b].add(n)
        #blocks[gridMap[a][b]].add(n)
        modifiedVal=defaultdict(list)
        modifyDS(n,a,b,modifiedVal)
        res=res|solvePuzzle()
        if res:
            break
        undoModifyDS(n,a,b,modifiedVal)
    if res:
        solvedGrid = sudokuGrid
        return True
    sudokuGrid[a][b]='.'
    numPossibleAns[lowestPossCell]=val
    emptyCellsRow[a].add(b)
    emptyCellsCol[b].add(a)
    emptyCellsBlock[gridMap[a][b]].append((a,b))
    return False



sudokuGrid=None
solvedGrid=None
rowDict=[set() for i in range(9)]
colDict=[set() for i in range(9)]
gridMap=[[0 for j in range(9)] for i in range(9)]
blocks=[set() for i in range(9)]
possibleAns=[[set() for j in range(9)] for i in range(9)]
emptyCellsRow=defaultdict(set)
emptyCellsCol=defaultdict(set)
emptyCellsBlock=defaultdict(list)
numPossibleAns=dict()
getInput()
fillRowDict()
fillColDict()
getGridMap()
fillBlocks()
fillPossibleAns()

print(rowDict)
print(colDict)
print(possibleAns)
print(numPossibleAns)

solvePuzzle()
printSolvedGrid()



"""
. . . 7 . 3 1 . .
. 5 . 4 9 . 8 3 .
. 9 . . 1 8 7 4 5
1 3 . . 4 9 . . .
9 . . 8 . . 6 . 3
2 . 6 . . 1 9 8 .
5 . 4 9 6 2 3 . .
. . . . 8 . . 2 .
. 2 . . . 4 5 . .
"""

"""
. . . . 7 8 . . .
1 8 . . 2 . . . .
. . 4 . 6 1 8 . 9
. . . . . 2 7 5 .
7 . . . . . 4 . .
2 . . 7 . 5 6 . 3
5 . 1 . . 4 . 7 .
. . . . 1 . 9 . .
. 4 9 . . . . 3 8
"""

"""
. 4 . . . 5 1 2 .
. . . . 1 . . . 6
. . 2 . . . . . 8
. . . . . . 6 . .
9 . . . . 8 . . .
. . 3 . 9 . 4 1 .
. 5 . 7 . . . . .
. . . . . . . . 2
. . 4 . 8 . 9 3 .
"""