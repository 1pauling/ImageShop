#pageclass.py


from graphics import*
from random import randrange
from time import sleep
from processorclass import*
from buttonclass import*


##This function helps to create text with features
def writeText(gwin, pos, text, font, fSize, fStyle, fColor): #the function can take
                                #various parameter such as the Graphwin, position, 
                                #text, font, fontsize, fontstyle, and font color. 
    #Perform the various features on the text. 
    writeIt = Text((pos), text)
    writeIt.setFace(font)
    writeIt.setSize(fSize)
    writeIt.setStyle(fStyle)
    writeIt.setTextColor(fColor)
    writeIt.draw(gwin) # don't forget to draw the text in the Graphical window! 

#This function creates a text with funky colors
def colorfulText(gwin, startxpt,startypt, text, font, fSize, fStyle):
    #make sure that this function understands the variable the assignment of r, g,
    #and b. 
    r = randrange(0,256)  
    g = randrange(0,256)
    b = randrange(0,256)

    #using a for loop, each character of the word can be created with different
    #colors
    for ch in text:  #each character in the word that we wish to create has to
                     #undergo the following process.
        r,g,b=shuffleColor(r,g,b)   #the R,G,B for each character in the word is
                                    #shuffled.
        #using the function that creates text where I can change its feature
        #create the text I want. 
        writeText(gwin, Point(startxpt, startypt), ch, font, fSize, fStyle,
                   color_rgb(r,g,b))
        startxpt = startxpt+80#This will change the y-point of each character in the
                            #word that is created. (going downwards)


##This function shuffles the R, G, B each time it is called.    
def shuffleColor(r, g, b):
    r = randrange(0,256)
    g = randrange(0,256)
    b = randrange(0,256)

    while r==0 and g ==0 and b==0:   #I will create a board that is black,
                                    # i want to make sure that the random colour
                                    #generated does not clash with the color of the
                                    #board. 
        r = randrange(0,256)
        g = randrange(0,256)
        b = randrange(0,256)        
        
    return r, g, b    #makes sure that the random R, G, B value is returned! 



class Pages:
    '''This class is a class of pages.
    It contains methods such as welcomePage(), greetPage(), inputPage(), and
    processPage(). Using this class, the pages can easily be called. '''
    

    def __init__(self, gwin):
        self.gwin= gwin   #initiating the instance variable and getting the
                            #graphical window passed in as a parameter
        self.imgEdit = None   #this instance variable calls on the processor
                                #class methods. 

    def welcomePage(self):
        '''This method creates the welcome page that contains the cover photo
        of the program'''
        
        #set background, title, texts and image. 
        self.gwin.setBackground("aquamarine2")
        wall = Rectangle(Point(0,525), Point(1010, 675))
        wall.setFill('burlywood')
        ground = Rectangle(Point(0,675), Point(1010, 800))
        ground.setFill('gray39')
        shopImg = ImageGUI(Point(500, 500), "shop.gif")

        text = Text(Point(500, 200), 'IMAGE')
        text.setFace('Phosphate Inline')
        text.setSize(125)

        wall.draw(self.gwin)
        ground.draw(self.gwin)
        shopImg.draw(self.gwin)
        
        #animate the title
        for i in range(10):
            colorfulText(self.gwin, 340,200, 'IMAGE', 'Phosphate Inline', 150, 'bold' )
            sleep(0.2)
            
        #instruction for user. 
        text = Text (Point(500, 750),"Click anywhere to start")
        text.setTextColor('white')
        text.draw(self.gwin)

        pt=self.gwin.getMouse()

        #ensure everything is undrawn in the graphical window(self.gwin) before
        #next method is called. 
        if 0<=pt.getX()<=1000 and 0<=pt.getY()<=800:

            shopImg.undraw()
            wall.undraw()
            ground.undraw()
            text.undraw()
         
        return None

    
    def greetPage(self):
        '''This method greets the user and asks for user's name to engage with
        user right from the start. '''

