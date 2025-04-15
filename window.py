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
    
    def close(self):
        self.__isrunning = False

        