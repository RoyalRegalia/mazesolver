import time
import random

from graphics import *

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None, #None for testing, remove None later
            seed=None 
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if seed:
            random.seed(seed) #leave seed param blank outside testing

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for col in range(self._num_cols):
            column = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        for col in range(self._num_cols):
            for row in range(self._num_rows):    
                self._draw_cell(col, row)
        
    def _draw_cell(self, col , row):
        if self._win is None:
            return
        cell_pos_x = self._x1 + (col * self._cell_size_x)
        cell_pos_y = self._y1 + (row * self._cell_size_y)
        self._cells[col][row].draw(cell_pos_x, cell_pos_y, (cell_pos_x + self._cell_size_x), (cell_pos_y + self._cell_size_y))
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.top_wall = False
        self._draw_cell(0, 0)
        
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            directions = [(1 , 0), (-1 , 0), (0, 1), (0, -1)]

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]):
                    if not self._cells[ni][nj].visited:
                        to_visit.append((ni,nj))

            if not to_visit:
                self._draw_cell(i, j)
                return

            ni, nj = random.choice(to_visit) #random.choice selects from a non-empty sequence

            if ni == i + 1: # 0 index column is top left, move down
                current.bottom_wall = False
                self._cells[ni][j].top_wall = False
            elif ni == i - 1: # move up
                current.top_wall = False
                self._cells[ni][j].bottom_wall = False
            elif nj == j + 1: # 0 index row is top left, move right
                current.right_wall = False
                self._cells[i][nj].left_wall = False
            elif nj == j - 1: #move left
                current.left_wall = False
                self._cells[i][nj].right_wall = False

            self._break_walls_r(ni, nj)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cells in col:
                cells.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j): #self, start, end
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if current == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True
        
        #left
        if (
            i > 0 #if bigger than the array size
            and not current.left_wall #left wall does not exist 
            and not self._cells[i - 1][j].visited #left cell was not visited
        ):
            current.draw_move(self._cells[i - 1][j]) #draw the move line from current to new cell
            if self._solve_r(i - 1, j): #if it is the right move, return True and dont check other directions
                return True
            else:
                current.draw_move(self._cells[i - 1][j], True) #draw undo gray line
        
        #right
        if (
            i < self._num_cols - 1
            and not current.right_wall
            and not self._cells[i + 1][j].visited 
        ):
            current.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                current.draw_move(self._cells[i + 1][j], True)

        #top
        if (
            j > 0
            and not current.top_wall
            and not self._cells[i][j - 1].visited
        ):
            current.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                current.draw_move(self._cells[i][j - 1], True)

        #down
        if (
            j < self._num_rows - 1
            and not current.bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            current.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                current.draw_move(self._cells[i][j + 1], True)

        return False