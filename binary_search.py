from typing import TypeVar

T = TypeVar('T')

def binary_search_asc(lst: list[T], target: T) -> int:
    """
        Busca el elemento `target` en la lista `lst` y devuelve su índice si lo encuentra.

        :param lst: Lista en la que se buscará el elemento. *La lista debe estar ordenada de menor a mayor*.
        :type list[T]

        :param target: Elemento a buscar en la lista.
        :type T

        :return: Índice del elemento `target` en la lista `lst` si lo encuentra, -1 en caso contrario.
    """
    # Comenzamos analizando toda la lista, por lo que
    # el índice de inicio es cero y el final es length - 1
    start = 0
    end = len(lst) - 1

    # Mientras que la sublista que analicemos tenga a lo sumo
    # un elemento...
    while start <= end:
        # Obtenemos el índice de la mitad de la sublista
        middle_index = start + (end - start) // 2

        # Obtenemos el valor que corresponde a tal índice
        middle = lst[middle_index]

        # Si la mitad es mayor al que buscamos, significa
        # que el elemento debe estar a la izquierda del centro
        if middle > target:
            # Entonces cambiamos end para reflejarlo
            end = middle_index - 1

        # Si el valor central es menor al que buscamos, significa
        # que el elemento debe estar a la derecha del centro
        elif middle < target:
            # Entonces cambiamos end para reflejarlo
            start = middle_index + 1
        else:
            # Si llegamos hasta aquí, middle == target 
            # y hemos encontrado el valor buscado.
            # Retornamos el índice correspondiente
            return middle_index

    # Si llegamos hasta aquí, la sublista ha quedado vacía
    # sin encontrar el elemento, por lo que retornamos -1
    return - 1

if __name__ == "__main__":
    assert binary_search_asc([1, 2, 3, 4, 5], 3) == 2
    assert binary_search_asc([1, 2, 3, 4, 5], 6) == -1
    assert binary_search_asc([], 1) == -1
    assert binary_search_asc([1], 1) == 0
    assert binary_search_asc([1], 2) == -1
    assert binary_search_asc([1, 2, 3, 4, 5], 3) == 2
    assert binary_search_asc([1, 2, 3, 4, 5], 6) == -1
    assert binary_search_asc([0, 1, 2, 3, 4, 5, 6, 7, 8], 9) == -1
    assert binary_search_asc([1, 3, 5, 7, 9], 3) == 1
    assert binary_search_asc([1, 3, 5, 7, 9], 7) == 3
    assert binary_search_asc([1, 3, 5, 7, 9], 9) == 4
    assert binary_search_asc([1, 3, 5, 7, 9], 2) == -1
    assert binary_search_asc([1, 3, 5, 7, 9], 6) == -1
    assert binary_search_asc([1, 3, 5, 7, 9], 10) == -1
    assert binary_search_asc([], 5) == -1
    assert binary_search_asc([2], 2) == 0
    assert binary_search_asc([2], 1) == -1
    assert binary_search_asc([2], 3) == -1

    print("Todos los casos de prueba han pasado.")