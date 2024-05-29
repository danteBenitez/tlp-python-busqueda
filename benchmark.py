import time
from linear_search import linear_search
from binary_search import binary_search_asc

LIST = [i for i in range(1_000_000)]
ELEMENTS = [(LIST, 10)]

def benchmark(fns: list[callable], args):
    """
    Ejecuta una serie de funciones y mide el tiempo que tarda en ejecutarse cada una.
    """
    for fn in fns:
        start = time.perf_counter()
        fn(*args)
        print(f"{fn.__name__} se ejecutó en {time.perf_counter() - start} segundos")

for arg in ELEMENTS:
    benchmark([linear_search, binary_search_asc], arg)