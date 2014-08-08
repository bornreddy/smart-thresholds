smart-thresholds
================

Python implementation of basic and Otsu thresholding algorithms. This project consists of my implementation of a standard image thresholding algorithm, along with the more intelligent Otsu's thresholding algorithm, which selects a threshold value by minimizing the inter-class variance between the intensities of the two binary clusters along all possible thresholds. A good next step would be to intelligently pare down the number of thresholds tested in Otsu's, decreasing runtime in practical situations. 
