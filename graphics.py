from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg= "White", width = width, height = height)
        self.__canvas.pack(fill = BOTH, expand = True)
        self.__isrunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__isrunning = True
        while self.__isrunning:
            self.redraw()
        print("Window closed")
    
    def close(self):
        self.__isrunning = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
        print(f"Drawing line from ({line.p1.x}, {line.p1.y}) to ({line.p2.x}, {line.p2.y}) with color {fill_color}")

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        

class Cell():
    def __init__(self, win=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.left_wall == True:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.top_wall == True:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.right_wall == True:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.bottom_wall == True:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        mid_x = (self._x1 + self._x2 ) / 2
        mid_y = (self._y1 + self._y2 ) / 2
        line_from = Point(mid_x, mid_y)
       
        other_mid_x = (to_cell._x1 + to_cell._x2) / 2
        other_mid_y = (to_cell._y1 + to_cell._y2) / 2
        line_to = Point(other_mid_x, other_mid_y)
        
        self._win.draw_line(Line(line_from, line_to), fill_color)