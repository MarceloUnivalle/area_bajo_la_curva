import ctypes
import time
from numpy import ctypeslib as npct

LIB = "./area_bajo_la_curva.so"
lib = npct.load_library(LIB, ".")
area = lib.area
area.restype = ctypes.c_double
area.argtypes = []


def main():
    inicio = time.time()
    print(f"El Area es: {area()}")
    fin = time.time()
    print(f"Tiempo de Ejecucion: {fin - inicio}")


if __name__ == "__main__":
    main()
