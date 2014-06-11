from PIL import Image
import os, sys
import numpy as np

try:
  img = Image.open(sys.argv[1])
  img.load()
  img.show()
  bw = img.convert('L')
except IOError:
  print "Unable to open file. Please try another format."

# create np.histogram from the opened image

# b and f indicate background and foreground
def otsu(hist, total):
  sum = 0;
  # iteratively add up all intensities of all pixels
  for i in range(0,255):
    sum += i * histogram[i]
  sumB = 0
  sumF = 0
  wB = 0
  wF = 0
  mB = 0
  mF = 0
  max = 0.0
  between = 0.0
  thresh1 = 0.0
  thresh2 = 0.0
  for i in range(0,255):
    # find the weight of the background pixels (the number of pixels in background)
    wB += histogram[i]
    if wB == 0:
      continue
    # find weight of foreground pixels (number of pixels in foreground)
    wF = sum - wB
    if wF == 0:
      break
    # find the sum of the background pixels
    sumB += i * histogram[i]
    sumF = sum - sumB
    #calculate background/foreground average intensity
    mB = sumB/wB 
    mF = sumF/wF
    # calculate 
    between = wB * wF * (mB - mF)**2
    
    
    
    
    
   

'''
total_pixels = bw.size[0] * bw.size[1]
histogram = {}

for w in range(0,bw.size[0]):
  for h in range(0,bw.size[1]):
    intensity = bw.getpixel((w,h))
    if intensity in histogram:
      histogram[intensity] += 1
    else:
      histogram[intensity] = 1

def all_probs(hist):
  p_hist = {}
  for x in hist.keys():
    p_hist[x] = hist[x]*1.0/total_pixels
  return p_hist

prob_histogram = all_probs(histogram)  
print bw.size
print histogram
print prob_histogram
'''


