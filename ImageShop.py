#Roxanne Low
#Final Project COM 110 (Fall 2015)
#ImageShop.py

from graphics import*
from pageclass import*   
    
def main():
    #Create graphical window of 1000x800 dimension
    win = GraphWin("ImageShop", 1000, 800)

    #Call upon different pages in the Pages class
    page = Pages(win)

    page.welcomePage()
    page.greetPage()

    #page.inputPage() is assigned to the variable 'option' because the function
    #will return the string that indicates with function should be called
    option = page.inputPage()

    #using a while loop, user can constantly go back and fort from the two pages
    #inputPage() and processPage()
    while option!='quit':
        option = page.processPage()
        if option=='back':
            option=page.inputPage()

    #if while loop is broken, then the graphical window will close
    win.close()

main()

    
