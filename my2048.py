#part is copy from google project ;
# 0 left counterclockwise
import random,copy
N = 4 ;
class Board:
    def __init__(self):
        self.board = [[0] * N for i in range(N)] ;
        self.score = 0 ;
        self.over = False ;
        self.randomTile()
        self.randomTile()

    def rotateLeft(self, grid):
        out = self.emptyGrid()
        for c in range(4):
            for r in range(4):
                out[r][3-c] = grid[c][r] ;
        return out

    def rotateRight(self, grid):
        out = self.emptyGrid()
        for c in range(4):
            for r in range(4):
                out[3-r][c] = grid[c][r] ;
        return out

    def emptyGrid(self):
        out = list()
        for x in range(4):
            col = list()
            for y in range(4):
                col.append(0)
            out.append(col)
        return out

    def get_empty_cells(self):
        out = list() ;
        for i in range(N):
            for j in range(N):
                if self.board[i][j] == 0:
                    out.append((i,j)) ;
        return out ;

    def randomTile(self):
        cells = self.get_empty_cells()
        if not cells: return False
        #print 'cells', cells

        if random.random() < 0.9: v = 1 ;
        else: v = 2 ;

        cid = random.choice(cells)
        #print cid
        self.board[cid[0]][cid[1]] = v
        return True

    def show(self):
        for i in self.board:
            print(i) ;
        print(self.score) ;

    def gameover(self):
        if self.over : return True ;
        over = True ;
        for row in range(4):
            for column in range (4):
                if self.board[row][column] == 0 :
                    over = False ;
        #if not over : return False ;
        for row in range(4):
            for column in range(3):
                if self.board[row][column] == self.board[row][column+1] :
                    over = False ;
        for row in range(3):
            for column in range(4):
                if self.board[row][column] == self.board[row+1][column] :
                    over = False ;
        if over : self.over = True ;
        return over 

    def move(self, direction):
        score, grid = self.to_move(self.board, direction)
    
        #self.board = next_board ;
        if grid != self.board: #moved
            self.board = grid ;
            self.randomTile() ;
        else :
            self.over = True ;
            score -= 30 ;
        self.score += score ;
        return score ;
        

    def to_move(self, grid2, direction):
        #out = self.emptyGrid()
        # left is 0
        grid = copy.deepcopy(grid2) ;
        for i in range(direction):
            grid = self.rotateLeft(grid) ;
        score = 0 ;
        for row in range(4):
            for i in range(3,0,-1):
                for j in range(i):
                    if grid[row][j] == 0 :
                        grid[row][j], grid[row][j+1] = grid[row][j+1], grid[row][j] ;
            for column in range(3):
                if grid[row][column] == grid[row][column+1] and grid[row][column] != 0:
                    score += 2**grid[row][column] ;
                    grid[row][column]+=1 ;
                    grid[row][column+1] = 0 ;
            for i in range(3,0,-1):
                for j in range(i):
                    if grid[row][j] == 0 :
                        grid[row][j], grid[row][j+1] = grid[row][j+1], grid[row][j] ;
                        #print("I swap") ;

        for i in range(direction):
            grid = self.rotateRight(grid) ;
        #for row in grid : print(row) ;
        return score, grid ;



if __name__ == "__main__":
    board = Board()
    board.show() ;
    while 1 :
        board.move(int(input())) ;
        board.show() ;
        #print(board.score) ;
        if board.gameover() : break ;
    print("you_die") ;