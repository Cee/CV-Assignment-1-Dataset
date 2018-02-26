import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

path = "CV-Assignment-1-Dataset/images/Pork/Original.jpg"

L = 2**8

def show_image(image):
  plt.axis('off')
  plt.imshow(image)
  plt.show()
  
def show_gray_image(image):
  plt.axis('off')
  plt.imshow(image, cmap = 'gray')
  plt.show()
  
def get_hist(image):
  hist = [0] * L
  
  for index, pixel in np.ndenumerate(image):
    hist[pixel] += 1
    
  return hist
  
def get_pdf(image):
  hist = [0] * L
  hist = get_hist(image)
  
  pdf = [0] * L
  height = 0
  width = 0
  size = 0
  (height, width) = image.shape[:2]
  size = height * width

  for i in range(0, L):
    pdf[i] = hist[i] / size
  
  return pdf
  
def get_cdf(image):
  pdf = [0] * L
  pdf = get_pdf(image)
  cdf = [0] * L
  
  for i in range(0, L):
    cdf[i] = cdf[i - 1] + pdf[i]
    
  return cdf
  
def show_hist(image):
  plt.plot(get_hist(image), color = 'r')
  plt.xlim([0, L])
  plt.ylim(ymin=0)
  plt.title("Histogram of Image")
  plt.show()

def show_hist_bins(image, bins=L):
  data = []
  if bins > L:
    bins = L
  for index, pixel in np.ndenumerate(image):
    data.append(pixel)
  plt.hist(data, bins=bins, range=[0, L-1])
  plt.title("Histogram of Image with " + str(bins) + " bins")
  plt.show()
  
def show_pdf(image):
  plt.plot(get_pdf(image), color = 'g')
  plt.xlim([0, L])
  plt.ylim(ymin=0)
  plt.title("Probability Density Function of Image")
  plt.show()
  
def show_cdf(image):
  plt.plot(get_cdf(image), color = 'b')
  plt.ylim(ymin=0, ymax=1.1)
  plt.xlim([0, L - 1])
  plt.title("Cumulative Distribution Function of Image")
  plt.show()
  
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Original Image
# show_image(image)

# Gray Image
show_gray_image(gray_image)

# Histogram
show_hist(gray_image)

show_hist_bins(gray_image, 256)
show_hist_bins(gray_image, 64)

# PDF
show_pdf(gray_image)

# CDF
show_cdf(gray_image)