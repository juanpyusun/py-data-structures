from typing import Optional

class Node:    
    def __init__(self, value)->None:
        self.__value = value
        self.__next = None

    def __repr__(self)->str:
        return f"Node(value={self.__value})"

    def __str__(self)->str:
        return f"Node(value={self.__value})"

# Se usara la estructura de LinkedList, siendo Head el primer elemento en salir
# y siendo Tail el ultimo elemento en llegar, se añade en Tail, se remueve en Head
# Siendo en ambos casos una complejidad O(1)

class Queue:
    def __init__(self, value=None)->None:
        if value:
            new_node = Node(value)
            self.__first = new_node
            self.__last = new_node
            self.__length = 1
        else:
            self.__head = None
            self.__tail = None
            self.__length = 0

    def dequeue(self)->Optional[Node]:
        if self.__length == 0:
            return None
        temp = self.__first

        if self.__length == 1:
            self.__first = None
            self.__last = None
        else:
            self.__first = self.__first.next

        temp.next = None
        self.__length -= 1
        return temp

    def enqueue(self, value:int|str)->bool:
        new_node = Node(value)
        
        if self.first:
            self.last.next = new_node
            self.last = new_node
        else:
            self.first = new_node
            self.last = new_node
        self.length += 1  
        return True

    def __str__(self)->str:
        temp = self.__first
        string = "<- "
        while temp:
            string += f"{temp.value} <- "
            temp = temp.next
        return string