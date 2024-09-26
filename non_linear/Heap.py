from typing import Optional
    
# Clase Max-Heap (valor maximo en la raiz)
class Heap:
    def __init__(self, value=None)->None:
        self.__heap = []
    
    @property
    def heap(self):
        return self.__heap

    # Estas funciones son para cuando se empieza en el indice cero (__left_child, __right_child, __parent)
    def __left_child(self, index:int)->int:
        return 2 * index + 1
    
    def __right_child(self, index:int)->int:
        return 2 * index + 2

    def __parent(self, index:int)->int:
        return (index - 1) // 2       

    def __sink_down(self, index:int):
        max_index = index
	  while True:
	      left_index = self.__left_child(index)
	      right_index = self.__right_child(index)

		if (left_index < len(self.__heap) and
		        self.__heap[left_index] > self.__heap[max_index]):
		    max_index = left_index

		if (right_index < len(self.__heap) and
		        self.__heap[right_index] > self.__heap[max_index]):
		    max_index = right_index

		if max_index != index:
		    self.__swap(index, max_index)
		    index = max_index
		else:
		    return True

    def __swap(self, index1:int, index2:int)->None:
        self.__heap[index1], self.__heap[index2] = self.__heap[index2], self.__heap[index1]

    def insert(self, value)->bool:
        self.__heap.append(value)
        current = len(self.__heap) - 1

        while current > 0 and self.__heap[current] > self.__heap[self.__parent(current)]:
            self.__swap(current, self.__parent(current))
            current = self.__parent(current)

    def remove(self):
        if len(self.__heap) == 0:
            return None
        elif len(self.__heap) == 1:
            return self.__heap.pop()
        max_value = self.__heap[0]
        self.__heap[0] = self.__heap.pop()
        self.__sink_down(0)
        return max_value
            
    def __str__(self)->str:
        return str(self.__heap) 

 