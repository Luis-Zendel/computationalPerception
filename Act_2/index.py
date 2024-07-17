import cv2 as cv 
import numpy as np
img1 = cv.imread('cars96.png')
img2 = cv.imread('cars96.png', cv.IMREAD_GRAYSCALE)
alto1, ancho1, canales1 = img1.shape
alto2, ancho2 = img2.shape

print("alto:", alto1, "ancho:", ancho1, "canales:", canales1)
print("alto:", alto2, "ancho:", ancho2,)

imgGris = cv.imread('cars3.png', cv.IMREAD_GRAYSCALE)
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
imgKernel = cv.filter2D(src=imgGris, ddepth=-1, kernel=kernel)
##cv.imshow('Imagen con Kernel', imgKernel)
kernelGaussian = cv.GaussianBlur(imgGris, (9,9),0)
##cv.imshow("ruido", kernelGaussian)

cv.waitKey(0)
cv.destroyAllWindows()