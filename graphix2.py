from graphics import *

def main():
    win = GraphWin('Shapes')
    win = GraphWin('Jon')
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)
    label = Text(center, "Red Circle")
    label.draw(win)

    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)

    



    win.getMouse()

main()