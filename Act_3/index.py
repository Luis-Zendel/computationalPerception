import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('edificios.jpg')
if image is None:
    print("No se pudo cargar la imagen.")
else:
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    plt.figure(figsize=(20, 10))
    plt.imshow(image_rgb)
    plt.title('Imagen Original')
    plt.axis('off')
    plt.show()  # Asegura que la imagen se muestre

    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 2  # Número de clusters
    compactness, labels, centers = cv.kmeans(pixel_values, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    print(compactness)
    print(labels)
    print(centers)

    center = np.uint8(centers)
    print(center)
    res = centers[labels.flatten()]
    res1 = res.reshape((image.shape))
    res2= res1.astype(np.uint8)
    res2.shape
    plt.figure(figsize=(20, 10))
    plt.imshow(res2)
    plt.title('Imagen Resultante')
    plt.axis('off')
    plt.show()


    ## CONNECTED COMPONENTS 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
image_path = 'edificios.jpg'  # Reemplaza esto con la ruta de tu imagen
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convertir la imagen a binaria utilizando un umbral
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Aplicar la función connectedComponents
num_labels, labels_im = cv2.connectedComponents(binary_image)

# Mostrar la imagen original y la imagen con los componentes conectados etiquetados
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(binary_image, cmap='gray')
ax[0].set_title('Imagen binaria')
ax[0].axis('off')

ax[1].imshow(labels_im, cmap='nipy_spectral')
ax[1].set_title('Componentes conectados')
ax[1].axis('off')

plt.show()

# Imprimir el número de componentes conectados
print(f'Número de componentes conectados: {num_labels}')
