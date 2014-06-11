import basic_threshold as bt
import otsu 
from PIL import Image

file_name = "images/kidney.jpg"

try:                                                                                      
  img = Image.open(file_name)                                                             
  img.load()                                                                              
  img.show()                                                                              
  bw = img.convert('L')                                                                   
except IOError:                                                                           
  print "Unable to open file. Please try another format."

otsu.otsu(bw)

print "hopefully I get to this point, with a color image and a black and white image showing"
