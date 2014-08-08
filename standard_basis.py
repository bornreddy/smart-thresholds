from PIL import Image
import sys, os

def intensity_snap(low_intensity,image):
  snapped_image = []
  for w in range(0,image.size[1]):
  	for h in range(0,image.size[0]):
  	  intensity = image.getpixel((h,w))
  	  if (intensity <= low_intensity):
  	  	x = 0
  	  else:
  	  	x = intensity
  	  snapped_image.append(x)
  image.putdata(snapped_image)
  image.show()
  filename = str(int((low_intensity/255.0)*100))
  image.save("images/lena" + filename + ".jpg")
  print "wrote file lena" + filename

def generate_images(x):
  for i in range x:
    intensity_snap(i,bw)

try:
  img = Image.open(sys.argv[1])
  img.load()
  img.show()
  bw = img.convert('L')
  intensity_snap(50,bw)
  intensity_snap(240,bw)
except IOError:
  print "Unable to open file. Please try another format."

