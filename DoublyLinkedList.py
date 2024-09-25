from typing import Optional

class Node:    
    def __init__(self, initdata)->None:
        self.__data = initdata
        self.__next = None
        self.__prev = None
    def __repr__(self)->str:
        return f"Node(data={self.__data})"

    def __str__(self)->str:
        return f"Node(data={self.__data})"

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
    
    def get(self, index:int)->Optional[Node]:
        """
        Retrieve the node at the specified index in the doubly linked list.
        Args:
            index (int): The zero-based index of the node to retrieve.
        Returns:
            Optional[Node]: The node at the specified index, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.__length:
            return None
        
        # If the index is closer to the start of the list, traverse from the head
        if index < self.__length//2:
            temp = self.__head
            for _ in range(index):
                temp = temp.next
        # If the index is closer to the end of the list, traverse from the tail
        else:
            temp = self.__tail
            for _ in range(self.__length - 1, index, - 1):
                temp = temp.prev
        return temp
    
    def insert(self, index:int, value:int|str)->bool:
        """
        Insert a new node with the provided value at the specified index in the doubly linked list.
        
        Args:
            index (int): The zero-based index at which to insert the new node.
            value (int or str): The value to be added to the list.
        
        Returns:
            bool: True if the node was successfully inserted, otherwise False.
        """
        if index < 0 or index > self.__length:
            return False
        
        if index == 0:
            return self.prepend(value)
        elif index == self.__length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.__length += 1
        return True
                
    def pop(self)->Optional[Node]:
        """
        Removes and returns the last node from the doubly linked list.
        Returns:
            Optional[Node]: The node that was removed from the end of the list, 
                            or None if the list is empty.
        """
        if self.__length == 0:
            return None
        
        temp = self.__tail
        
        if self.__length == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = temp.prev
            self.__tail.next = None
            temp.prev = None
        
        self.__length -= 1
        return temp
    
    def pop_first(self)->Optional[Node]:
        """
        Removes and returns the first node from the doubly linked list.
        
        Returns:
            Optional[Node]: The node that was removed from the beginning of the list, 
                            or None if the list is empty.
        """
        if self.__length == 0:
            return None
        
        temp = self.__head
        
        if self.__length == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = temp.next
            self.__head.prev = None
            temp.next = None
        
        self.__length -= 1
        return temp
        
    def prepend(self, value:int|str)->bool:
        """
        Prepends a new node with the provided value to the beginning of the doubly linked list.

        Args:
            value (int or str): The value to be added to the list.

        Returns:
            bool: True if the node was successfully prepended to the list, otherwise False.
        """
        new_node = Node(value)
        
        if self.__head:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        else:
            self.__head = new_node
            self.__tail = new_node
        
        self.__length += 1
        
        return True
    
    def remove(self, index:int)->Optional[Node]:
        """
        Removes and returns the node at the specified index in the doubly linked list.
        
        Args:
            index (int): The zero-based index of the node to remove.
        
        Returns:
            Optional[Node]: The node that was removed from the list, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.__length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.__length - 1:
            return self.pop()
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.__length -= 1
        return temp
    
    def set_value(self, index:int, value:int|str)->bool:
        """
        Set the value of the node at the specified index in the doubly linked list.
        
        Args:
            index (int): The zero-based index of the node to modify.
            value (int or str): The new value to assign to the node.
        
        Returns:
            bool: True if the value was successfully set, otherwise False.
        """
        node = self.get(index)
        
        if node:
            node.data = value
            return True
        return False
    
    def swap_first_last(self)->None:
        """
        Swap the values of the first (head) and last (tail) nodes in the doubly linked list.

        This method checks if both the head and tail nodes exist in the list. If they do,
        it swaps their values.

        Returns:
            None
        """
        if self.head and self.tail:
            self.head.data, self.tail.data = self.tail.data, self.head.data 

    def reverse(self)->bool:
        """
        Reverses the doubly linked list in place.
        Returns:
            bool: True if the list was successfully reversed, None if the list is empty.
        """
        if self.__length == 0:
            return None
        
        current = self.__head
        previous = None
        self.__tail = current  # Update tail to the current head before reversing
        
        while current:
            next_node = current.next  # Store the next node
            current.next = previous    # Reverse the next pointer
            current.prev = next_node   # Reverse the prev pointer
            previous = current         # Move previous to current
            current = next_node        # Move to the next node
        
        self.__head = previous  # Update head to the last node processed
        return True

    def is_palindrome(self) -> bool:
        """
        Check if the doubly linked list is a palindrome.
        A palindrome is a sequence that reads the same backward as forward.
        This method compares the values from the head and the tail of the list,
        moving towards the center, to determine if the list is a palindrome.
        Returns:
            bool: True if the list is a palindrome, False otherwise.
        """
        if self.__length == 0:
            return True  # An empty list is a palindrome
        if self.__length == 1:
            return True  # A single node is a palindrome
        
        left = self.__head
        right = self.__tail

        while left != right and left.prev != right:  # Check until the pointers meet
            if left.data != right.data:
                return False  # Values don't match
            left = left.next
            right = right.prev
        
        return True

    def swap_pairs(self)->bool:
        """
        Swap the values of adjacent nodes in the doubly linked list.
        This method iterates through the list and swaps the values of each pair of adjacent nodes.
        If the list is empty or contains only one node, no swaps are performed.
        Returns:
            bool: True if the operation was performed, otherwise returns None.
        """
        if self.__head is None or self.__head.next is None:
            return  # No swap needed for empty or single-node lists

        current = self.__head
        
        # Initialize a pointer for the new head if the list has more than one node
        if current.next is self.__tail:
            self.__tail = current
        
        while current and current.next:
            # Swap values of the current node and the next node
            current.data, current.next.data = current.next.data, current.data
            
            # Move to the next pair (two nodes ahead)
            current = current.next.next
            
            # If current is None, we've reached the end
            if current is None:
                break
            
            # Update tail if we reach the end of the list
            if current.next is None:
                self.__tail = current.prev
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
    