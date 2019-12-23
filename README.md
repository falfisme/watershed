# watershed

### Watershed Segmentation
pada pembahasan kali ini, saya akan mencoba menerangkan mengenai pembuatan segmentasi pada sebuah gambar dengan pyhton

nah, akan tetapi perlu diketahui gambar diharuskan untuk diconvert terlebih dahulu menjadi gambar skala keabuan atau grayscale
oleh karena itu perlunya package dari cv2

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

setelah dibuat abuabu, maka dilanjut ke tresholding agar sisi gambar terlihat dengan jelas (dapat dibedakan)
ret, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
