from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    x1, y1 = 50, 50  
    x2, y2 = 100, 100
    cell1 = Cell(win)
    
    cell1.draw(x1, y1, x2, y2)
    

    x1, y1 = 100, 50  
    x2, y2 = 150, 100
    cell2 = Cell(win)
    cell2.draw(x1, y1, x2, y2)
    print("Cell1 center:", (cell1._x1 + cell1._x2) / 2, (cell1._y1 + cell1._y2) / 2)
    print("Cell2 center:", (cell2._x1 + cell2._x2) / 2, (cell2._y1 + cell2._y2) / 2)
    cell1.draw_move(cell2)

    win.wait_for_close()

main()