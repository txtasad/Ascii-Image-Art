from ascii_image_art.ascii_images_and_text import ASCIIArt
from ascii_image_art.usingAI import usingAIClass

a=ASCIIArt(chars=' .ASD',path='',scale=0.05)
a.getPath()
a.convert()
a.convertWithAI(depth=3)
a.printASCII()