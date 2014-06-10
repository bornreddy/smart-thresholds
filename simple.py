from PIL import Image
import sys, os

try:
  img = Image.open(sys.argv[1])
  img.load()
  img.show()
  bw = img.convert('L')
except IOError:
  print "Unable to open file. Please try another format."

threshold = raw_input("Choose threshold value: ") 

color_array = []

for w in range(0,bw.size[1]):
  for h in range(0,bw.size[0]):
    color = bw.getpixel((h,w))
    if (color <= int(threshold)):
      x = 0
    else:
      x = 255
    color_array.append(x)

bw.putdata(color_array)
bw.show()
