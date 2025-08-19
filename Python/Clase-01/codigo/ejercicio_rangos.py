# Clase 1 - Rangos

def h(t):
    print("\n" + "*"*60)
    print(t)
    print("*"*60)

def demo_rangos():
    h("RANGOS - FOR, STEP Y LISTAS")

    print("range(5):", list(range(5)))                # 0..4
    print("range(2, 7):", list(range(2, 7)))          # 2..6
    print("range(0, 10, 2):", list(range(0, 10, 2)))  # pares

    print("Recorriendo range(3):")
    for i in range(3):
        print(" i ->", i)

    numeros = list(range(1, 11))  # 1..10
    print("numeros:", numeros)
    print("numeros[2:7]:", numeros[2:7])
    print("numeros[-3:]:", numeros[-3:])

if __name__ == "__main__":
    demo_rangos()
