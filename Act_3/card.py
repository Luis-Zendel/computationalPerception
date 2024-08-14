from __future__ import print_function
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random as rng
rng.seed(12345)

src = cv.imread('cards.png')
src[np.all(src == 255, axis=2)] = 0

kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float32)
imgLaplacian = cv.filter2D(src, cv.CV_32F, kernel)
sharp = np.float32(src)
imgResult = sharp - imgLaplacian

imgResult = np.clip(imgResult, 0, 255)
imgResult = imgResult.astype('uint8')
imgLaplacian = np.clip(imgLaplacian, 0, 255)
imgLaplacian = np.uint8(imgLaplacian)

bw = cv.cvtColor(imgResult, cv.COLOR_BGR2GRAY)
_, bw = cv.threshold(bw, 40, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

dist = cv.distanceTransform(bw, cv.DIST_L2, 3)
cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)

_, dist = cv.threshold(dist, 0.4, 1, cv.THRESH_BINARY)
kernel1 = np.ones((3,3), dtype=np.uint8)
dist = cv.dilate(dist, kernel1)

dist_8u = dist.astype('uint8')
contours, _ = cv.findContours(dist_8u, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
markers = np.zeros(dist.shape, dtype=np.int32)

for i in range(len(contours)):
    cv.drawContours(markers, contours, i, (i+1), -1)
cv.circle(markers, (5,5), 3, (255,255,255), -1)
markers_8u = (markers * 10).astype('uint8')

# Mostrar todas las imágenes usando Matplotlib
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

axes[0, 0].imshow(cv.cvtColor(src, cv.COLOR_BGR2RGB))
axes[0, 0].set_title('Source Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(cv.cvtColor(imgResult, cv.COLOR_BGR2RGB))
axes[0, 1].set_title('New Sharped Image')
axes[0, 1].axis('off')

axes[0, 2].imshow(cv.cvtColor(imgLaplacian, cv.COLOR_BGR2RGB))
axes[0, 2].set_title('Laplace Filtered Image')
axes[0, 2].axis('off')

axes[1, 0].imshow(bw, cmap='gray')
axes[1, 0].set_title('Binary Image')
axes[1, 0].axis('off')

axes[1, 1].imshow(dist, cmap='gray')
axes[1, 1].set_title('Distance Transform Image')
axes[1, 1].axis('off')

axes[1, 2].imshow(markers_8u, cmap='gray')
axes[1, 2].set_title('Markers')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()
