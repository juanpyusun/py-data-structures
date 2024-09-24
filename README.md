# Definiciones de mediciones de complejidad temporal
- **Big-Ω(omega):** El mejor caso posible
- **Big-Θ(theta):** El caso promedio
- **Big-O:** El peor caso posible

# Mediciones comunes de complejidad temporal
- `O(1)`: Tiempo constante. No depende del tamaño de la entrada.
- `O(log n)`: Tiempo logarítmico. Crece lentamente a medida que aumenta el tamaño de la entrada. Comun en la busqueda binaria (DIVIDE Y VENCERAS!)
- `O(n)`: Tiempo lineal. Crece en proporción directa al tamaño de la entrada.
- `O(n log n)`: Tiempo lineal-logarítmico. Común en algoritmos de ordenamiento eficientes como Merge Sort y Quick Sort.
- `O(n²)`: Tiempo cuadrático. Común en algoritmos de ordenamiento de comparación simples como Bubble Sort y Selection Sort.
- `O(2^n)`: Tiempo exponencial. Crece muy rápidamente con el tamaño de la entrada. Común en problemas de fuerza bruta como el problema de la mochila.
- `O(n!)`: Tiempo factorial. Común en problemas de permutación, como el problema del vendedor viajero (TSP).

# Definiciones de mediciones de complejidad espacial
- **Big-Ω(omega):** cota inferior para la cantidad de espacio que un algoritmo puede requerir
- **Big-Θ(theta):** el algoritmo requiere un espacio que crece de manera proporcional tanto en el mejor como en el peor caso
- **Big-O:** cota superior para la cantidad de espacio que un algoritmo puede requerir

***
***

# Lista
- espacios contiguos de memoria
- indice en sus elementos

# Linked List (LL)
- Se compone de dos apuntadores y los nodos conectados
- no tienen indice los elementos
- Un nodo se compone de valor y hacia donde esta apuntando, por ejemplor, un diccionario de dos valores: `{"value": x, "next": None}`, entonces LL seria un conjunto de diccionarios anidados
- no estan necesariamente acomodados en espacios contiguos de memoria
- tiene un apuntador a los nodos de la `head` y la `Tail`
- cada nodo apunta desde la `head`, hasta el siguientre nodo, asi hasta la `Tail`, es decir, de un nodo a otros solo lo conoce el nodo anterior
- el nodo de la `Tail` apunta a `None`

# LL and Big-O
- **Añadir un elemento en la** `Tail`
  - `O(1)`
  - El ultimo elemento que apuntaba a `None`, ahora apuntara al nuevo elemento, y este apuntara a `None`, al igual que la `Tail` apuntara a este ultimo nodo.
- **Quitar un elemento en la** `Tail`
  - `O(n)`
  - Toca ir desde la `head` para saber el apuntador hacia la `Tail`, por lo que toca recorrer los n elementos
- **Añadir un elemento en la** `Head`
  - `O(1)`
  - dado que `head`apunta al primer nodo, entonces el nuevo nodo copia esa referencia y `Head` tomara la referencia del nuevo nodo
- **Quitar un elemento en la** `Head`
  - `O(1)`
  - `Head` tomara la referencia al segundo nodo del nodo que se desea eliminar
- **Añadir un elemento en otro punto i**
  - `O(n)`
  - Se itera desde `Head` hasta `i`, el nodo en esa posicion le pasa la referencia del siguiente nodo al nuevo, y este de la posicion `i` tomara la referencia del nuevo
  
- **Quitar un elemento en otro punto i**
  - `O(n)`
  - Se itera desde `Head` hasta `i`, el nodo en esa posicion le pasa la referencia del siguiente nodo al de la posicion `i-1`, y este de la posicion `i` tomara la referencia del nuevo y el nodo removido retomara su referencia a  `None`

- **Buscar un elemento**
  - `O(n)`
  - Se debe iterar de `Head` a `Tail` por el elemento deseado  

- **Indexar un elemento**
  - `O(n)`
  - Se debe iterar de `Head` a `Tail` por el elemento deseado, a diferencia de las listas que se accede al elemento a traves del indice lo cual seria una complejidad constante

# Resumen de Complejidad temporal y estructuras lineales - Tabla comparativa

| Operations | Description | LIST | LL | DLL | Stack | Queue |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| append | add tail | `O(1)` | `O(1)` | `O(1)` | `O(1)` | `O(1)` |
| pop | remove tail | `O(1)` | `O(n)` | `O(1)` | `O(1)` | `O(n)` |
| prepend | add head | `O(n)` | `O(1)` | `O(1)` | `O(n)` | `O(n)` |
| pop first | remove head  | `O(n)` | `O(1)` | `O(1)` | `O(n)` | `O(1)` |
| insert | add i | `O(n)` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |
| remove | remove i | `O(n)` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |
| Lookup by index | - | `O(1)` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |
| Lookup by Value | - | `O(n)` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |