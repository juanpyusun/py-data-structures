# Índice
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
- [Binary Search Trees (BST)](#binary-search-trees-bst)
  - [BST and Big-O](#bst-and-big-o)
  - [Otro tipo de arboles](#otro-tipo-de-arboles)
- [Hash Table (HT)](#hash-table-ht)
  - [HT and Big-O](#ht-and-big-o)
- [Resumen de Complejidad temporal y estructuras no lineales - Tabla comparativa](#resumen-de-complejidad-temporal-y-estructuras-no-lineales---tabla-comparativa)


***
***

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

# List
- **Estructura**: Espacios contiguos de memoria.
- **Acceso**: Índice en sus elementos.

## L and Big-O
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

# Linked List (LL)
- **Estructura**: Se compone de dos apuntadores y nodos conectados.
- **Acceso**: No tienen índice los elementos.
- **Nodo**: Un nodo se compone de valor y hacia donde está apuntando, por ejemplo, un diccionario de dos valores: `{"value": x, "next": None}`. Entonces, LL sería un conjunto de diccionarios anidados.
- **Memoria**: No están necesariamente acomodados en espacios contiguos de memoria.
- **Apuntadores**: Tiene un apuntador a los nodos de la `head` y la `Tail`.
- **Conexiones**: Cada nodo apunta desde la `head`, hasta el siguiente nodo, así hasta la `Tail`, es decir, de un nodo a otro solo lo conoce el nodo anterior.
- **Tail**: El nodo de la `Tail` apunta a `None`.

## LL and Big-O
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

# Doubly Linked List (DLL)
- **Descripción**: Una lista doblemente enlazada se compone de nodos donde cada nodo tiene tres partes: un valor, un apuntador al siguiente nodo (`next`) y un apuntador al nodo anterior (`prev`).
- **Memoria**: Cada nodo ocupa más espacio que un nodo de una lista enlazada simple debido a los dos apuntadores.

## DLL and Big-O
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

# Stack (S)
- **Descripción**: Una estructura de datos que sigue el principio LIFO (Last In, First Out), donde el último elemento añadido es el primero en ser retirado.
- **Implementación**: Puede ser implementado utilizando arreglos o listas enlazadas.

## S and Big-O
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

# Queue (Q)
- **Descripción**: Una estructura de datos que sigue el principio FIFO (First In, First Out), donde el primer elemento añadido es el primero en ser retirado.
- **Implementación**: Puede ser implementada utilizando arreglos o listas enlazadas.

## Q and Big-O
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

# Resumen de Complejidad temporal y estructuras lineales - Tabla comparativa
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

## Notas sobre la Tabla
- La complejidad de las operaciones puede variar dependiendo de la implementación específica.
- Para las listas, `N/A` indica que la operación no es aplicable.

***
***

# Binary Search Trees (BST)
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

## BST and Big-O
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

# Hash Table (HT)

- **Estructura**: Utiliza un mecanismo de dispersión (hashing) para almacenar pares clave-valor.
- **Acceso**: Los elementos se acceden mediante una clave única en lugar de un índice o posición.
- **Elemento**: Cada entrada en la tabla hash se compone de una clave y un valor: `{"key": x, "value": y}`. Se almacena el valor en un bucket basado en el hash de la clave.
- **Memoria**: Las entradas no se almacenan necesariamente en posiciones contiguas en memoria.
- **Colisiones**: Si dos claves tienen el mismo hash, se puede utilizar manejo de colisiones, como:
  - **Encadenamiento**: Utiliza listas enlazadas para almacenar múltiples elementos en el mismo bucket.
  - **Direccionamiento Abierto**: Reubica datos en la tabla para encontrar un lugar libre.
- **Clave Única**: Cada valor se asocia a una clave única, lo que permite acceder, insertar o eliminar elementos en tiempo constante promedio.
- **Búsqueda**: Se basa en el hash de la clave, lo que generalmente permite un acceso rápido.

## HT and Big-O

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

# Resumen de Complejidad Temporal y Estructuras No Lineales - Tabla Comparativa
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

## Consideraciones Adicionales
- La complejidad de las operaciones puede variar según la implementación específica de cada estructura de datos.
- Para grafos, la representación puede influir en la eficiencia de ciertas operaciones, como la búsqueda y el recorrido.