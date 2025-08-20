# Clase 1 - Colecciones: Tuplas (ejercicios)

def h(t):
    print("\n" + "-"*60)
    print(t)
    print("-"*60)

def demo_tuplas():
    h("TUPLAS - PRÁCTICA")

    dias = ("lun", "mar", "mie", "jue", "vie", "sab", "dom")
    print("Tupla:", dias, "| len:", len(dias))

    print("Primer día:", dias[0])
    print("Último día:", dias[-1])
    print("'mar' en dias?", "mar" in dias)

    print("count('lun'):", dias.count("lun"))
    print("index('jue'):", dias.index("jue"))

    # Convertir a lista para 'modificar'
    dias_lista = list(dias)
    dias_lista[0] = "lunes"
    print("Lista modificada:", dias_lista)

    # Volver a tupla
    dias_mod = tuple(dias_lista)
    print("De nuevo tupla:", dias_mod)

    # Desempaquetado
    lunes, martes, miercoles, *resto = dias_mod
    print("Desempaquetado:", lunes, martes, miercoles, "| resto:", resto)

if __name__ == "__main__":
    demo_tuplas()
