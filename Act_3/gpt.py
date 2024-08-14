import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = 'celulares_.jpg'  
image = cv.imread(image_path)
if image is None:
    print("No se pudo cargar la imagen.")
    exit()

# Convertir la imagen a escala de grises
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Aplicar filtro gaussiano para suavizar la imagen
blurred = cv.GaussianBlur(gray, (5, 5), 0)

# Binarizar la imagen usando un umbral adaptativo
_, binary = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# Mostrar imagen original y binarizada
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
ax[0].set_title('Imagen Original')
ax[0].axis('off')
ax[1].imshow(binary, cmap='gray')
ax[1].set_title('Imagen Binarizada')
ax[1].axis('off')
plt.show()

# Eliminar ruido con apertura morfológica
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)

# Determinar el área de fondo seguro
sure_bg = cv.dilate(opening, kernel, iterations=3)

# Determinar el área de primer plano seguro
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

# Mostrar los resultados del algoritmo watershed
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

axes[0, 0].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
axes[0, 0].set_title('Imagen Original con Bordes Watershed')
axes[0, 0].axis('off')

axes[0, 1].imshow(binary, cmap='gray')
axes[0, 1].set_title('Imagen Binarizada')
axes[0, 1].axis('off')

axes[0, 2].imshow(dist_transform, cmap='gray')
axes[0, 2].set_title('Transformación de Distancia')
axes[0, 2].axis('off')

axes[1, 0].imshow(sure_bg, cmap='gray')
axes[1, 0].set_title('Fondo Seguro')
axes[1, 0].axis('off')

axes[1, 1].imshow(sure_fg, cmap='gray')
axes[1, 1].set_title('Primer Plano Seguro')
axes[1, 1].axis('off')

axes[1, 2].imshow(markers, cmap='nipy_spectral')
axes[1, 2].set_title('Marcadores Watershed')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()

# Imprimir el número de componentes conectados
print(f'Número de componentes conectados: {num_labels}')
