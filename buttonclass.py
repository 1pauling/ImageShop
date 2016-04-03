#buttonclass.py

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""
    

    def __init__(self, win, center, width, height, label, textsize):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## self = tells the function that it is refering to the variable that has been given
        ## win = passing in the graphical window that has been created in main
        ## center  = point object where the button should be
        ## width = the width of the button
        ## height = height of the button
        ## label = label that should be on the button
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit', 14) """ 
        w,h = width/2.0, height/2.0   
        x,y = center.getX(), center.getY()  
        ## you should comment these variables...
        ## using the getX and getY function as well as the width and height specifications provided
        ## this function can find the point to create the rectangle button
        self.xmax, self.xmin = x+w, x-w   #xmax and xmin are the corner x points of the button
        self.ymax, self.ymin = y+h, y-h  #ymax and ymin are the corner y points of the button
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setSize(textsize)
        self.label.draw(win)
        self.activate() #this line was not there in class today

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        ##color the text "darkgray"
        self.label.setFill("darkgray")
        ##set the outline to look finer/thinner
        self.rect.setWidth(1)
        ##set the boolean variable that tracks "active"-ness to False
        self.active = False

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        ##your code here
        if self.active:
            if self.xmin<=p.getX()<= self.xmax and self.ymin<=p.getY()<=self.ymax:
                return True
            

    
def main():
    
    ##check 1. create a graphical window in which to test the Button class
    win = GraphWin ("Dice Roller", 300,300)
    
    ##check 2. test the Button constructor method...
    
    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
    diceButton  = Button(win, Point(150, 170), 80, 20, 'Roll Dice')
    quitButton = Button (win, Point(150, 220), 45, 20, 'QUIT')
    ##activate the Roll button
    diceButton.activate()
    quitButton.deactivate()
    
    ##check 3. now test the deactivate() method...
    ##deactivate the "Quit" button

    pt = win.getMouse()
    ##check 4. test the .clicked() method with an if statement
    ##(remove this test code before moving onto the next check)


    ##check 5: 
    ##loop until the "Quit" button is clicked...
    ##if the roll button is clicked
    ##activate the quit button
    ##take the next mouse click
    
    while not quitButton.isClicked(pt):
        if diceButton.isClicked(pt) :
            quitButton.activate()
        pt = win.getMouse()
                   
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__": 
    main()