##        print('in instruc')

        #setting up the room where the program character speaks to the user
        self.gwin.setBackground('blue violet')
        ground = Rectangle(Point(0,675), Point(1010, 800))
        ground.setFill('gray39')
        line= Line (Point(200, 0), Point(200, 575))

        ground = Polygon(Point(0,810), Point(200,575), Point(1000, 575),
                         Point(1010, 8010))
        ground.draw(self.gwin)
        ground.setFill('dark red')
        
        board = Rectangle(Point(275, 125), Point(725, 325))
        board.setFill('black')
        
        board.draw(self.gwin)
        line.draw(self.gwin)
        
        colorfulText(self.gwin, 340,200,'IMAGE', 'Phosphate Inline', 150, 'bold' )
        writeText(self.gwin, Point(500,275) ,'Shop', 'Lucida Handwriting', 48, 'normal',
                    'bisque')
        didiImg = ImageGUI (Point(500, 575), 'deedee1.gif')
        didiImg.draw(self.gwin)
        
        dialogbox = Polygon(Point(700, 200), Point(950, 200), Point(950, 450),
                            Point(745, 450), Point(600, 475), Point(700, 400))
        dialogbox.setFill('white')
        dialogbox.draw(self.gwin)

        reply = Text(Point(825, 250), "")
        reply.draw(self.gwin)

        #a list that contains the phrases that the program will say to the
        #user. 
        textList = ["Hello, my name is Didi","Welcome to ImageShop!", "What is "
                    "your name?\nEnter in the textbox below then click 'OK!'"]
        for phrase in textList:
                    reply.setText(str(phrase))
                    sleep (1.5)

        okButt = Button(self.gwin,Point(825, 500), 30, 25, 'OK', 12)
        inputBox = Entry (Point(825, 300), 10)
        inputBox.draw(self.gwin)

        pt=self.gwin.getMouse()

        #using while loop will allow program to take the user's click until
        #the button 'OK' is clicked. 
        while not okButt.isClicked(pt):
            pt=self.gwin.getMouse()
            
        inputBox.undraw()
        okButt.deactivate()
        userInput= inputBox.getText()
