# import numpy dan cv2 serta pyplot
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Membaca gambar dengan memasukan gambar anda
img = cv2.imread('isi gambar anda.jpg')
# konfersi gambar ke gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# tresholding
ret, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow("Otsu", thresh)

# Menghapus noise
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

plt.colorbar()
plt.show()
