############# Images ASCII TEXT file and ASCII colored Images by Mohammad Asad ##########
#### Added AI & ML module by Mohammad Asad ####

from PIL import Image, ImageDraw, ImageFont

from sklearn.cluster import KMeans
import numpy as np
import math

__VERSION__ = 0.4


class usingAIClass:
    ascii=""
    def __init__(self, chars="", path="", filename="OutputAI", scale=0.1, K=2):
        self.chars = chars
        self.path = path
        self.K = K
        self.filename = filename
        self.chars_i = self.chars[::-1]
        self.charArray = list(self.chars)
        self.charArrayI = list(self.chars_i)
        self.charLength = len(self.charArray)
        
        self.interval = self.charLength/256
        self.scaleFactor = scale
        self.oneCharWidth = 10
        self.oneCharHeight = 18
        
    def getChar(self, inputInt, i=False):
        if i:
            return self.charArrayI[math.floor(inputInt*self.interval)]
        return self.charArray[math.floor(inputInt*self.interval)]
    
    def clustering(self,image: np.ndarray, **kmeans_kwargs: dict[str, any]) -> tuple[np.ndarray, np.ndarray]:
        col=3
        if (self.path[-3:len(self.path)].lower()=='png'):
            col=4
        else:
            col=3
        pixels = image.reshape((image.shape[0] * image.shape[1], col))
        kmeans = KMeans(**kmeans_kwargs)
        kmeans.fit(pixels)
        compressed_image = kmeans.labels_.astype(np.uint8) # y_predict and convert to uint8
        centroids = kmeans.cluster_centers_ # total bits = (3or4) columns * 8 * K(clusters)
        return compressed_image, centroids

    def convert(self):
        if self.path == None or self.path=="" or len(self.path)<5:
            print("Provide a Path to the Image! You can also use `getPath()` method to get path runtime from user.")
            return
        image=None
        try:
            image = np.array(Image.open(self.path))
        except Exception as e:
            print(self.path, "Invalid Image.",e)
            return
        original_shape=image.shape

        compressed_image, centroids = self.clustering(image, n_clusters=self.K, n_init="auto", max_iter=300, random_state=42)
        reconstructed_image_array = centroids[compressed_image]
        reconstructed_image = reconstructed_image_array.reshape(original_shape).astype(np.uint8)
        ri=Image.fromarray(reconstructed_image)
        ri.save('compressed.png')
        rii=Image.open('compressed.png')
        
        im = rii.resize((int(self.scaleFactor*original_shape[1]), int(self.scaleFactor*original_shape[0]*(self.oneCharWidth/self.oneCharHeight))), Image.NEAREST)
        pix = im.load()
        width, height = im.size
        #image from ascii image
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
                ascii=ascii+self.getChar(h)
                d1.text((j*self.oneCharWidth, i*self.oneCharHeight), self.getChar(h), fill = (r, g, b))
                d2.text((j*self.oneCharWidth, i*self.oneCharHeight), self.getChar(h,True), fill = (r, g, b))
            ascii=ascii+'\n'
        
        text_file.write(ascii)
        text_file.close()
        self.ascii=ascii
        outputImage1.save(self.filename+'.png')
        outputImage2.save(self.filename+'_inverted.png')
    
    def printASCII(self):
        if len(self.ascii)>5:
            print(self.ascii)

    def getASCII(self):
        return self.ascii