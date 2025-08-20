# Clase 1 - Colecciones: Listas (básico)

def h(t):  # helper título
    print("\n" + "="*60)
    print(t)
    print("="*60)

def demo_listas():
    h("LISTAS - OPERACIONES BÁSICAS")

    alumnos = ["Ana", "Luis", "Carla", "Diego"]
    print("Lista inicial:", alumnos)

    # Índices y slicing
    print("Primer elemento:", alumnos[0])
    print("Últimos dos:", alumnos[-2:])

    # Agregar
    alumnos.append("Marta")
    print("append('Marta'):", alumnos)
    alumnos.insert(1, "Pedro")
    print("insert(1, 'Pedro'):", alumnos)

    # Eliminar
    eliminado = alumnos.pop()
    print(f"pop() -> '{eliminado}':", alumnos)
    alumnos.remove("Pedro")
    print("remove('Pedro'):", alumnos)

    # Búsqueda / conteo
    print("'Ana' in lista?", "Ana" in alumnos)
    print("count('Ana'):", alumnos.count("Ana"))

    # Ordenar / invertir
    alumnos.sort()
    print("sort():", alumnos)
    alumnos.reverse()
    print("reverse():", alumnos)

    # List comprehension
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [n*n for n in numeros]
    print("numeros:", numeros)
    print("cuadrados:", cuadrados)

if __name__ == "__main__":
    demo_listas()
