#processorclass.py

from PIL import Image
from PIL import ImageFilter
from time import sleep
from graphics import*

class ImgProcessor:
    '''This class is an image processor.
    It contains methods such as applyFilter(), drawGifinWin(), undrawGifinWin(),
    duplicate(), savegif()'''

    def __init__(self, gwin, userfilename):
        self.gwin = gwin
        self.userfilename = userfilename
        self.userjpg= Image.open(self.userfilename)
        self.jpgwidth, self.jpgheight = self.userjpg.size
        self.jpgcenterxpt = self.jpgwidth//2
        self.jpgcenterypt = self.jpgheight//2
        self.userjpgpixels = None
        self.usernewjpg= None
        self.usergifname=''
        self.stickername = ''
        self.userstickerpixels = None
        self.swidth, self.sheight = None, None
        self.userjpgname = ''
        self.userorijpg = None
        
    def imgjpgsize(self):
        '''returns the width and height of user's jpg image'''
        return self.jpgwidth, self.jpgheight

    def imgcenterpt(self):
        '''returns the center x and y point of the user's jpg image'''
        return self.jpgcenterxpt, self.jpgcenterypt

    def applyFilter(self,filtertype, namechoice):
        '''Apply user's choice of filter on image and save user's preferred
        name for the new edited image'''
        
        self.userjpgname= 'inprogress'+str('.jpg')
        self.usergifname = 'inprogress'+str('.gif')

        self.namechoice = namechoice  #save the user's new filename

        #apply filter on the user's image
        if filtertype ==1:
            self.usernewjpg=self.userjpg
            
        elif filtertype==2:
            self.usernewjpg=self.userjpg.filter(ImageFilter.CONTOUR)

        elif filtertype==3:
            self.usernewjpg=self.userjpg.filter(ImageFilter.FIND_EDGES)

        elif filtertype ==4:
            self.usernewjpg=self.userjpg.filter(ImageFilter.EMBOSS)

        elif filtertype ==5:
            self.usernewjpg=self.userjpg.filter(ImageFilter.BLUR)

        #save the new image in jpg and gif format for PIL processing and
        #GUI windows displaying
        self.usernewjpg.save(self.userjpgname)
        self.usernewjpg.save(self.usergifname)
        
        self.userorijpg = self.usernewjpg  #have a variable that holds user's
                                            #image with the applied filter. 
        
##        print('savefilter')
##        self.userorijpg.show()
##        print('done')
        return None

    def drawGifinWin(self, gwin, pos):
        '''open user's edited gif image as a GUI Image object and draw it in
        the graphical window that is passed in as parameter and Point position'''
        self.usernewgif = ImageGUI(pos, self.usergifname)
        self.usernewgif.draw(gwin)
##        print('drawgif')
##        self.userorijpg.show()
        return None
        
    def undrawGifinWin(self):
        '''undraw user's gif so that there isn't too many overlaping images'''
        self.usernewgif.undraw()
        return None

    def duplicate(self, index):
        '''duplicating the user's jpg and gif image allows user to refresh
        later go back to a clean image without stickers on'''
        self.userorijpg.save('inprogress'+str(index)+str('.jpg'))
        self.userorijpg.save('inprogress'+str(index)+str('.gif'))
        self.tempfilename = 'inprogress'+str(index) #assigning the name of the
                                                    #duplicated file to
                                                    #self.tempfilename for easy
                                                    #access
        
        return None

    def refresh(self):
        '''refresh does the swap of filenames to that the self.usernewjpg 
        now takes the duplicated image without stickers and can restart the
        process of applying stickers on the image'''
        
        self.userorijpg = Image.open(self.tempfilename+str('.jpg'))
        self.usernewjpg = self.userorijpg
        self.usergifname = self.tempfilename +str('.gif')
        self.userjpgname = self.tempfilename +str('.jpg')
        
        return None
                                  

    def setupsticker(self, choice):
        '''setting up sticker changes the number inputs to the filename of the
        sticker so that it can be applied on the user's image. At the same time,
        this method gets the width and size of the sticker and assigns it to
        variables. Since it is Christmas, the stickers are Christmas themed'''
        if choice ==0:
            self.stickername = 'mc1.jpg'
        elif choice ==1:
            self.stickername = 'mc2.jpg'
        elif choice == 2:
            self.stickername = 'mc3.jpg'
        elif choice==3:
            self.stickername = 'mc4.jpg'
        elif choice ==4:
            self.stickername = 'mc5.jpg'

        self.userstickerjpg = Image.open(self.stickername)
        self.swidth,self.sheight = self.userstickerjpg.size  #this information
                                        #is needed for later during the resizing
                                        #of the stickers

        return None

    def transformsticker(self, size):
        '''this method transforms the size of the stickers. There are three
        different sizes that user can choose from. '''
