import time

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
            win=None,
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()
    
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
        
    def _draw_cell(self, i , j):
        if self._win is None:
            return
        cell_pos_x = self._x1 + (i * self._cell_size_x)
        cell_pos_y = self._y1 + (j * self._cell_size_y)
        self._cells[i][j].draw(cell_pos_x, cell_pos_y, (cell_pos_x + self._cell_size_x), (cell_pos_y + self._cell_size_y))
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
