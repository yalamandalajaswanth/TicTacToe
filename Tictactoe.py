import random
class TicTacToe:
    def printGrid(self):
        for row in self.grid:
            for col in row:
                print('| '.join(col),end=' ')
            print("\n--------")
    def isAvailable(self,position):
        for row in self.grid:
            for col in row:
                if position == 1 and col == 'j':
                    return True
                position-=1
        return False
    def availablePositions(self):
        position = 1
        res = []
        for row in self.grid:
            for col in row:
                if col == 'j':
                    res.append(position)
                position+=1
        return res
    def changeGrid(self,position,letter):
        if self.isAvailable(position):
            for row in range(3):
                for col in range(3):
                    if position ==1:
                        self.grid[row][col] = letter
                        return
                    position -= 1
    def gameOver(self):
        #if rows same:
        for row in self.grid:
            if len(set(row)) == 1 and 'j' not in set(row):
                return True
        cols = [['j' for _ in range(3)] for _ in range(3)]
        #if cols same
        for row in range(3):
            for col in range(3):
                 cols[col][row] = self.grid[row][col]
        for row in cols:
            if len(set(row)) == 1 and 'j' not in set(row):
                return True
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2]!='j') or (self.grid[0][2] == self.grid[1][1] == self.grid[2][0]!='j'):
            return True
        return False
    def draw(self):
        if self.gameOver():
            return False
        else:
            for row in self.grid:
                for col in row:
                    if col != 'X' or 'O':
                        return False
        return True
    def __init__(self,turn = True,XorO = True):
        first = input('who wanna play first? say p1 or p2:')
        self.turn = 'p1' if first.lower() =='p1'else 'p2'  #U-p1, B-p2
        #self.userXorO = 'X' if input('type X to play as X and O to play as O').upper()=='X' else 'O'
        #self.botXorO = 'O' if self.userXorO == 'X' else 'x'
        #game begins:
        if self.turn=='p1':
            self.userXorO='X' if input('player1,type X to play as X and O to play as O').upper()=='X' else 'O'
            self.botXorO = 'O' if self.userXorO == 'X' else 'X'
        if self.turn=='p2':
            self.botXorO = 'X' if input('player2, type X to play as X and O to play as O').upper()=='X' else 'O'
            self.userXorO='O' if self.userXorO == 'X' else 'X'
        self.grid = [['j' for i in range(3)] for j in range(3)]
        self.printGrid()
        while(True):
            if self.turn == 'p1':
                position = int(input('Player 1 enter an available position from 1-9'))
                while not self.isAvailable(position) or position<1 or position>9:
                    print("available positions - ", self.availablePositions())
                    position = int(input('position invalid, enter a valid position:'))
                print(position)
                self.changeGrid(position,self.userXorO)
                self.printGrid()
                self.turn = 'p2'
                if self.gameOver():
                    print("Player 1 won!!!")
                    break
            else:
                position = int(input('Player 2 enter an available position from 1-9'))
                while not self.isAvailable(position) or position<1 or position>9:
                    print("available positions - ", self.availablePositions())
                    position = int(input('position invalid, enter a valid position:'))
                print(position)
                self.changeGrid(position,self.botXorO)
                self.printGrid()
                self.turn = 'p1'
                if self.gameOver():
                    print("Player 2 won")
                    break   
t=TicTacToe()