##        print('original', self.swidth, self.sheight)
        
        if size=='S':

            self.swidth = self.swidth//3
            self.sheight = self.sheight//3

            self.userstickerjpg= self.userstickerjpg.resize((self.swidth, self.sheight))

        elif size =='M':
            self.swidth = 2*self.swidth//3
            self.sheight = 2*self.sheight//3

            self.userstickerjpg= self.userstickerjpg.resize((self.swidth, self.sheight))

        elif size == 'L':

            self.userstickerjpg= self.userstickerjpg.resize((self.swidth, self.sheight))

##        print('transformed', self.swidth, self.sheight)
        self.swidth, self.sheight = self.userstickerjpg.size  #This is to get
                                        #the new width and height of the stickers
        return None
    
    def pastesticker(self, xpos, ypos):
        '''this process applies the stickers on the user's jpg image using PIL
        .load() pixels & pixel indexing methods
        Then, it is saved over the same file into jpg and gif format'''
        self.userjpgpixels = self.usernewjpg.load()
        self.userstickerpixels= self.userstickerjpg.load()

        for x in range (self.swidth):
            
            for y in range(self.sheight):
                rgb = self.userstickerpixels[x,y]

                if not (rgb[0]>=240 and rgb[1]>=240 and rgb[2]>=240):
                    self.userjpgpixels[xpos-(self.swidth//2)+x,ypos-(self.sheight//2)+y]=self.userstickerpixels[x,y]               

        self.usernewjpg.save(self.userjpgname)
        self.usernewjpg.save(self.usergifname)
        return None

    def savegif(self):
        '''this method saves the latest edited image into the filename that
        that user inputted before.'''
        
        self.usernewjpg.save(self.namechoice+ str('.jpg'))
        return self.namechoice+str('.jpg')
 
    def inboundaries(self, xpos, ypos,centerx, centery):
        '''this method checks if the image, if printed on the image still within
        the image. If it is within, it returns yes, else, it returns false'''
        firstxlimit=centerx-self.jpgwidth//2
        secondxlimit=centerx+self.jpgwidth//2
        firstylimit=centery-self.jpgheight//2
        secondylimit = centery+self.jpgheight//2
        
##        print('aftercheck', self.swidth, self.sheight)
        
        x1 = xpos-(self.swidth//2)+50  #+50 and +126 here is taking into
                                            #account that the image is not printed
                                            #right at (0,0) instead, in the middle
                                            #of the windows
        x2= xpos+(self.swidth//2)+50
        y1= ypos-(self.sheight//2)+126  
        y2=ypos+(self.sheight//2)+126

##        print(firstxlimit,secondxlimit, firstylimit, secondylimit)
##        print(x1, x2, y1, y2)

        if (x1>=firstxlimit) and (x2<=secondxlimit)and (y1>=firstylimit) and (y2<=secondylimit):
                return True
        else:
                return False                                  


def main():
    win = GraphWin('processclasstest', 1000, 800)
    img = ImgProcessor(win, 'jpeg.jpg')
    img.drawGifinWin(win, Point(400,400))
    img.applyFilter('2', 'mypicture')
    img.drawGifinWin(win, Point(400, 400))
    img.setupsticker(1)
    img.transformsticker( 'M')
##    if img.inboundaries(200, 300, 400,400):
    img.pastesticker(200, 200)
    img.drawGifinWin(win, Point(400,400))


    img.setupsticker(2)
    img.transformsticker( 'M')
##    if img.inboundaries(200, 300, 400,400):
    img.pastesticker( 200, 200)
    img.drawGifinWin(win, Point(400,400))


if __name__=="__main__":
    main()
