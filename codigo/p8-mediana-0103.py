#Santiago Medrano 0103
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/Flamenco 2.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen, 7)
# Mostrar imágenes
cv2.imshow("Flamenco original 0103", imagen)
cv2.imshow("Imagen con filtro de mediana 0103", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultados/paisaje_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("resultados/paisaje_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Santiago Medrano NC 0103")