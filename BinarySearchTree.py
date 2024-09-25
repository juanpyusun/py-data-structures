from typing import Optional

class Node:
    def __init__(self, value: int)->None:
        self.__value = value
        self.__left = None
        self.__right = None
    
    def __repr__(self)->str:
        return f"Node(value={self.__value})"
    
    def __str__(self)->str:
        return f"Node(value={self.__value})"
    
class BinarySearchTree:
    def __init__(self, value=None)->None:
        if value:
            new_node = Node(value)
            self.__root = new_node
            self.__length = 1
        else:
            self.__root = None
            self.__length = 0