##        print(userInput)


        reply.setText("Hi there, "+ str(userInput)+'!\n\n Nice to meet you!')
        sleep(3)
        reply.setText("Click on me to go to the next page.")
        

        pt=self.gwin.getMouse()

        #Once again, to ensure that the main things are undrawn from window
        #before next method is called. 
        if 0<=pt.getX()<=1000 and 0<=pt.getY()<=800:
            line.undraw()
            ground.undraw()
            dialogbox.undraw()
            reply.undraw()
            didiImg.undraw()
            
        return None

        
    def inputPage(self):
        '''This method gets user's image filename and allows user to choose
        a filter and enter the name that they want their edited image to be
        saved into. '''

        #setting up the background, images, buttons and inputboxes. 
        self.gwin.setBackground('deep pink')

        board = Rectangle(Point(275, 125), Point(725, 325))
        board.setFill('black')
        board.draw(self.gwin)

        colorfulText(self.gwin, 340,200,'IMAGE', 'Phosphate Inline', 150, 'bold' )
        writeText(self.gwin, Point(500,275) ,'Shop', 'Lucida Handwriting', 48, 'normal',
                    'bisque')
        
        inputBox1 = Entry (Point(525, 400), 25)
        boxText1 = Text(Point(350, 400), "Enter your image file name in\n jpeg format"
                       " (Eg: stick.jpg)")
        inputBox2 = Entry (Point(525, 450), 25)
        boxText2 = Text(Point(350, 450),"Enter the name you wish to call\n"
                                "your edited image (Eg: mypicture)")

        didiImg = ImageGUI (Point(850, 475), 'deedee2.gif')
        didiImg.draw(self.gwin)

        dialogbox = Polygon(Point(750, 100), Point(975, 100), Point(975, 300),
                            Point(830, 300), Point(820, 400), Point(810, 300),
                            Point(750, 300))
        dialogbox.setFill('white')
        dialogbox.draw(self.gwin)

        reply = Text(Point(865, 200), "")
        reply.draw(self.gwin)

        textList = ["Click on me \nto find out what you need to do!", 
                    "Enter the filename of an image in jpg format. \n",
                    "Make sure that the image size is \n NOT more than 600x550\n"
                    "&\n it is in the same folder of this program!",
                    "Then click the 'Open' button",
                    "Now, do you see the five buttons in a row?\n Click on them to\n"
                    "view your image in the filters!", "When you're ready, \n"
                    "enter the number of the filter \n&\n the name of your"
                    " newly edited image. \n\nOne final step, click 'Apply'\n "
                    "and start editing your picture! ",
                    "Make sure you have entered \nall information correctly!",
                    "You image dimension \ndoes not meet requirement! \n\n"
                    "Please make sure it is \nno bigger than 600x550. "]

        reply.setText(textList[0])

        pt=self.gwin.getMouse()
        
        inputBox1.draw(self.gwin)
        boxText1.draw(self.gwin)
        quitButt= Button(self.gwin,Point(950, 50), 25, 25, "Quit",12)

        newButt = Button(self.gwin, Point(600, 500), 35, 25, "New",12)
        applyButt = Button(self.gwin,Point(650, 500), 35, 25, "Apply",12)
        openButt= Button(self.gwin,Point(700, 500), 35, 25, "Open",12)
        applyButt.deactivate()        
        normButt = Button(self.gwin,Point(100, 700), 75, 50, "1\nNormal",12)
        outl1Butt = Button(self.gwin,Point(300, 700), 75, 50, "2\nWhite Outline",12)
        outl2Butt = Button(self.gwin,Point(500, 700),75, 50, "3\nBlack Outline",12)
        embossButt= Button(self.gwin,Point(700, 700), 75, 50, "4\nEmboss",12)
        blurButt=Button(self.gwin,Point(900, 700),75, 50, "5\nBlur",12)

        #using for loop to index into the list of phrases the the program
        #would like to say to the user. 
        for index in range(1,6):
            reply.setText(textList[index])
            sleep(5)

        counter = 0  #counter is used during the processing image to have
                     #duplicates of the users image until users click save

        pt=self.gwin.getMouse()
        
        while not quitButt.isClicked(pt):
            
            userInput1= inputBox1.getText()
            userInput2 = inputBox2.getText()
            

            if newButt.isClicked(pt):
##                print('new')
                boxText1.setText("Enter your image file name in\n jpeg format"
                       " (Eg: Kitty.jpg)")
                openButt= Button(self.gwin,Point(700, 500), 35, 25, "Open",12)
                openButt.activate()
                inputBox2.undraw()
                boxText2.undraw()
                
            
            elif openButt.isClicked(pt):
                userInput1 = userInput1.lower()
                if userInput1[(len(userInput1)-4):]=='.jpg':
                    openButt.deactivate()

                    #first time the processor class is called.
                    #set up ImgProcessor object using the user's image filename
                    self.imgEdit = ImgProcessor(self.gwin, userInput1)
                    imgwidth, imgheight = self.imgEdit.imgjpgsize()
##                    print(imgwidth, imgheight)
                    
                    #check if the image is within the dimension 
                    if imgwidth<=600 and imgheight<=550:
