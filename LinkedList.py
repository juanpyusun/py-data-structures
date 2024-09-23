from typing import Optional
from Node import Node

class LinkedList:
    
    def __init__(self, value=None)->None:
        """
        Initializes a new LinkedList. If a value is provided, a new node is created
        with that value and set as both the head and tail of the list. If no value 
        is provided, the list is initialized as empty.

        Args:
            value (optional): The initial value for the LinkedList. Defaults to None.

        Attributes:
            __head (Node or None): The head node of the LinkedList.
            __tail (Node or None): The tail node of the LinkedList.
            __length (int): The number of nodes in the LinkedList.
        """
        if value is None:
            self.__head = None
            self.__tail = None
            self.__length = 0
        else:
            new_node = Node(value)
            self.__head = new_node
            self.__tail = new_node
            self.__length = 1

    @property
    def head(self)->Optional[Node]:
        """
        Returns the head node of the linked list.

        Returns:
            Optional[Node]: The head node of the linked list if it exists, otherwise None.
        """
        return self.__head

    @property
    def tail(self)->Optional[Node]:
        """
        Returns the tail node of the linked list.

        Returns:
            Optional[Node]: The tail node if it exists, otherwise None.
        """
        return self.__tail

    @property
    def length(self)->int:
        """
        Returns the length of the linked list.

        :return: The number of elements in the linked list.
        :rtype: int
        """
        return self.__length

    def append(self, value:int|str)->bool:
        """
        Appends a new node with the given value to the end of the linked list.
        Args:
            value (int | str): The value to be stored in the new node.
        Returns:
            bool: True if the node was successfully appended.
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__length += 1
        return True

    def get(self, index: int)->Optional[Node]:
        """
        Retrieve the node at the specified index in the linked list.
        Args:
            index (int): The zero-based index of the node to retrieve.
        Returns:
            Optional[Node]: The node at the specified index, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.__length:
            return None
        
        temp = self.__head
        
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index:int, value:int|str)->bool:
        """
        Sets the value of the node at the specified index.

        :param index: The index of the node whose value is to be set.
        :param value: The new value to be assigned to the node.
        :return: True if the operation was successful, False otherwise.
        """
        temp = self.get(index)
        
        if temp:
            temp.data = value
            return True
        
        return False

    def insert(self, index:int, value:int|str)->bool:
        """
        Inserts a new node with the given value at the specified index in the linked list.
        Args:
            index (int): The position at which to insert the new node. Must be between 0 and the current length of the list.
            value (int | str): The value to be stored in the new node. Can be an integer or a string.
        Returns:
            bool: True if the insertion was successful, False otherwise.
        """
        if index < 0 or index > self.__length:
            return False

        if index == 0:
            return self.prepend(value)
        
        if index == self.__length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.__length += 1
        return True

    def remove(self, index:int)->Optional[Node]:
        """
        Removes the node at the specified index from the linked list.
        Args:
            index (int): The zero-based index of the node to remove.
        Returns:
            Optional[Node]: The removed node if the index is valid, otherwise None.
        """
        if index < 0 or index >= self.__length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.__length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next  # Avoid using get() for O(1) access
        prev.next = temp.next
        temp.next = None
        self.__length -= 1
        return temp

    def reverse(self)->None:
        def reverse(self) -> None:
            """
            Reverses the linked list in place.
            This method swaps the head and tail of the linked list and then iteratively
            reverses the direction of the links between the nodes.
            Returns:
                None
            """
        temp = self.__head
        self.__head, self.__tail = self.__tail, self.__head
        
        after = temp.next
        before = None
        for _ in range(self.__length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def pop(self)->Optional[Node]:
        """
        Removes and returns the last node from the linked list.
        If the linked list is empty, returns None.
        Returns:
            Optional[Node]: The last node of the linked list, or None if the list is empty.
        """
        if self.__length == 0:
            return None

        temp = self.__head
        pre = self.__head

        while temp.next:
            pre = temp
            temp = temp.next

        self.__tail = pre
        self.__tail.next = None
        self.__length -= 1

        if self.__length == 0:
            self.__head = None
            self.__tail = None  
        
        return temp

    def prepend(self, value:int|str)->bool:
        """
        Adds a new node with the given value to the beginning of the linked list.
        Args:
            value (int | str): The value to be added to the linked list. It can be either an integer or a string.
        Returns:
            bool: True if the node was successfully added to the linked list.
        """
        new_node = Node(value)

        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__length += 1
        return True

    def pop_first(self)->Optional[Node]:
        """
        Removes and returns the first node from the linked list.
        Returns:
            Optional[Node]: The node that was removed from the beginning of the list,
                            or None if the list is empty.
        """
        if self.__length == 0:
            return None

        temp = self.__head
        self.__head = self.__head.next
        temp.next = None
        self.__length -= 1

        if self.__length == 0:
            self.__tail = None

        return temp

    def __str__(self)->str:
        """
        Returns a string representation of the linked list.
        
        The string is formatted as a sequence of node data values separated by ' -> ',
        ending with 'None' to indicate the end of the list.

        Returns:
            str: A string representation of the linked list.
        """
        temp = self.__head
        string = ""
        while temp is not None:
            string += f"{temp.data} -> "
            temp = temp.next
        return string + "None"

    def __len__(self)->int:
        """
        Return the number of elements in the linked list.

        Returns:
            int: The number of elements in the linked list.
        """
        return self.__length

    def __repr__(self)->str:
        """
        Return a string representation of the LinkedList instance.

        Returns:
            str: A string describing the LinkedList with its head, tail, and length.
        """
        return f"LinkedList(head={self.__head}, tail={self.__tail}, length={self.__length})"
    