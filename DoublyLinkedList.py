from typing import Optional
from Node import Node

class DoublyLinkedList:
    
    def __init__(self, value=None)->None:
        """
        Initializes a new DoublyLinkedList.

        If a value is provided, a new node is created with that value and set as both the head and tail of the list.
        The length of the list is set to 1.

        If no value is provided, the head and tail are set to None, and the length of the list is set to 0.

        Args:
            value (optional): The initial value to be added to the list. Defaults to None.
        """
        if value:
            new_node = Node(value)
            self.__head = new_node
            self.__tail = new_node
            self.__length = 1
        else:
            self.__head = None
            self.__tail = None
            self.__length = 0

    @property
    def head(self) -> Optional[Node]:
        """
        Returns the head node of the doubly linked list.

        Returns:
            Optional[Node]: The head node of the list if it exists, otherwise None.
        """
        return self.__head

    """ @head.setter
    def head(self, value: Node) -> None:
        self.__head = value """

    @property
    def tail(self) -> Optional[Node]:
        """
        Returns the tail node of the doubly linked list.

        Returns:
            Optional[Node]: The tail node of the list if it exists, otherwise None.
        """
        return self.__tail

    """ @tail.setter
    def tail(self, value: Node) -> None:
        self.__tail = value """

    @property
    def length(self) -> int:
        """
        Returns the number of elements in the doubly linked list.

        Returns:
            int: The number of elements in the list.
        """
        return self.__length

    """ @length.setter
    def length(self, value: int) -> None:
        self.__length = value """
    
    def append(self, value:int|str)->bool:
        """
        Appends a new node with the provided value to the end of the doubly linked list.

        Args:
            value (int or str): The value to be added to the list.

        Returns:
            bool: True if the node was successfully appended to the list, otherwise False.
        """
        new_node = Node(value)
        
        if self.__head:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        else:
            self.__head = new_node
            self.__tail = new_node
        
        self.__length += 1
        
        return True
                
    def __str__(self)->str:
        """
        Returns a string representation of the doubly linked list.
        
        The format of the string is "None <- node1_data <-> node2_data <-> ... <-> nodeN_data -> None",
        where each node's data is separated by " <-> " and the list starts with "None <- " and ends with " -> None".
        
        Returns:
            str: A string representation of the doubly linked list.
        """
        temp = self.__head
        string = "None <- "
        while temp:
            string += f"{temp.data}"
            
            if temp.next:
                string += " <-> "
            else:
                string += " -> "
            
            temp = temp.next           
            
        return string + "None"

    def __len__(self)->int:
        """
        Return the number of elements in the doubly linked list.

        Returns:
            int: The number of elements in the doubly linked list.
        """
        return self.__length

    def __repr__(self)->str:
        """
        Return a string representation of the DoublyLinkedList instance.

        Returns:
            str: A string describing the DoublyLinkedList with its head, tail, and length.
        """
        return f"DoublyLinkedList(head={self.__head}, tail={self.__tail}, length={self.__length})"
    
if __name__ == "__main__":
    dll = DoublyLinkedList(5)
    print(dll)
    print(len(dll))
    print(repr(dll))
    print(dll.head)
    print(dll.tail)
    print(dll.length)