##                        print('inwidth')
                        userImg = Image.open(userInput1)

                        boxText1.setText("Enter the number of your \nprefered filter"
                               " (Eg: 1,2,3,4,or 5)")
                        inputBox2.draw(self.gwin)
                        boxText2.draw(self.gwin)
                        sleep(2.0)
                        applyButt.activate()

                        normButt.activate()
                        outl1Butt.activate()
                        outl2Butt.activate()
                        embossButt.activate()
                        blurButt.activate()

                    #return phrase that says image file dimensions does not
                    #meet requirement
                    else:
                        reply.setText(textList[-1])
                        openButt.activate()
                #if wrong input, tell user to ensure input is correct
                else:
                    reply.setText(textList[-2])

            #if filter buttons are clicked
            elif normButt.isClicked(pt) :
                filterImg = userImg
                filterImg.show()

            elif outl1Butt.isClicked(pt):
                filterImg = userImg.filter(ImageFilter.CONTOUR)
                filterImg.show()

            elif outl2Butt.isClicked(pt) :
                filterImg = userImg.filter(ImageFilter.FIND_EDGES)
                filterImg.show()
                
            elif embossButt.isClicked(pt) :
                filterImg = userImg.filter(ImageFilter.EMBOSS)
                filterImg.show()
                
            elif blurButt.isClicked(pt) :
                filterImg = userImg.filter(ImageFilter.BLUR)
                filterImg.show()

            
            elif applyButt.isClicked(pt):
                
                #check if input is a string, if yes, ask user to input the correct
                #input. 
                if userInput1.isalpha() ==True:
                    reply.setText(textList[-2])
                
                #check if input is a number and a string
                elif float(userInput1).is_integer()==True and len(userInput2)!=0:
                    userInput1 = eval(userInput1)
                    #check if user's number is within 1-5 only
                    if (userInput1<1 or userInput1>5):

                        reply.setText(textList[-2])
                       
                    elif ((1<=userInput1 or userInput1<=5)) and len(userInput2)!=0 :

                        filtertype = userInput1
                        applyButt.deactivate()

                        #call on methods in the processorclass
                        self.imgEdit.applyFilter(filtertype, userInput2)
                        self.imgEdit.duplicate(counter)
                        inputBox1.undraw()
                        inputBox2.undraw()
                        
                        return 'next'


                else:
                    reply.setText(textList[-2])

            elif quitButt.isClicked(pt):
                return 'quit'
            
            pt=self.gwin.getMouse()

        return 'quit'


    def processPage(self):
        '''This method creates the final page where user can perform edits on
        the image by putting on stickers (Christmas themed)'''

        #setting up the background, buttons, center Point for the image,
        #inputboxes, help instruction, 
        background = Rectangle(Point(0,0), Point(1010, 810))
        background.setFill('pale green')
        background.draw(self.gwin)

        didiImg = ImageGUI(Point(875, 700), 'deedee3.gif')
        didiImg.draw(self.gwin)

        dialogbox = Polygon(Point(350, 700), Point(725,700), Point(725, 760),
                            Point(800, 715), Point(725, 780), Point(725, 790),
                            Point(350, 790))
        dialogbox.setFill('white')
        dialogbox.draw(self.gwin)

        reply = Text(Point(540, 745), "")
        reply.draw(self.gwin)

        imgcenterx, imgcentery = self.imgEdit.imgcenterpt()
        gifcenterx = imgcenterx+50
        gifcentery = imgcentery+126
        imgwidth, imgheight = self.imgEdit.imgjpgsize()
        
        yline = Line(Point(49,80), Point(49, 676))
        yline.setArrow('first')
        yline.draw(self.gwin)
        xline = Line(Point(49, 676), Point(675, 676))
        xline.setArrow('last')
        xline.draw(self.gwin)
        ylabel= Text(Point(50, 70), 'y')
        xlabel =Text(Point(680, 675), 'x')
        ylabel.draw(self.gwin)
        xlabel.draw(self.gwin)
       
        corner1 = Text(Point(49, 682), 'x\n(50, 676)')
        corner2 = Text(Point(650, 682), 'x\n(650, 676)')
        corner3 = Text(Point(650, 120), '(650, 126)\nx')
        corner4 = Text(Point(49, 120), '(50, 126)\nx')
     
        corner1.draw(self.gwin)
        corner2.draw(self.gwin)
        corner3.draw(self.gwin)
        corner4.draw(self.gwin)

        quitButt= Button(self.gwin,Point(950, 50), 50, 50, "Quit",16)
        backButt= Button(self.gwin,Point(890, 50),50,50, "Back",16)
        refreshButt = Button(self.gwin, Point(755, 50), 75, 50, "Refresh", 16)
        saveButt= Button(self.gwin, Point(830, 50), 50, 50,"Save", 16)
        
        drawButt= Button(self.gwin, Point(950, 600), 35, 25, "Draw", 12)
        drawButt.deactivate()

        leftarrowButt= Button(self.gwin, Point(715, 225), 15, 15, '<', 12)
        rightarrowButt = Button(self.gwin, Point(975, 225), 15, 15 ,'>', 12)

        display= Rectangle(Point(725, 100), Point(965, 350))
        display.setFill('white')
        display.draw(self.gwin)

        #a list to easily access the stickers for display
        stickergiflist = ['mc1.gif', 'mc2.gif','mc3.gif', 'mc4.gif', 'mc5.gif']
        stickerindex=0 #this is the index for the sticker label and display,
                        #and accessing sticker when user chooses to put it on
                        # their image. 
        sticker=ImageGUI(Point(845,225), stickergiflist[stickerindex])
        stickerlabel= Text(Point(845, 370), '')
        stickerlabel.draw(self.gwin)

        inputbox2 = Entry(Point(875,450), 5)
        inputbox3 = Entry(Point(875,500), 5)
        inputbox4 = Entry(Point(875,550),5)

        boxText2 = Text(Point(775,450), "Sticker Size:\n (S/M/L)")
        boxText3 = Text(Point(775,500), "x-coordinate:")
        boxText4 = Text(Point(775,550),"y-coordinate:")

        inputbox2.draw(self.gwin)
        inputbox3.draw(self.gwin)
        inputbox4.draw(self.gwin)

        boxText2.draw(self.gwin)
        boxText3.draw(self.gwin)
        boxText4.draw(self.gwin)

        helpText = Text(Point(570,57), "Need Help?\n'Refresh' & Click Anywhere: Remove stickers & "
                                    "start over \n'Save': Save your edited image \n"
                                    "'Back': Return to the previous page to \nopen "
                                    "a new image file. \nDouble click 'Quit': Close out of program")

        textList = ["I hope you're ready to do some image editing!",
                    "Before you start, let me first explain to you what you can"
                    " do. \n\n Choose the sticker that you like",
                    "Input the size of your sticker choice \n Either 'S', 'M', or "
                    "'L'","Input the coordinates x and y, \nwhere "
                    "you want your sticker to be. \nUse the corners of the "
                    "Cartesian plane as a guide."," If the coordinates you provide "
                    "is out of your image, \nit will not print on your image.",
                    "Once you all the input boxes filled, click 'Draw'!",
                    "Whenever you're ready, click on me to start!",
                    "Please make sure you enter input correctly!",
                    "The x and y coordinates you entered is out of your image!\n"
                    "Please enter new coordinates and click 'Draw'."]
        for index in range(7):
                    reply.setText(textList[index])
                    sleep (4.5)

        pt = self.gwin.getMouse()
        helpText.draw(self.gwin)
        reply.setText('Good luck!')
        drawButt.activate()
        stickerlabel.setText(str(stickerindex))
        sticker.draw(self.gwin)

        counter = 0 #like in the method before, this counter indicates the
                    #number of duplicates of the user's image. (necessary
                    #for the refresh method so that user can refresh their
                    #edits if necesssary.
        


        while not quitButt.isClicked(pt):
            

            startover = False
           
            while startover ==False:
