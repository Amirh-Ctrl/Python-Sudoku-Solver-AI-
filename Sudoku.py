class Table:
    def __init__(self,InitState):
        self.Domain = range(1,10)
        self.Content = InitState
        self.CSP = self.CreateCSP()
    
    def CheckRow(self,i,Domain):
        RowContainer = []
        for j in range(9):
            if self.Content[i][j] != 0:
                RowContainer.append(self.Content[i][j])
        Remains = list(set(Domain)-set(RowContainer))
        return Remains

    def CheckCol(self,j,Domain):
        ColContainer = []
        for i in range(9):
            if self.Content[i][j] != 0:
                ColContainer.append(self.Content[i][j])
        Remains = list(set(Domain)-set(ColContainer))
        return Remains

    def CheckBlock(self,i,j,Domain):
        BlockContainer = []
        i = i // 3
        j = j // 3
        for k in range(3*i,3*i+3):
            for l in range(3*j,3*j+3):
                if self.Content[k][l] != 0:
                    BlockContainer.append(self.Content[k][l])
        Remains = list(set(Domain)-set(BlockContainer))
        return Remains
    
    def CreateCSP(self):
        CSP = []
        for i in range(9):
            CSP.append([])
            for j in range(9):
                CSP[i].append([])
        for i in range(9):
            for j in range(9):
                if self.Content[i][j] == 0:
                    ThisDomain = self.Domain
                    ThisDomain = self.CheckBlock(i,j,ThisDomain)
                    ThisDomain = self.CheckCol(j,ThisDomain)
                    ThisDomain = self.CheckRow(i,ThisDomain)
                    CSP[i][j] = ThisDomain
        return CSP
    
    def MRVFind(self,CSP):
        min = 10
        self.mini = 10
        self.minj = 10
        for i in range(9):
            for j in range(9):
                if self.Content[i][j] == 0 and len(CSP[i][j]) == 0:
                    return -1
                elif (self.Content[i][j] == 0 and len(CSP[i][j]) < min):
                    self.mini = i
                    self.minj = j
                    min = len(CSP[i][j])

    def LCVFind(self):
        max = 0
        maxi = 10
        b = 0
        Possibs = self.CSP[self.mini][self.minj]
        Sorted = []
        while (len(Possibs) > 0):
            for i in Possibs:
                self.Content[self.mini][self.minj] = i
                CSPtemp = self.CreateCSP()
                total = self.sumCSP(CSPtemp)
                if total > max:
                    Sorted.append(i)
                    b = i
            Possibs.remove(b)
            self.Content[self.mini][self.minj] = 0
        return Sorted

    def sumCSP(self,CSP):
        total = 0
        for i in range(9):
            for j in range(9):
                total += len(CSP[i][j])
        return total
    
    def isSolveable(self):
         if self.MRVFind(self.CreateCSP()) == -1 :
            return False
         else:
             return True

    def isSolved(self):
        sum = 0
        for i in range(9):
            for j in range(9):
                if self.Content[i][j] == 0:
                    return False
        return True

    def Solve(self):
        if (self.isSolved()):
            return True
        self.CSP = self.CreateCSP()
        if (not self.isSolveable()):
            return False
        localmini = self.mini
        localminj = self.minj
        Poss = self.CSP[localmini][localminj]
        
        
        for i in Poss:
            self.Content[localmini][localminj] = i

            if self.Solve():
                return True
            
            self.Content[localmini][localminj] = 0
        return False
        
        
                  
    

        
def print_board(board):
    for i in range(9):
        for j in range(9):
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


try:
    sudoku_puzzle = []
    for i in range(9):
        input_line = input() 
        row = [int(num) for num in input_line.split(' ')]
        sudoku_puzzle.append(row)
    
    my_sudoku = Table(sudoku_puzzle)

    if my_sudoku.Solve():
        print_board(my_sudoku.Content)
    else:
        print("This Sudoku puzzle has no solution.")

except ValueError as e:
    print(f"Invalid input: {e}")
except NameError:
    print("Error: 'Table' class or 'print_board' function is not defined.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
