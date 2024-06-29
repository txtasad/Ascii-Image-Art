############# Images ASCII TEXT file and ASCII colored Images by Mohammad Asad ##########
import PIL
from PIL import Image, ImageDraw, ImageFont
import math
import urllib.request
import asyncio
from ascii_image_art.constants import CHARS_BY_DENSITY
from ascii_image_art.usingAI import usingAIClass


__VERSION__ = 0.5


class ASCIIArt:
    ascii=""
    K=2
    def __init__(self, chars=None, path="", filename="Output",scale=0.1):
        self.chars = CHARS_BY_DENSITY if not chars else chars
        self.path = path
        self.filename = filename
        self.chars_i = self.chars[::-1]
        self.charArray = list(self.chars)
        self.charArrayI = list(self.chars_i)
        self.charLength = len(self.charArray)
        
        self.interval = self.charLength/256
        self.scaleFactor = 0.1 if scale>1.01 or scale<0.01 else scale
        self.oneCharWidth = 10
        self.oneCharHeight = 18
        
    def getChar(self, inputInt, i=False):
        if i:
            return self.charArrayI[math.floor(inputInt*self.interval)]
        return self.charArray[math.floor(inputInt*self.interval)]
        
    def getPath(self):
        if self.path == None or self.path=="":
	    p=""
            try:
                p = input("Enter a Pathname to an Image:\n")
                ext=p.lower().split('.')[1]
                if ext=='png' or ext=='jpg' or ext =='webp' or ext=='jpeg':
                    self.path=p
                else:
                    print('Only PNG/JPG/WEBP Images allowed!')
            except Exception as e:
                print(p, " is not a valid pathname to an image.",e)

    def convert(self):
        if self.path == None or self.path=="" or len(self.path)<5:
            print("Provide a Path to the Image! You can also use `getPath()` method to get path runtime from user.")
            return
        image=None
        try:
            image = Image.open(self.path)
                        # fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
        except Exception as e:
            print(self.path, "Invalid Image.",e)
        
        width, height = image.size
        im = image.resize((int(self.scaleFactor*width), int(self.scaleFactor*height*(self.oneCharWidth/self.oneCharHeight))), Image.NEAREST)
        width, height = im.size
        pix = im.load()
		# image from ascii image
        outputImage1 = Image.new('RGB', (self.oneCharWidth * width, self.oneCharHeight * height), color = (0, 0, 0))
        outputImage2 = Image.new('RGB', (self.oneCharWidth * width, self.oneCharHeight * height), color = (0, 0, 0))
        # to draw on that image canvas
        d1 = ImageDraw.Draw(outputImage1)
        d2 = ImageDraw.Draw(outputImage2)
        
        text_file = open(self.filename+".txt", "w")
        ascii=""
        
        for i in range(height):
            for j in range(width):
                                		r, g, b, a = 255,255,255,255
                                		if (self.path[-3:len(self.path)].lower()=='png'):
                                        			r,g,b,a=pix[j, i]
                                		else:
                                        			r,g,b=pix[j, i]
                                		h = int(r/3 + g/3 + b/3)
                                		pix[j, i] = (h, h, h)
                                		ascii=ascii+self.getChar(h)
                                		d1.text((j*self.oneCharWidth, i*self.oneCharHeight), self.getChar(h), fill = (r, g, b))
                                		d2.text((j*self.oneCharWidth, i*self.oneCharHeight), self.getChar(h,True), fill = (r, g, b))
            ascii=ascii+'\n'
        
        text_file.write(ascii)
        text_file.close()
        self.ascii=ascii
        outputImage1.save(self.filename+'.png')
        outputImage2.save(self.filename+'_inverted.png')

    def convertWithAI(self, depth):
        self.K = 3 if depth>50 or depth<2 else depth
        a=usingAIClass(chars=self.chars,path=self.path,scale=self.scaleFactor,K=self.K,filename=self.filename+"AI")
        a.convert()
        a.printASCII()
    
    def printASCII(self):
        if len(self.ascii)>5:
            print(self.ascii)

    def getASCII(self):
        return self.ascii