##                print('secondwhile')

                self.imgEdit.drawGifinWin(self.gwin, Point(gifcenterx, gifcentery))
                
                if drawButt.isClicked(pt) :

                    size = (inputbox2.getText()).upper()
                    xcoord = inputbox3.getText()
                    ycoord = inputbox4.getText()

                    #checks to see if all inputs are correct and to ensure that
                    #program does not crash when wrong input is given. 
                    if (size.isalpha()==True) and (float(xcoord).is_integer()==True) and (float(ycoord).is_integer()==True): 

                        #Checks to make sure that the right letters are given,
                        #else, tell user to check input
                        if (size=='S' or size =='M' or size=='L'):
                            self.imgEdit.setupsticker(stickerindex)
                            self.imgEdit.transformsticker(size)

                            #if statement checks if the coordinates provided by the
                            #user for the stickers are within the boundaries of the
                            #image. If yes, process, if not, return a phrase to
                            #ask for new coordinates. 
                            if self.imgEdit.inboundaries(eval(xcoord), eval(ycoord),gifcenterx,gifcentery):
                                self.imgEdit.pastesticker( eval(xcoord), eval(ycoord))
                                self.imgEdit.undrawGifinWin()
                                self.imgEdit.drawGifinWin(self.gwin,Point(gifcenterx, gifcentery))
                            else:
                                reply.setText(textList[-1])
                        
                        else:
                            reply.setText(textList[-2])
                            
                    elif float(size).is_integer()==True or xcoord.isalpha()==True or ycoord.isalpha()==True:
                        reply.setText(textList[-2])
                        
                            
                    else:
                        reply.setText(textList[-2])

                elif refreshButt.isClicked(pt):
