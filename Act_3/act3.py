import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = 'celulares_.jpg' 
image = cv.imread(image_path)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Aplicar filtro gaussiano
blurred = cv.GaussianBlur(gray, (5, 5), 0)

# Binarizar la imagen
_, binary = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# Eliminar ruido
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)

# Determinar el área de fondo
sure_bg = cv.dilate(opening, kernel, iterations=3)

# Determinar el área de primer plano
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
_, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Encontrar áreas desconocidas
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

# Etiquetar marcadores
num_labels, markers = cv.connectedComponents(sure_fg)

# Añadir uno para que el fondo no sea 0, sino 1
markers = markers + 1

# Marcar la región desconocida con 0
markers[unknown == 255] = 0

# Aplicar el algoritmo watershed
markers = cv.watershed(image, markers)
image[markers == -1] = [255, 0, 0]

# Mostrar los resultados
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

axes[0].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
axes[0].set_title('Imagen Original con Bordes Watershed')
axes[0].axis('off')

axes[1].imshow(binary, cmap='gray')
axes[1].set_title('Imagen Binaria')
axes[1].axis('off')

axes[2].imshow(markers, cmap='nipy_spectral')
axes[2].set_title('Marcadores Watershed')
axes[2].axis('off')

plt.tight_layout()
plt.show()
