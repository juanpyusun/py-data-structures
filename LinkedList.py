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
# ------------------------------
    def __two_pointer_method(self):
        slow_pointer = self.head
        fast_pointer = self.head
        
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            yield slow_pointer, fast_pointer  # Generador que devuelve ambos punteros

    def find_middle_node(self):
        for slow, fast in self.__two_pointer_method():
            pass  # Solo necesitamos el valor de slow al final
        return slow

    def has_loop(self):
        for slow, fast in self.__two_pointer_method():
            if slow is fast:
                return True
        return False

    def find_kth_from_end(self, k):
        slow = self.head
        fast = self.head

        # Mover el puntero rápido k nodos adelante
        for _ in range(k):
            if fast is None:
                return None  # La lista es más corta que k nodos
            fast = fast.next

        # Mover ambos punteros hasta que fast alcance el final
        while fast:
            slow = slow.next
            fast = fast.next

        return slow 

	def partition_list(self, x):
        # If the list is empty, return immediately
        if self.head is None:
            return
        
        # Create two dummy nodes
        dummy1 = Node(0)  # For nodes < x
        dummy2 = Node(0)  # For nodes >= x
        
        prev1 = dummy1  # Pointer for the lesser list
        prev2 = dummy2  # Pointer for the greater or equal list
        
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current  # Link to the lesser list
                prev1 = prev1.next
            else:
                prev2.next = current  # Link to the greater or equal list
                prev2 = prev2.next
            current = current.next
        
        # Connect the two lists
        prev1.next = dummy2.next  # Link the end of the lesser list to the start of the greater list
        prev2.next = None  # End the greater list
        
        # Update the head of the original list
        self.head = dummy1.next

	 # Update the tail of the list
    if prev2 != dummy2:  # If there are nodes in the greater or equal list
        self.tail = prev2  # The tail is the last node of the greater or equal list
    else:
        self.tail = prev1  # If there are no nodes greater or equal, the tail is the last node of the lesser list

def remove_duplicates(self):
    current = self.head
    prev = None
    seen = set()  # Set to track seen values

    while current:
        if current.value in seen:
            # If value is a duplicate, skip the current node
            prev.next = current.next
        else:
            # If value is not a duplicate, add it to the set and move prev
            seen.add(current.value)
            prev = current
        
        # Move to the next node
        current = current.next
    
    # Update tail to the last unique node
    if prev:  # Ensure that there was at least one unique node
        self.tail = prev
    else:
        self.tail = None  # If no unique nodes, set tail to None

   def binary_to_decimal(self):
        current = self.head
        decimal_value = 0
        position = 0

        while current:
            decimal_value += current.value * (2 ** (self.length - position - 1))
            position += 1
            current = current.next

        return decimal_value

    def reverse_between(self, start_index, end_index):
        if not self.head or start_index == end_index:
            return None
        
        # Dummy node to handle edge cases like reversing from the head
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        # Move `prev` to the node just before the start_index
        for _ in range(start_index):
            prev = prev.next

        # `start` will be the first node to reverse
        start = prev.next
        # `then` will point to the node that will be reversed
        then = start.next

        # Reverse the sublist
        for _ in range(end_index - start_index):
            start.next = then.next  # Change next of start
            then.next = prev.next  # Move `then` to the front of the sublist
            prev.next = then  # Connect `prev` to `then`
            then = start.next  # Update `then` to the next node to reverse

        # Update the head if necessary
        self.head = dummy.next

	  # Update tail
        if self.head is None:  # If the list is empty
            self.tail = None
        else:
            # Traverse to get the new tail
            current = self.head
            while current.next:
                current = current.next
            self.tail = current  # Set tail to the last node
    

# -------------------------------

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
    