##                    print('inrefresh')
                    self.imgEdit.undrawGifinWin()
                    self.imgEdit.refresh() #refresh methods assigns the name of 
                                            #duplicated image to the variable
                                            #that holds the image for editing
                    
                    counter +=1 #increase counter 
                    self.imgEdit.duplicate(counter) #and make another duplicate
                                                    #for the next time when
                                                    #user clicks the refresh
                    startover = True  #change the flag so that it gets out of the
                                        #while loop and starts over. 
                                        
##                    print(startover)

                
                elif saveButt.isClicked(pt):
                    savefilename = self.imgEdit.savegif()  #call on savegif method
                                                #from processorclass to save
                                                #user's edited image to the
                                                #filename that user gave previously
                    reply.setText("Your edited image is saved under the filename, "
                                  + str(savefilename)+"\n\nPlease look for the"
                                  " file in the same folder! Enjoy!")

                elif backButt.isClicked(pt):

                    inputbox2.undraw()
                    inputbox3.undraw()
                    inputbox4.undraw()

                    #since there is too many things to undraw from this page,
                    #a background is used to overlap all the images drawn on
                    #graphical window. 
                    newbackground = Rectangle(Point(0,0), Point(1010, 810))
                    newbackground.setFill('deep pink')
                    newbackground.draw(self.gwin)

                    return 'back'
                
                elif quitButt.isClicked(pt):
                    startover = True

                #allow user to browse through the stickers and choose
                #the sticker of their choice to put on their image
                elif leftarrowButt.isClicked(pt) and (0<=stickerindex<=4):
                    stickerindex-=1
                    if stickerindex<=-1:
                        stickerindex=0
                    sticker.undraw()
                    sticker=ImageGUI(Point(845,225), stickergiflist[stickerindex])
                    sticker.draw(self.gwin)
                    stickerlabel.setText(str(stickerindex))
                    
                elif rightarrowButt.isClicked(pt) and (0<=stickerindex<=4):
                    stickerindex+=1
                    if stickerindex>=4:
                        stickerindex=4
                    sticker.undraw()
                    sticker=ImageGUI(Point(845,225), stickergiflist[stickerindex])
                    sticker.draw(self.gwin)
                    stickerlabel.setText(str(stickerindex))
                    
                pt=self.gwin.getMouse()
                
            if quitButt.isClicked(pt):
                return 'quit'
        return 'quit'

        

def main():
    win = GraphWin('shop', 1000, 800)
    page = Pages(win)
    page.welcomePage()
    page.greetPage()
    option=page.inputPage()

    while option!="quit":
        option = page.processPage()

        if option=='back':
            option=page.inputPage()

    win.close()
    

if __name__=="__main__":
    main()

