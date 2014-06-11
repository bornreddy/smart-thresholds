from PIL import Image
import sys, os

'''
try:
  img = Image.open(sys.argv[1])
  img.load()
  img.show()
  bw = img.convert('L')
except IOError:
  print "Unable to open file. Please try another format."

threshold = raw_input("Choose threshold value: ") 

intensity_array = []

for w in range(0,bw.size[1]):
  for h in range(0,bw.size[0]):
    intensity = bw.getpixel((h,w))
    if (intensity <= int(threshold)):
      x = 0
    else:
      x = 255
    intensity_array.append(x)

bw.putdata(intensity_array)
bw.show()

'''

def threshold(t, image):
  intensity_array = []
  for w in range(0,image.size[1]):
    for h in range(0,image.size[0]):
      intensity = image.getpixel((h,w))
      if (intensity <= t):
        x = 0
      else:
        x = 255
      intensity_array.append(x)
  image.putdata(intensity_array)
  image.show()  
