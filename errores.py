class PrecioNoValido(Exception):
    pass
class DescripcionVacia(Exception):
    pass

def verificarPrecio(precio):
    if precio < 0 or precio == 0:
        raise PrecioNoValido("El precio no puede ser menor o igual a 0.")
def comprobarDescripcion(descripcion):
    if not descripcion.strip():
        raise DescripcionVacia("Debes añadir una descripción")