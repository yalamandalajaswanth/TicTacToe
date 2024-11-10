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
        first = input('wanna play first? say Y or N:')
        self.turn = 'U' if first =='Y' else 'B' #U for user B for bot
        self.userXorO = 'X' if input('type X to play as X and O to play as O')=='X' else 'O'
        self.botXorO = 'X' if self.userXorO == 'O' else 'O'
        #game begins:
        self.grid = [['j' for i in range(3)] for j in range(3)]
        self.printGrid()
        while(True):
            if self.turn == 'U':
                position = int(input('enter an available position from 1-9'))
                while not self.isAvailable(position) or position<1 or position>9:
                    print("available positions - ", self.availablePositions())
                    position = int(input('position invalid, enter a valid position:'))
                print(position)
                self.changeGrid(position,self.userXorO)
                self.printGrid()
                self.turn = 'B'
                if self.gameOver():
                    print("YOU WON!!!")
                    break
            else:
                print("Bot playing")
                available = self.availablePositions()
                position = random.choice(available)
                self.changeGrid(position,self.botXorO)
                self.printGrid()
                self.turn = 'U'
                if self.gameOver():
                    print("YOU LOST:(")
                    break
            if self.draw():
                print("it's a draw")
                break
t=TicTacToe()