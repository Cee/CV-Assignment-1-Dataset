import math

path1 = "CV-Assignment-1-Dataset/chino.png"
path2 = "CV-Assignment-1-Dataset/images/Pork/Original.jpg"

image1 = cv2.imread(path1)
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread(path2)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

pdf1 = get_pdf(gray_image1)
pdf2 = get_pdf(gray_image2)

cdf1 = get_cdf(gray_image1)
cdf2 = get_cdf(gray_image2)

mapping = [0] * L

for i in range(0, L):
  delta = 1
  for j in range(0, L):
    if math.fabs(cdf1[i] - cdf2[j]) < delta:
      delta = abs(cdf1[i] - cdf2[j])
      mapping[i] = j

for index, pixel in np.ndenumerate(gray_image1):
    gray_image1[index] = mapping[pixel]

show_gray_image(gray_image1)

show_hist(gray_image1)

show_hist_bins(gray_image, 256)
show_hist_bins(gray_image, 64)
show_hist_bins(gray_image, 32)

show_pdf(gray_image1)

show_cdf(gray_image1)