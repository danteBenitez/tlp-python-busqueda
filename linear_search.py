from typing import TypeVar

T = TypeVar('T')

def linear_search(lst: list[T], target: T) -> int:
    """
        Busca el elemento `target` en la lista `lst` y devuelve su índice si lo encuentra.

        :param lst: Lista en la que se buscará el elemento.
        :type list[T]

        :param target: Elemento a buscar en la lista.
        :type T

        :return: Índice del elemento `target` en la lista `lst` si lo encuentra, -1 en caso contrario.
    """
    # Por cada elemento en la lista...
    for i, elem in enumerate(lst):
        # Si el elemento es igual al objetivo...
        if elem == target:
            # Devolver el índice del elemento.
            return i
    # Por convención, retornamos -1 cuando no se encuentra.
    return -1

if __name__ == "__main__":
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    assert linear_search([], 1) == -1
    assert linear_search([1], 1) == 0
    assert linear_search([1], 2) == -1

    print("Todos los casos de prueba han pasado.")