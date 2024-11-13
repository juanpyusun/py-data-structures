# Estructura de datos y algoritmos avanzados

## Índice
- [Estructura de datos y algoritmos avanzados](#estructura-de-datos-y-algoritmos-avanzados)
  - [Índice](#índice)
  - [Definiciones de mediciones de complejidad temporal](#definiciones-de-mediciones-de-complejidad-temporal)
  - [Mediciones comunes de complejidad temporal](#mediciones-comunes-de-complejidad-temporal)
  - [Definiciones de mediciones de complejidad espacial](#definiciones-de-mediciones-de-complejidad-espacial)
  - [List](#list)
    - [L and Big-O](#l-and-big-o)
  - [Linked List (LL)](#linked-list-ll)
    - [LL and Big-O](#ll-and-big-o)
  - [Doubly Linked List (DLL)](#doubly-linked-list-dll)
    - [DLL and Big-O](#dll-and-big-o)
  - [Stack (S)](#stack-s)
    - [S and Big-O](#s-and-big-o)
  - [Queue (Q)](#queue-q)
    - [Q and Big-O](#q-and-big-o)
  - [Resumen de Complejidad temporal y estructuras lineales - Tabla comparativa](#resumen-de-complejidad-temporal-y-estructuras-lineales---tabla-comparativa)
    - [Notas sobre la Tabla](#notas-sobre-la-tabla)
  - [Binary Search Trees (BST)](#binary-search-trees-bst)
    - [BST and Big-O](#bst-and-big-o)
  - [Otro tipo de arboles](#otro-tipo-de-arboles)
  - [Hash Table (HT)](#hash-table-ht)
    - [HT and Big-O](#ht-and-big-o)
  - [Graph (G)](#graph-g)
    - [G and Big-O](#g-and-big-o)
  - [Heap](#heap)
    - [Heap and Big-O](#heap-and-big-o)
  - [Resumen de Complejidad Temporal y Estructuras No Lineales - Tabla Comparativa](#resumen-de-complejidad-temporal-y-estructuras-no-lineales---tabla-comparativa)
    - [Consideraciones Adicionales](#consideraciones-adicionales)
  - [Recursividad](#recursividad)
    - [Call stack](#call-stack)
  - [Breadth First Search (BFS)](#breadth-first-search-bfs)
  - [Depth First Search (DFS)](#depth-first-search-dfs)
  - [Metodos de Ordenamiento](#metodos-de-ordenamiento)
    - [1. Bubble Sort](#1-bubble-sort)
      - [Resumen:](#resumen)
      - [Características:](#características)
    - [2. Selection Sort](#2-selection-sort)
      - [Resumen:](#resumen-1)
      - [Características:](#características-1)
    - [3. Insertion Sort](#3-insertion-sort)
      - [Resumen:](#resumen-2)
      - [Características:](#características-2)
    - [4. Merge Sort](#4-merge-sort)
      - [Resumen:](#resumen-3)
      - [Características:](#características-3)
    - [5. Quick Sort](#5-quick-sort)
      - [Resumen:](#resumen-4)
      - [Características:](#características-4)
    - [Tabla Comparativa de Complejidad](#tabla-comparativa-de-complejidad)
  - [Resumen sobre Programación Dinámica](#resumen-sobre-programación-dinámica)
    - [1. Overlapping Subproblems](#1-overlapping-subproblems)
    - [2. Optimized Substructure](#2-optimized-substructure)
    - [3. Caso - Fibonacci Sequence](#3-caso---fibonacci-sequence)
    - [4. Memoization](#4-memoization)
    - [5. Bottom Up](#5-bottom-up)


***
***

## Definiciones de mediciones de complejidad temporal
- **Big-Ω(omega):** El mejor caso posible
- **Big-Θ(theta):** El caso promedio
- **Big-O:** El peor caso posible

## Mediciones comunes de complejidad temporal
- `O(1)`: Tiempo constante. No depende del tamaño de la entrada.
- `O(log n)`: Tiempo logarítmico. Crece lentamente a medida que aumenta el tamaño de la entrada. Comun en la busqueda binaria (DIVIDE Y VENCERAS!)
- `O(n)`: Tiempo lineal. Crece en proporción directa al tamaño de la entrada.
- `O(n log n)`: Tiempo lineal-logarítmico. Común en algoritmos de ordenamiento eficientes como Merge Sort y Quick Sort.
- `O(n²)`: Tiempo cuadrático. Común en algoritmos de ordenamiento de comparación simples como Bubble Sort y Selection Sort.
- `O(2^n)`: Tiempo exponencial. Crece muy rápidamente con el tamaño de la entrada. Común en problemas de fuerza bruta como el problema de la mochila.
- `O(n!)`: Tiempo factorial. Común en problemas de permutación, como el problema del vendedor viajero (TSP).

## Definiciones de mediciones de complejidad espacial
- **Big-Ω(omega):** cota inferior para la cantidad de espacio que un algoritmo puede requerir
- **Big-Θ(theta):** el algoritmo requiere un espacio que crece de manera proporcional tanto en el mejor como en el peor caso
- **Big-O:** cota superior para la cantidad de espacio que un algoritmo puede requerir

***
***

## Array
- **Estructura**: Espacios contiguos de memoria, similar a listas, pero generalmente de un tipo específico (homogéneas).
- **Acceso**: Índice en sus elementos.

## List
- **Estructura**: Espacios contiguos de memoria.
- **Acceso**: Índice en sus elementos.

### L and Big-O
- **Acceso a Elementos**
  - **Complejidad**: `O(1)`
  - Descripción: Las listas permiten acceso directo a elementos utilizando índices, lo que resulta en un tiempo constante para acceder a cualquier elemento.

- **Añadir un Elemento al Final**
  - **Complejidad**: `O(1)` (Amortizado)
  - Descripción: La operación de añadir un elemento al final de la lista es generalmente constante, aunque puede ser `O(n)` si es necesario redimensionar el arreglo subyacente.

- **Eliminar un Elemento del Final**
  - **Complejidad**: `O(1)`
  - Descripción: Al eliminar el último elemento, no es necesario mover otros elementos, lo que resulta en un tiempo constante.

- **Añadir un Elemento al Inicio**
  - **Complejidad**: `O(n)`
  - Descripción: Para añadir un elemento al inicio de una lista, todos los elementos existentes deben ser desplazados, lo que requiere tiempo lineal.

- **Eliminar un Elemento del Inicio**
  - **Complejidad**: `O(n)`
  - Descripción: Similar a la operación de añadir, al eliminar el primer elemento, todos los elementos restantes deben ser desplazados.

- **Buscar un Elemento**
  - **Complejidad**: `O(n)`
  - Descripción: La búsqueda de un elemento específico requiere iterar sobre todos los elementos, lo que resulta en un tiempo lineal.

- **Indexar un Elemento**
  - **Complejidad**: `O(1)`
  - Descripción: Acceder a un elemento mediante su índice es una operación constante, ya que las listas están diseñadas para permitir acceso directo.

- **Insertar un Elemento en el Medio**
  - **Complejidad**: `O(n)`
  - Descripción: Al insertar un elemento en una posición intermedia, todos los elementos a partir de esa posición deben ser desplazados, lo que requiere tiempo lineal.

- **Eliminar un Elemento en el Medio**
  - **Complejidad**: `O(n)`
  - Descripción: Al eliminar un elemento en una posición intermedia, todos los elementos posteriores deben ser desplazados, lo que también requiere tiempo lineal.

- **Contar el Número de Elementos**
  - **Complejidad**: `O(1)`
  - Descripción: Si se mantiene un contador de longitud, contar el número de elementos en la lista es una operación constante.

- **Reversar la Lista**
  - **Complejidad**: `O(n)`
  - Descripción: La operación de reversar requiere iterar sobre todos los elementos para cambiar sus enlaces, lo que resulta en un tiempo lineal.

- **Copiar la Lista**
  - **Complejidad**: `O(n)`
  - Descripción: Al crear una copia de la lista, cada elemento debe ser copiado, lo que requiere tiempo lineal.

- **Eliminar Duplicados**
  - **Complejidad**: `O(n^2)`
  - Descripción: Dependiendo de la implementación, la eliminación de duplicados puede requerir iterar sobre la lista para cada elemento, lo que puede resultar en un tiempo cuadrático.

- **Concatenar Listas**
  - **Complejidad**: `O(n)`
  - Descripción: La concatenación de dos listas implica copiar todos los elementos de una lista a otra, lo que requiere tiempo lineal.

- **Filtrar Elementos**
  - **Complejidad**: `O(n)`
  - Descripción: Filtrar elementos de una lista implica iterar sobre todos los elementos y aplicar una condición, resultando en un tiempo lineal.

## Linked List (LL)
- **Estructura**: Se compone de dos apuntadores y nodos conectados.
- **Acceso**: No tienen índice los elementos.
- **Nodo**: Un nodo se compone de valor y hacia donde está apuntando, por ejemplo, un diccionario de dos valores: `{"value": x, "next": None}`. Entonces, LL sería un conjunto de diccionarios anidados.
- **Memoria**: No están necesariamente acomodados en espacios contiguos de memoria.
- **Apuntadores**: Tiene un apuntador a los nodos de la `head` y la `Tail`.
- **Conexiones**: Cada nodo apunta desde la `head`, hasta el siguiente nodo, así hasta la `Tail`, es decir, de un nodo a otro solo lo conoce el nodo anterior.
- **Tail**: El nodo de la `Tail` apunta a `None`.

### LL and Big-O
- **Añadir un elemento en la `Tail`**
  - **Complejidad**: `O(1)`
  - Descripción: El último elemento que apuntaba a `None`, ahora apuntará al nuevo elemento, y este apuntará a `None`, al igual que la `Tail` apuntará a este último nodo.
  
- **Quitar un elemento en la `Tail`**
  - **Complejidad**: `O(n)`
  - Descripción: Toca ir desde la `head` para saber el apuntador hacia la `Tail`, por lo que toca recorrer los n elementos.
  
- **Añadir un elemento en la `Head`**
  - **Complejidad**: `O(1)`
  - Descripción: Dado que `head` apunta al primer nodo, entonces el nuevo nodo copia esa referencia y `Head` tomará la referencia del nuevo nodo.
  
- **Quitar un elemento en la `Head`**
  - **Complejidad**: `O(1)`
  - Descripción: `Head` tomará la referencia al segundo nodo del nodo que se desea eliminar.
  
- **Añadir un elemento en otro punto i**
  - **Complejidad**: `O(n)`
  - Descripción: Se itera desde `Head` hasta `i`, el nodo en esa posición le pasa la referencia del siguiente nodo al nuevo, y este de la posición `i` tomará la referencia del nuevo.
  
- **Quitar un elemento en otro punto i**
  - **Complejidad**: `O(n)`
  - Descripción: Se itera desde `Head` hasta `i`, el nodo en esa posición le pasa la referencia del siguiente nodo al de la posición `i-1`, y este de la posición `i` tomará la referencia del nuevo y el nodo removido retomará su referencia a `None`.

- **Buscar un elemento**
  - **Complejidad**: `O(n)`
  - Descripción: Se debe iterar de `Head` a `Tail` por el elemento deseado.  

- **Indexar un elemento**
  - **Complejidad**: `O(n)`
  - Descripción: Se debe iterar de `Head` a `Tail` por el elemento deseado, a diferencia de las listas que se accede al elemento a través del índice, lo cual sería una complejidad constante.

## Doubly Linked List (DLL)
- **Descripción**: Una lista doblemente enlazada se compone de nodos donde cada nodo tiene tres partes: un valor, un apuntador al siguiente nodo (`next`) y un apuntador al nodo anterior (`prev`).
- **Memoria**: Cada nodo ocupa más espacio que un nodo de una lista enlazada simple debido a los dos apuntadores.

### DLL and Big-O
- **Añadir un Elemento al Final**
  - **Complejidad**: `O(1)`
  - **Descripción**: Se puede añadir un nuevo nodo al final actualizando el apuntador de la `Tail` y haciendo que el nuevo nodo apunte a `None`.

- **Eliminar un Elemento del Final**
  - **Complejidad**: `O(1)`
  - **Descripción**: Se puede eliminar el nodo `Tail` actualizando el apuntador de la `Tail` al nodo anterior y liberando el nodo eliminado.

- **Añadir un Elemento al Inicio**
  - **Complejidad**: `O(1)`
  - **Descripción**: Similar a añadir al final, se puede añadir un nuevo nodo al inicio actualizando el apuntador de la `Head`.

- **Eliminar un Elemento del Inicio**
  - **Complejidad**: `O(1)`
  - **Descripción**: Al eliminar el primer nodo, se actualiza el apuntador de la `Head` al siguiente nodo.

- **Buscar un Elemento**
  - **Complejidad**: `O(n)`
  - **Descripción**: La búsqueda de un elemento requiere iterar a través de la lista desde la `Head` hasta la `Tail`, o viceversa, lo que resulta en un tiempo lineal.

- **Indexar un Elemento**
  - **Complejidad**: `O(n)`
  - **Descripción**: Acceder a un elemento por índice implica recorrer la lista, lo que requiere tiempo lineal.

- **Insertar un Elemento en el Medio**
  - **Complejidad**: `O(n)`
  - **Descripción**: Para insertar un nodo en una posición específica, primero se debe recorrer la lista para llegar a esa posición, y luego actualizar los apuntadores del nodo anterior y el nuevo nodo.

- **Eliminar un Elemento en el Medio**
  - **Complejidad**: `O(n)`
  - **Descripción**: Al igual que en la inserción, se debe recorrer la lista para encontrar el nodo a eliminar y luego actualizar los apuntadores del nodo anterior y el siguiente.

- **Contar el Número de Elementos**
  - **Complejidad**: `O(n)` (si no se mantiene un contador)
  - **Descripción**: Si no se mantiene un contador de longitud, contar los elementos requiere iterar a través de toda la lista.

- **Reversar la Lista**
  - **Complejidad**: `O(n)`
  - **Descripción**: Reversar una lista doblemente enlazada implica recorrer la lista y cambiar los apuntadores `next` y `prev`, lo que requiere tiempo lineal.

- **Eliminar Duplicados**
  - **Complejidad**: `O(n)`
  - **Descripción**: Se puede utilizar un conjunto para rastrear duplicados mientras se itera a través de la lista, resultando en una complejidad lineal.

- **Concatenar Dos Listas**
  - **Complejidad**: `O(1)`
  - **Descripción**: Al conectar la `Tail` de la primera lista al `Head` de la segunda lista y actualizar los apuntadores adecuadamente, la concatenación se puede realizar en tiempo constante.

- **Filtrar Elementos**
  - **Complejidad**: `O(n)`
  - **Descripción**: Filtrar elementos de una lista implica iterar a través de todos los nodos y aplicar una condición, resultando en un tiempo lineal.

## Stack (S)
- **Descripción**: Una estructura de datos que sigue el principio LIFO (Last In, First Out), donde el último elemento añadido es el primero en ser retirado.
- **Implementación**: Puede ser implementado utilizando arreglos o listas enlazadas.

### S and Big-O
- **Push (Añadir un Elemento)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Añadir un elemento a la parte superior de la pila es una operación constante.

- **Pop (Eliminar un Elemento)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Retirar el elemento de la parte superior de la pila también es una operación constante.

- **Peek (Obtener el Elemento Superior)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Acceder al elemento en la parte superior sin retirarlo es una operación constante.

- **IsEmpty (Verificar si está Vacío)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Verificar si la pila está vacía es una operación constante.

- **Size (Contar Elementos)**
  - **Complejidad**: `O(1)` (si se mantiene un contador)
  - **Descripción**: Si se mantiene un contador de elementos, contar el número de elementos es una operación constante.

## Queue (Q)
- **Descripción**: Una estructura de datos que sigue el principio FIFO (First In, First Out), donde el primer elemento añadido es el primero en ser retirado.
- **Implementación**: Puede ser implementada utilizando arreglos o listas enlazadas.

### Q and Big-O
- **Enqueue (Añadir un Elemento)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Añadir un elemento al final de la cola es una operación constante.

- **Dequeue (Eliminar un Elemento)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Retirar el elemento al frente de la cola también es una operación constante.

- **Peek (Obtener el Elemento Frontal)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Acceder al elemento en la parte frontal sin retirarlo es una operación constante.

- **IsEmpty (Verificar si está Vacío)**
  - **Complejidad**: `O(1)`
  - **Descripción**: Verificar si la cola está vacía es una operación constante.

- **Size (Contar Elementos)**
  - **Complejidad**: `O(1)` (si se mantiene un contador)
  - **Descripción**: Si se mantiene un contador de elementos, contar el número de elementos en la cola es una operación constante.

## Resumen de Complejidad temporal y estructuras lineales - Tabla comparativa
| **Operation**       | **Description**                         | **Array List** | **Linked List (LL)** | **Doubly Linked List (DLL)** | **Stack** | **Queue** |
| :------------------ | :-------------------------------------: | :------------: | :------------------: | :---------------------------: | :-------: | :-------: |
| **Append**          | Add element at the tail                | `O(1)`        | `O(1)`               | `O(1)`                       | `O(1)`   | `O(1)`   |
| **Pop**             | Remove element at the tail             | `O(1)`        | `O(n)`               | `O(1)`                       | `O(1)`   | `O(n)`   |
| **Prepend**         | Add element at the head                | `O(n)`        | `O(1)`               | `O(1)`                       | `O(n)`   | `O(n)`   |
| **Pop First**       | Remove element at the head             | `O(n)`        | `O(1)`               | `O(1)`                       | `O(n)`   | `O(1)`   |
| **Insert**          | Add element at position `i`            | `O(n)`        | `O(n)`               | `O(n)`                       | `O(n)`   | `O(n)`   |
| **Remove**          | Remove element at position `i`         | `O(n)`        | `O(n)`               | `O(n)`                       | `O(n)`   | `O(n)`   |
| **Lookup by Index** | Access element by index                 | `O(1)`        | `O(n)`               | `O(n)`                       | `O(n)`   | `O(n)`   |
| **Lookup by Value** | Find element by value                  | `O(n)`        | `O(n)`               | `O(n)`                       | `O(n)`   | `O(n)`   |
| **Peek**            | View element at the top (stack/queue)  | N/A           | N/A                  | N/A                          | `O(1)`   | `O(1)`   |
| **Enqueue**         | Add element at the rear (queue)        | N/A           | N/A                  | N/A                          | N/A      | `O(1)`   |
| **Dequeue**         | Remove element from the front (queue)   | N/A           | N/A                  | N/A                          | N/A      | `O(1)`   |

### Notas sobre la Tabla
- La complejidad de las operaciones puede variar dependiendo de la implementación específica.
- Para las listas, `N/A` indica que la operación no es aplicable.

***
***

## Binary Search Trees (BST)
- **Estructura**: Se compone de nodos conectados de manera jerárquica mediante relaciones de padre-hijo.
- **Nodo**: Un nodo se compone de un valor y sus hijos. En un árbol binario, por ejemplo, un nodo tiene un valor y dos apuntadores: `{"value": x, "left": None, "right": None}`.
- **Acceso**: Los elementos no tienen índices como en una lista.
- **Padre (Parent)**: Un nodo que tiene uno o más nodos descendientes se llama "padre". En un árbol, cada nodo puede tener un solo padre, excepto la raíz, que no tiene ninguno.
- **Hijo (Child)**: Un nodo que es descendiente directo de otro nodo se llama "hijo". En un árbol, cada nodo puede tener múltiples hijos, pero solo un padre.
- **Hermanos (Siblings)**: Dos o más nodos que comparten el mismo padre en un árbol se denominan "hermanos". Por ejemplo, en un árbol binario, si un nodo tiene dos hijos, esos hijos son hermanos entre sí.
- **Memoria**: Los nodos no están necesariamente acomodados en espacios contiguos de memoria.
- **Raíz (Root)**: Es el nodo superior que no tiene padre, siendo el punto de partida para el árbol.
- **Hojas (Leaves)**: Nodos que no tienen hijos.
- **Conexiones**: Cada nodo apunta a sus hijos, y en un árbol binario, tiene como máximo dos hijos: `left` y `right`.
- **Subárboles**: Un nodo y sus descendientes forman un subárbol, que puede tratarse como un árbol independiente.
- **Árbol binario completo (Full Binary Tree)**: Cada nodo tiene exactamente 0 o 2 hijos; es decir, ningún nodo tiene un solo hijo.
- **Árbol binario perfecto (Perfect Binary Tree)**: Todos los nodos internos tienen exactamente 2 hijos, y todas las hojas están al mismo nivel.
- **Árbol completo (Complete Binary Tree)**: Todos los niveles, excepto posiblemente el último, están completamente llenos, y los nodos en el último nivel se colocan de manera consecutiva de izquierda a derecha.

### BST and Big-O
- **Añadir un nodo**
  - **Complejidad**: `O(log n)` (árbol balanceado), `O(n)` (peor caso en árbol desbalanceado)
  - **Descripción**: Se compara el valor del nuevo nodo con los valores existentes en el árbol y se inserta en el lugar adecuado, moviéndose por el árbol de manera recursiva o iterativa.
  
- **Eliminar un nodo**
  - **Complejidad**: `O(log n)` (árbol balanceado), `O(n)` (peor caso en árbol desbalanceado)
  - **Descripción**: Se localiza el nodo a eliminar, luego se ajustan las referencias de los nodos adyacentes, y en algunos casos, se reorganiza el árbol para mantener el equilibrio.
  
- **Buscar un nodo**
  - **Complejidad**: `O(log n)` (árbol balanceado), `O(n)` (peor caso en árbol desbalanceado)
  - **Descripción**: Se compara el valor del nodo objetivo con los nodos del árbol, dividiendo el espacio de búsqueda en mitades hasta encontrar el nodo deseado.

- **Recorrer el árbol**
  - **Complejidad**: `O(n)`
  - **Descripción**: Se recorren todos los nodos de un árbol en distintos órdenes: preorden, enorden o postorden, visitando cada nodo una vez.

- **Altura del árbol**
  - **Complejidad**: `O(n)`
  - **Descripción**: Para calcular la altura de un árbol, se debe recorrer cada rama hasta la hoja más profunda.

- **Balancear el árbol**
  - **Complejidad**: `O(n log n)` en promedio.
  - **Descripción**: Si el árbol se desbalancea (por ejemplo, un árbol binario de búsqueda se convierte en una lista), es necesario realizar una serie de rotaciones o reestructuraciones para mantener un balance óptimo.

## Otro tipo de arboles
- **Árbol Binario**: Cada nodo tiene un máximo de dos hijos.
- **Árbol No Binario**: Cada nodo no tiene un máximo de hijos.
- **Árbol Binario de Búsqueda (BST)**: Es un árbol binario con la propiedad que para cada nodo, los valores de los nodos en el subárbol izquierdo son menores y los del subárbol derecho son mayores.
- **Árbol AVL**: Es un BST auto-balanceado, que mantiene una altura mínima para garantizar operaciones eficientes.

## Hash Table (HT)

- **Estructura**: Utiliza un mecanismo de dispersión (hashing) para almacenar pares clave-valor.
- **Acceso**: Los elementos se acceden mediante una clave única en lugar de un índice o posición.
- **Elemento**: Cada entrada en la tabla hash se compone de una clave y un valor: `{"key": x, "value": y}`. Se almacena el valor en un bucket basado en el hash de la clave.
- **Memoria**: Las entradas no se almacenan necesariamente en posiciones contiguas en memoria.
- **Colisiones**: Si dos claves tienen el mismo hash, se puede utilizar manejo de colisiones, como:
  - **Encadenamiento**: Utiliza listas enlazadas para almacenar múltiples elementos en el mismo bucket.
  - **Direccionamiento Abierto**: Reubica datos en la tabla para encontrar un lugar libre.
- **Clave Única**: Cada valor se asocia a una clave única, lo que permite acceder, insertar o eliminar elementos en tiempo constante promedio.
- **Búsqueda**: Se basa en el hash de la clave, lo que generalmente permite un acceso rápido.

### HT and Big-O

- **Añadir un elemento**
  - **Complejidad**: `O(1)` en promedio, `O(n)` en el peor caso.
  - **Descripción**: Se calcula el hash de la clave y se almacena el valor en el bucket correspondiente. En caso de colisión, puede necesitar más operaciones para encontrar un lugar libre o añadir el elemento a la lista vinculada.

- **Quitar un elemento**
  - **Complejidad**: `O(1)` en promedio, `O(n)` en el peor caso.
  - **Descripción**: Se calcula el hash de la clave, se accede al bucket correspondiente, y el elemento se elimina, manejando colisiones si es necesario.

- **Buscar un elemento**
  - **Complejidad**: `O(1)` en promedio, `O(n)` en el peor caso.
  - **Descripción**: Se calcula el hash de la clave para acceder al bucket correspondiente y se recupera el valor, buscando en caso de colisiones.

- **Acceder a un elemento**
  - **Complejidad**: `O(1)` en promedio, `O(n)` en el peor caso.
  - **Descripción**: Utiliza el hash de la clave para acceder directamente al valor almacenado.

- **Manejo de colisiones**
  - **Complejidad**: Depende del método utilizado, como encadenamiento o direccionamiento abierto.
  - **Descripción**: Si dos claves generan el mismo hash, el hashtable debe manejar la colisión. Con encadenamiento, los elementos se almacenan en una lista; con direccionamiento abierto, se busca otro lugar disponible.

- **Rehashing**
  - **Complejidad**: `O(n)`
  - **Descripción**: Cuando la tabla alcanza una cierta capacidad, puede necesitar redimensionarse y recalcular los hashes de todos los elementos existentes para redistribuirlos en una nueva tabla más grande.

- **Cargar elementos**
  - **Complejidad**: `O(1)` en promedio, `O(n)` en el peor caso.
  - **Descripción**: Los elementos se cargan eficientemente en la tabla, pero a medida que la tabla se llena, puede necesitarse rehashing para mantener la eficiencia.

## Graph (G)
- **Estructura**: Un grafo se compone de nodos (o vértices) y aristas (o conexiones) que los unen.
- **Acceso**: Los elementos (nodos) pueden ser accedidos a través de sus conexiones (aristas).
- **Nodo**: Un nodo puede ser representado como un objeto o diccionario que contiene un valor y una lista de adyacencias, por ejemplo: `{"value": x, "edges": [y, z]}`. Entonces, un grafo sería un conjunto de nodos con sus conexiones.
- **Memoria**: Los nodos no están necesariamente en espacios contiguos de memoria, y las conexiones pueden ser bidireccionales o unidireccionales.
- **Conexiones**: Cada nodo puede estar conectado a múltiples nodos, y estas conexiones son representadas por aristas.
- **Aristas**: Las aristas pueden ser ponderadas (con un costo) o no ponderadas, con direccion o bidireccionales.
- **Representacion**: Se puede representar en codigo de dos maneras:
  - **Adjacency Matrix**: Una matriz nxn donde cada fila y columna es un nodo, teniendo en cuenta la perspectiva de las filas, si A tiene conexion con B se pone 1 o el peso de esa arista, si todas las aristas son bidireccionales, se formara una matriz simetrica
  - **Adjacency List**: Un diccionario cuyo cada nodo es una llave y sus valores es una lista con los nodos asociados

### G and Big-O
- **Añadir un nodo**
  - **Complejidad**: `O(1)`
  - Descripción: Se crea un nuevo nodo y se añade a la estructura del grafo (por ejemplo, a un diccionario o lista de nodos).

- **Eliminar un nodo**
  - **Complejidad**: `O(V + E)`
  - Descripción: Es necesario eliminar todas las aristas que están conectadas a ese nodo, lo que puede requerir recorrer todos los nodos (V) y aristas (E) del grafo.

- **Añadir una arista**
  - **Complejidad**: `O(1)`
  - Descripción: Se añade una conexión entre dos nodos, lo que puede hacerse en tiempo constante si se utilizan listas o diccionarios.

- **Eliminar una arista**
  - **Complejidad**: `O(V)`
  - Descripción: Se debe encontrar la arista entre los dos nodos, lo que puede implicar iterar a través de las conexiones de uno de los nodos.

- **Buscar un nodo**
  - **Complejidad**: `O(V)`
  - Descripción: Se puede requerir recorrer todos los nodos para encontrar el nodo deseado, especialmente si no se tiene un índice.

- **Buscar una arista**
  - **Complejidad**: `O(V)`
  - Descripción: Se debe iterar a través de las conexiones de un nodo para ver si hay una arista hacia el nodo deseado.

- **Recorrer el grafo (DFS o BFS)**
  - **Complejidad**: `O(V + E)`
  - Descripción: Ambos algoritmos requieren visitar cada nodo y cada arista del grafo, por lo que la complejidad es proporcional a la suma del número de nodos y aristas.

## Heap
- **Estructura**: Un heap es una estructura de datos en forma de árbol binario que satisface la propiedad de heap, donde cada nodo es menor (min-heap) o mayor (max-heap) que sus hijos.
- **Acceso**: El acceso a los elementos se realiza a través de la raíz del árbol, que contiene el valor mínimo (en un min-heap) o máximo (en un max-heap).
- **Nodos**: Cada nodo tiene un valor y apuntadores a sus nodos hijos. Por ejemplo, un nodo puede representarse como: `{"value": x, "left": None, "right": None}`.
- **Memoria**: Generalmente se implementa usando un array o lista, donde la posición de los nodos se determina por sus índices.
- **Propiedad de Heap**: En un min-heap, el valor de cada nodo es menor o igual que el valor de sus nodos hijos; en un max-heap, el valor de cada nodo es mayor o igual que el de sus nodos hijos.

### Heap and Big-O
- **Añadir un elemento**
  - **Complejidad**: `O(log n)`
  - Descripción: Se añade el elemento al final del heap y luego se realiza un "up-heap" o "bubble-up" para mantener la propiedad de heap.

- **Eliminar el elemento raíz**
  - **Complejidad**: `O(log n)`
  - Descripción: Se elimina la raíz y se reemplaza con el último elemento, seguido de un "down-heap" o "bubble-down" para restaurar la propiedad de heap.

- **Acceder al elemento raíz**
  - **Complejidad**: `O(1)`
  - Descripción: El elemento raíz puede ser accedido directamente sin necesidad de recorrer otros elementos.

- **Buscar un elemento**
  - **Complejidad**: `O(n)`
  - Descripción: No hay una forma eficiente de buscar un elemento específico en un heap, ya que no se mantiene un orden total.

- **Construir un heap a partir de una lista**
  - **Complejidad**: `O(n)`
  - Descripción: Se puede construir un heap a partir de una lista de elementos usando el algoritmo "heapify".

## Resumen de Complejidad Temporal y Estructuras No Lineales - Tabla Comparativa
| **Operations**         | **Description**                       | **Binary Tree** | **BST (Balanced)** | **BST (Unbalanced)** | **Heap**   | **Graph (Adjacency List)** | **Graph (Adjacency Matrix)** |
| :--------------------- | :-----------------------------------: | :-------------: | :----------------: | :------------------: | :--------: | :------------------------: | :---------------------------: |
| **Insert**             | Add a node                           | `O(log n)`      | `O(log n)`        | `O(n)`               | `O(log n)` | `O(1)`                    | `O(n^2)`                     |
| **Delete**             | Remove a node                        | `O(log n)`      | `O(log n)`        | `O(n)`               | `O(log n)` | `O(E)`                    | `O(n^2)`                     |
| **Search**             | Find a node                          | `O(log n)`      | `O(log n)`        | `O(n)`               | `O(n)`    | `O(V + E)`                | `O(n^2)`                     |
| **Access Root**        | Access the root node                 | `O(1)`          | `O(1)`            | `O(1)`               | `O(1)`    | N/A                        | N/A                           |
| **Find Min/Max**       | Find the minimum/maximum value       | `O(n)`          | `O(log n)`        | `O(n)`               | `O(1)`    | N/A                        | N/A                           |
| **Traverse (DFS/BFS)** | Visit all nodes                      | `O(n)`          | `O(n)`            | `O(n)`               | `O(n)`    | `O(V + E)`                | `O(n^2)`                     |
| **Update**             | Modify a node value                  | `O(log n)`      | `O(log n)`        | `O(n)`               | `O(log n)` | `O(E)`                    | `O(n^2)`                     |
| **Is Empty**           | Check if the structure is empty      | `O(1)`          | `O(1)`            | `O(1)`               | `O(1)`    | `O(1)`                    | `O(1)`                       |
| **Clear**              | Remove all nodes                     | `O(n)`          | `O(n)`            | `O(n)`               | `O(n)`    | `O(V)`                    | `O(n^2)`                     |

### Consideraciones Adicionales
- La complejidad de las operaciones puede variar según la implementación específica de cada estructura de datos.
- Para grafos, la representación puede influir en la eficiencia de ciertas operaciones, como la búsqueda y el recorrido.

***
***

## Recursividad
La recursividad es una técnica de programación en la cual una función se llama a sí misma directa o indirectamente para resolver un problema. Esta técnica se utiliza comúnmente para dividir un problema complejo en subproblemas más simples y manejables. Cada llamada recursiva trabaja con una versión reducida del problema original hasta que se alcanza una condición base que detiene la recursión.

- **Características Clave de la Recursividad**
  - **Condición Base**: Una condición que detiene la recursión para evitar llamadas infinitas.
  - **Llamada Recursiva**: La función se llama a sí misma con argumentos modificados que acercan el problema a la condición base.

### Call stack
El call stack (pila de llamadas) es una estructura de datos utilizada por los lenguajes de programación para gestionar las llamadas a funciones y los contextos de ejecución. Cada vez que se invoca una función, se crea un nuevo marco de pila (stack frame) que contiene información sobre la función, como sus parámetros, variables locales y la dirección de retorno. Este marco se apila en la parte superior del call stack. Cuando la función termina, su marco se desapila y el control se devuelve a la función llamante.

- **Características Clave del Call Stack**
  - **LIFO (Last In, First Out)**: El último marco en entrar es el primero en salir.
  - **Gestión de Contexto**: Mantiene el contexto de ejecución de las funciones.
  - **Recursividad**: Maneja las llamadas recursivas apilando múltiples marcos de la misma función. 

## Breadth First Search (BFS)
Breadth First Search (BFS) es un algoritmo de búsqueda utilizado para explorar nodos y aristas en un grafo o árbol. Comienza en un nodo raíz y explora todos los nodos vecinos en el mismo nivel antes de avanzar a los nodos en el siguiente nivel. Este enfoque es útil para encontrar el camino más corto en grafos no ponderados y se aplica en diversas áreas como redes, inteligencia artificial y resolución de problemas.

- **Características Clave de BFS**
  - **Estrategia por Niveles**: Explora todos los nodos a una distancia `d` del nodo inicial antes de pasar a los nodos a una distancia `d+1`.
  - **Uso de Cola**: Utiliza una estructura de datos tipo cola `FIFO` para gestionar los nodos pendientes de exploración.
  - **Complejidad**: La complejidad temporal es `O(V + E)` y la complejidad espacial es `O(V)`.

## Depth First Search (DFS)
Depth First Search (DFS) es un algoritmo de búsqueda que explora un grafo o árbol empezando desde un nodo raíz y avanzando lo más profundo posible por cada rama antes de retroceder. Este enfoque se utiliza para recorrer o buscar elementos en estructuras de datos jerárquicas y es esencial en aplicaciones como la búsqueda de caminos, la topología de grafos y la resolución de problemas de laberintos.

- **Características Clave de DFS**
  - **Estrategia de Profundidad**: Explora cada rama del grafo hasta que llega a un nodo sin hijos, luego retrocede y explora otras ramas.
  - **Uso de Pila**: Se puede implementar utilizando una pila `LIFO` o de forma recursiva, donde las llamadas recursivas funcionan como una pila implícita.
  - **Complejidad**: La complejidad temporal es `O(V + E)` y la complejidad espacial es `O(V)` en su implementación recursiva.

- **Tipos de DFS**

| Tipo de Recorrido | Orden de Visita                        | Uso Común                                |
|-------------------|----------------------------------------|------------------------------------------|
| Preorden          | Nodo actual → Izquierda → Derecha      | Crear copias, serializar árboles         |
| Inorden           | Izquierda → Nodo actual → Derecha      | Obtener valores en orden ascendente (BST)|
| Postorden         | Izquierda → Derecha → Nodo actual      | Eliminar árboles, calcular alturas       |


***
***

## Metodos de Ordenamiento

A continuación se presenta un resumen de los métodos de ordenamiento más comunes, junto con sus características y casos de uso. Al final, se incluye una tabla comparativa de complejidad temporal y espacial.

### 1. Bubble Sort

#### Resumen:
El Bubble Sort es un algoritmo simple que repetidamente recorre la lista, compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada.

#### Características:
- **Complejidad Temporal**: `O(n²)` en el peor y caso promedio, O(n) en el mejor (si la lista ya está ordenada).
- **Complejidad Espacial**: `O(1)` (in-place).
- **Uso**: Poco eficiente para listas grandes, se usa más como una herramienta didáctica.

### 2. Selection Sort

#### Resumen:
El Selection Sort divide la lista en dos partes: la parte ordenada y la parte desordenada. Repetidamente selecciona el elemento más pequeño de la parte desordenada y lo mueve al final de la parte ordenada.

#### Características:
- **Complejidad Temporal**: `O(n²)` en todos los casos.
- **Complejidad Espacial**: `O(1)` (in-place).
- **Uso**: Sencillo y fácil de implementar, pero no es eficiente para listas grandes.

### 3. Insertion Sort

#### Resumen:
El Insertion Sort construye una lista ordenada de manera incremental. Toma un elemento de la lista desordenada y lo inserta en la posición correcta en la lista ordenada.

#### Características:
- **Complejidad Temporal**: `O(n²)` en el peor y caso promedio, `O(n)` en el mejor.
- **Complejidad Espacial**: `O(1)` (in-place).
- **Uso**: Eficiente para listas pequeñas o casi ordenadas.

### 4. Merge Sort

#### Resumen:
El Merge Sort es un algoritmo de ordenamiento basado en la técnica de Divide y Vencerás. Divide la lista en mitades, ordena cada mitad y luego las une.

#### Características:
- **Complejidad Temporal**: `O(n log n)` en todos los casos, para descomponer la lista se necesita `O(log n)`, para componer el resultado se necesita `O(n)`, de ahi surge `O(n log n)`.
- **Complejidad Espacial**: `O(n)` (no es in-place), dado que genera `n` listas en la descomposicion.
- **Uso**: Muy eficiente para listas grandes y estable.

### 5. Quick Sort

#### Resumen:
El Quick Sort es otro algoritmo basado en Divide y Vencerás, que selecciona un "pivote" y particiona la lista en elementos menores y mayores que el pivote, ordenando recursivamente las particiones.

#### Características:
- **Complejidad Temporal**: `O(n log n)` en el caso promedio, `O(n²)` en el peor (cuando la lista ya está ordenada o inversa), se comportaría como el método Bubble Sort.
- **Complejidad Espacial**: `O(log n)` en el caso promedio (debido a la recursión).
- **Uso**: Muy eficiente en la práctica y versátil.

### Tabla Comparativa de Complejidad

| Algoritmo         | Mejor Caso| Caso Promedio | Peor Caso | Complejidad Espacial|
|-------------------|-----------|---------------|-----------|---------------------|
| Bubble Sort       | `O(n)`      | `O(n²)`         | `O(n²)`     | `O(1)`        |
| Selection Sort    | `O(n²)`     | `O(n²)`         | `O(n²)`     | `O(1)`        |
| Insertion Sort    | `O(n)`      | `O(n²)`         | `O(n²)`     | `O(1)`        |
| Merge Sort        | `O(n log n)`| `O(n log n)`    | `O(n log n)`| `O(n)`        |
| Quick Sort        | `O(n log n)`| `O(n log n)`    | `O(n²)`     | `O(log n)`    |

***
***

## Resumen sobre Programación Dinámica

La programación dinámica es una técnica de diseño de algoritmos que se utiliza para resolver problemas complejos dividiéndolos en subproblemas más simples. Es especialmente útil en situaciones donde los subproblemas se superponen y donde la solución de un problema puede construirse a partir de las soluciones de sus subproblemas.

### 1. Overlapping Subproblems
Los problemas que presentan **subproblemas superpuestos** son aquellos en los que se repiten los mismos subproblemas al resolver el problema principal. Esto significa que en lugar de resolver el mismo subproblema varias veces, se puede almacenar su resultado y reutilizarlo. Esta característica es fundamental para aplicar programación dinámica, ya que reduce el tiempo de cómputo al evitar cálculos redundantes.

### 2. Optimized Substructure
La **estructura óptima** se refiere a la propiedad que tienen ciertos problemas en los que la solución óptima del problema puede construirse a partir de las soluciones óptimas de sus subproblemas. Si un problema tiene una estructura óptima, entonces es adecuado para ser resuelto mediante programación dinámica, ya que podemos combinar soluciones de subproblemas para formar la solución del problema original.

### 3. Caso - Fibonacci Sequence
La **secuencia de Fibonacci** es un ejemplo clásico que ilustra la programación dinámica. La secuencia se define como:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2) para n > 1`

Este problema presenta subproblemas superpuestos, ya que calcular `F(n)` implica calcular `F(n-1)` y `F(n-2)`, que a su vez requieren cálculos de `F(n-2)` y `F(n-3)`, y así sucesivamente. Usar programación dinámica (ya sea con memoización o un enfoque de abajo hacia arriba) permite calcular la secuencia de Fibonacci de manera eficiente.

### 4. Memoization
La **memoización** es una técnica de optimización que consiste en almacenar los resultados de los subproblemas ya resueltos para evitar recalcularlos. Se implementa generalmente utilizando una estructura de datos como un diccionario o un arreglo. Cuando se necesita el resultado de un subproblema, se verifica si ya está almacenado. Si es así, se devuelve el resultado almacenado; si no, se calcula y se almacena para usos futuros. Esto es fundamental para mejorar la eficiencia de algoritmos recursivos que tienen subproblemas superpuestos.

### 5. Bottom Up
El enfoque **Bottom Up** es una técnica de programación dinámica que resuelve el problema construyendo soluciones a partir de subproblemas más pequeños. En lugar de resolver el problema de manera recursiva, se comienza desde los casos base y se van resolviendo los subproblemas hasta llegar a la solución del problema original. Este enfoque suele implementarse utilizando bucles, y es útil para evitar la sobrecarga de la recursión, lo que puede ser un problema en algunos casos.