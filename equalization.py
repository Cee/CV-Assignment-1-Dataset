mapping = [0] * L

cdf = get_cdf(gray_image)

for i in range(0, L):
  mapping[i] = int(round(cdf[i] * L))

for index, pixel in np.ndenumerate(gray_image):
    gray_image[index] = mapping[pixel]

# Image
show_gray_image(gray_image)

# Histogram
show_hist(gray_image)

show_hist_bins(gray_image, 256)
show_hist_bins(gray_image, 64)
show_hist_bins(gray_image, 32)
show_hist_bins(gray_image, 16)

# PDF
show_pdf(gray_image)

# CDF
show_cdf(gray_image)