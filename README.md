# Investigación sobre algoritmos de búsqueda

## Búsqueda lineal

La búsqueda linal es un algoritmo que puede utilizarse para encontrar un elemento en una lista, sin importar el orden de sus elementos. Para ello, recorre la lista de principio a fin, y va comparando cada valor con aquel que se busca.

### Requisitos:

- La lista debe tener elementos comparables con aquel que buscamos.
- *No* es necesario que la lista esté ordenada.

### Complejidad

La búsqueda lineal realiza una cantidad fija de operaciones *por cada elemento de la lista*. En consecuencia, su complejidad es lineal, es decir, O(n), donde n es la cantidad de elementos en la lista.

### Ejemplo de implementación en Python:

- Puede ejecutarse y probarse una implementación de búsqueda linal ejecutando:

```bash
$ python3 linear_search.py
```

## Búsqueda binaria

La búsqueda binaria es un algoritmo de búsqueda cuyo requisito principal es que la lista *debe estar ordenada* según un criterio de ordenación conocido. Este hecho es aprovechado por el algoritmo para recortar la lista de búsqueda a la mitad en cada iteración, reduciendo las comparaciones necesarias para encontrar un elemento.

### Requisitos:

- La lista debe contener elementos comparables con aquel que buscamos.
- La lista debe estar ordenada según un criterio de ordenación conocido.

### Complejidad

Por cada iteración, la búsqueda binaria reduce a la mitad la cantidad de elementos a considerar. Por ejemplo, para buscar en una lista de 4 elementos requiere de 2 comparaciones, en una lista de 8 elementos requiere de 3 comparaciones, y así sucesivamente. Puede verse, entonces, que son necesarias log_2(n) comparaciones para una lista de n elementos. En consecuencia, la complejidad de la búsqueda binaria es logarítmica, es decir, O(log n).

### Ejemplo de implementación en Python:

- Puede ejecutarse y probarse una implementación de búsqueda binaria ejecutando:

```bash
$ python3 binary_search.py
```

## Comparación entre los algoritmos

- Puede ejecutar un script que compare ambos algoritmos en cuanto a su tiempo de ejecución, ejecutando:

```bash
$ python3 benchmark.py
```