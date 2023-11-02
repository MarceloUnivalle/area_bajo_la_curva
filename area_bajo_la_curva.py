import math
import time

MAX_RECT = 9000000
LIM_BAJ = 0
LIM_ALT = 2


def funcion(x):
    f1 = math.sin(x)
    f2 = math.cos(x)
    return f1**3 + f2**3


def main():
    base = (LIM_ALT - LIM_BAJ) / MAX_RECT
    hbase = base / 2.0
    area = 0.0
    inicio = time.time()

    for i in range(MAX_RECT):
        area += base * funcion(i / MAX_RECT + hbase)

    fin = time.time()
    print(f"El Area es: {area}")
    print(f"Tiempo de Ejecucion: {fin - inicio}")


if __name__ == "__main__":
    main()
