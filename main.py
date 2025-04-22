# remove_watermark.py
# Script para eliminar la marca de agua de la imagen 'as.png'
# Requiere: OpenCV (cv2)

import cv2
import numpy as np
import os

# Ruta de entrada y salida
ingreso = 'D:/MER/plunar/as.png'
salida = 'D:/MER/plunar/as_clean.png'

# Verificar que el archivo exista\if not os.path.exists(ingreso):
print(f"Error: no se encontró '{ingreso}'. Coloca este script junto a la imagen.")
exit(1)

# Cargar la imagen
img = cv2.imread(ingreso)

# Convertir a escala de grises para detectar la marca de agua (píxeles muy claros)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Dilatar la máscara para cubrir todo el texto/noise
kernel = np.ones((3,3), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=2)

# Inpaint (rellenar) las áreas de la marca de agua
inpainted = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# Guardar la imagen resultante
cv2.imwrite(salida, inpainted)
print(f"Imagen limpia guardada en: {salida}")
