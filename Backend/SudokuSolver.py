from collections import defaultdict

class Sudokusolver:

    def getInput(self):
        """
        for i in range(9):
            row=list(map(str,input().split()))
            sudokuGrid.append(row)
        """
        for i in range(9):
            for j in range(9):
                if self.sudokuGrid[i][j] !=".":
                    self.sudokuGrid[i][j]=int(self.sudokuGrid[i][j])

    def fillRowDict(self):
        for i in range(9):
            for j in range(9):
                if self.sudokuGrid[i][j] != '.':
                    self.rowDict[i].add(self.sudokuGrid[i][j])
                else:
                    self.emptyCellsRow[i].add(j)

    def fillColDict(self):
        for i in range(9):
            for j in range(9):
                if self.sudokuGrid[j][i] != '.':
                    self.colDict[i].add(self.sudokuGrid[j][i])
                else:
                    self.emptyCellsCol[i].add(j)

    def getGridMap(self):
        file1 = open(r"C:\Users\Sys\PycharmProjects\pythonProject\gridMap.txt", "r")
        for line in file1.readlines():
            ind=line.split(' ')
            self.gridMap[int(ind[0])][int(ind[1])]=int(ind[2][0])

    def fillBlocks(self):
        for i in range(9):
            for j in range(9):
                if self.sudokuGrid[i][j] != '.':
                    self.blocks[self.gridMap[i][j]].add(self.sudokuGrid[i][j])
                else:
                    self.emptyCellsBlock[self.gridMap[i][j]].append((i,j))


    def fillPossibleAns(self):
        for i in range(9):
            for j in range(9):
                if self.sudokuGrid[i][j]=='.':
                    for k in range(1,10):
                        if k not in self.rowDict[i] and k not in self.colDict[j] and k not in self.blocks[self.gridMap[i][j]]:
                            self.possibleAns[i][j].add(k)
                    key=str(i)+" "+str(j)
                    self.numPossibleAns[key]=len(self.possibleAns[i][j])

    def findNextCell(self):
        leastVal=min(self.numPossibleAns.values())
        for k in self.numPossibleAns.keys():
            if self.numPossibleAns[k]==leastVal:
                return k

    def modifyDS(self,n,a,b,modifiedVal):
        for j in self.emptyCellsRow[a]:
            if n in self.possibleAns[a][j]:
                modifiedVal[1].append(j)
                self.possibleAns[a][j].remove(n)
        for i in self.emptyCellsCol[b]:
            if n in self.possibleAns[i][b]:
                modifiedVal[2].append(i)
                self.possibleAns[i][b].remove(n)
        for (i,j) in self.emptyCellsBlock[self.gridMap[a][b]]:
            if n in self.possibleAns[i][j]:
                modifiedVal[3].append((i,j))
                self.possibleAns[i][j].remove(n)

    def undoModifyDS(self,n,a,b,modifiedVal):
        for j in modifiedVal[1]:
            self.possibleAns[a][j].add(n)
        for i in modifiedVal[2]:
            self.possibleAns[i][b].add(n)
        for (i,j) in modifiedVal[3]:
            self.possibleAns[i][j].add(n)
        """
        for j in emptyCellsRow[a]:
            possibleAns[a][j].add(n)
        for i in emptyCellsCol[b]:
            possibleAns[i][b].add(n)
        for (i,j) in emptyCellsBlock[gridMap[a][b]]:
            possibleAns[i][j].add(n)
        """

    def printSolvedGrid(self):
        #print("Inside solvedgrid")
        for row in self.solvedGrid:
            for ele in row:
                print(ele,end=' ')
            print('')

    def solvePuzzle(self):
        #global solvedGrid
        #print("Inside solvedgrid")
        if len(self.numPossibleAns)==0:
            return True
        res=False
        lowestPossCell = self.findNextCell()
        val = self.numPossibleAns[lowestPossCell]
        self.numPossibleAns.pop(lowestPossCell)
        a, b = map(int, lowestPossCell.split())
        self.emptyCellsRow[a].remove(b)
        self.emptyCellsCol[b].remove(a)
        self.emptyCellsBlock[self.gridMap[a][b]].remove((a,b))
        for n in self.possibleAns[a][b]:
            self.sudokuGrid[a][b]=n
            #rowDict[a].add(n)
            #colDict[b].add(n)
            #blocks[gridMap[a][b]].add(n)
            modifiedVal=defaultdict(list)
            self.modifyDS(n,a,b,modifiedVal)
            res=res|self.solvePuzzle()
            if res:
                break
            self.undoModifyDS(n,a,b,modifiedVal)
        if res:
            self.solvedGrid = self.sudokuGrid
            return True
        self.sudokuGrid[a][b]='.'
        self.numPossibleAns[lowestPossCell]=val
        self.emptyCellsRow[a].add(b)
        self.emptyCellsCol[b].add(a)
        self.emptyCellsBlock[self.gridMap[a][b]].append((a,b))
        return False

    def __init__(self,grid):
        self.sudokuGrid = grid
        self.solvedGrid = None
        self.rowDict = [set() for i in range(9)]
        self.colDict = [set() for i in range(9)]
        self.gridMap = [[0 for j in range(9)] for i in range(9)]
        self.blocks = [set() for i in range(9)]
        self.possibleAns = [[set() for j in range(9)] for i in range(9)]
        self.emptyCellsRow = defaultdict(set)
        self.emptyCellsCol = defaultdict(set)
        self.emptyCellsBlock = defaultdict(list)
        self.numPossibleAns = dict()

    def funcOrder(self):
        self.getInput()
        self.fillRowDict()
        self.fillColDict()
        self.getGridMap()
        self.fillBlocks()
        self.fillPossibleAns()
        print(self.rowDict)
        print(self.colDict)
        print(self.possibleAns)
        print(self.numPossibleAns)
        self.solvePuzzle()
        self.printSolvedGrid()









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