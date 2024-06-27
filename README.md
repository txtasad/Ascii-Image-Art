
# Ascii-Image-Art Readme


**🌱 ASCII-IMAGE-ART package for converting images into ASCII character strings and ASCII character colored images.**


<img alt="Elephant ASCII Conversion" src="https://raw.githubusercontent.com/txtasad/Ascii-Image-Art/main/elephant.png?raw=true" width="200" /> <img alt="Human ASCII Conversion" src="https://raw.githubusercontent.com/txtasad/Ascii-Image-Art/main/human_inverted.png?raw=true" width="200" /> <img alt="Female ASCII Conversion" src="https://raw.githubusercontent.com/txtasad/Ascii-Image-Art/main/female.png?raw=true" width="200" /> <img alt="Chicken ASCII Conversion" src="https://raw.githubusercontent.com/txtasad/Ascii-Image-Art/main/chicken_inverted.png?raw=true" width="200" />


**Import**

- 🔗 from ascii_image_art import ASCIIArt


**Parameters**

```obj = ASCIIArt( path = 'path to file without dots'[mandatory], scale = 0.1 [optional], chars = 'string of characters'[optional], filename = 'name of file you want to save with without extension'[optional] )```

- 🔗 path = absolute path to image file available locally. Don't use dots in the file name or file path. 
- 🔗 filename = name of file you would be saving the final processed results with. Don't provide any extension like '.txt' or '.png' just the name.
- 🔗 scale = from 0.01 to 1. The scaled percentage of image of you want your end text and image with. By default = 0.1 or 10%.
- 🔗 chars = character 'string' you want to recreate the image with.


**Methods**

a.getPath()
a.convert()
a.printASCII()
- 🔗 getPath() : incase you don't want to pass the mandatory path to image and want to ask for image path at runtime from user. 
- 🔗 convert() : to convert image to ascii. Use - `obj.convert()`
- 🔗 getASCII() : returns an ascii image in string format.
- 🔗 printASCII() : prints the ascii string like below.



                                                                         
                                                                         
                              D..AA.AD                                   
                             A   . S..                                   
                                      S                                  
                            D AAASSAA                                    
                              S..AA A..                                  
                             SSAASAAAAA                                  
                              AAA..A..A                                  
                             A ..AA.  AD                                 
                            SDA       AS                                 
                       DDDDDDDA      .SDDS                               
                      DDDDDDDDS.    SASSDDDDD                            
                      DDDDDDDDDSSA   SDDDDDDD                            
                     DDDDDDDDDDDDS  DDDDDDDDD                            
                    DDDDDSDDDDDDDD. DDDDDDDDD                            
                   DDDDDDDDDDDDDD. SDDDDDDDDD                            
                   DDDDDDSDDDDDDD .DDDDDDSDDD                            
                  DDDDDDDDDDDDDDDS.DDSDDDDDDD                            
                  DDDDDDDDDDDDDDDDDDDDDDDDDDD                            
                  DDDDDDDDDDDDDDDDDDDDDDDDDDD                            
                  DDDDDDDDDDDDDDD DSDDDSDDDD                             
                  DDDDDDDDDDDDDDDDSDDDSDDDDD                             
                   DSDDDDDDDDDDDDSDDDDDDDDS                              
                    DDDDDDDDDDDDSDDDDDDDDD                               
                    DDDDDDDDDDDD DDDDDDDD                                
                    DSDDDSDSDDDD.DDDDDDD                                 
                   DDDDDDDDDDDA.AAADDDSS                                 
                  SDDDDDDDDDAAA .AAADSSS                                 
                  DDDDDDDDSA.AAAA..SSSSS                                 
                  DDDDDDDDDS.AA...SSSDDD                                 
                   SDDDDDDSDDSDDSSDDDD.                                  
                   DDDSDSDDDDDDDDDDDD                                    
                   DDDDDDDSDDSDDDDDDDD                                   
                   DDDDDDDSD DDDDDDDDD                                   
                   DDDDDDSS  DDDDDDDD                                    
                   DDDDDDDS  SDDDDDDD                                    
                   DDDDDDS   DDDDDDDD                                    
                   DDDDDDS   DDDDDDDD                                    
                   DDDDDDS   DDDDDDDD                                    
                   SDDDSS   DDDDDDDDA                                    
                   DDDDSS DDDDDDDDDD                                     
                   DDDSSSDDDDDDDDDD                                      
                   DDDSDDDDDDDDDDS                                       
                   DSDDDDDDDDDDS                                         
                   DDDDDDDDDDDD                                          
                  DDDDDDDDDDD                                            



- 💞️ Thank You. Mohammad ASAD


