from typing import Optional, Generator

class Node:    
    def __init__(self, value)->None:
        self.__value = value
        self.__next = None

    def __repr__(self)->str:
        return f"Node(value={self.__value})"

    def __str__(self)->str:
        return f"Node(value={self.__value})"

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
            temp.value = value
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

    def __two_pointer_method(self)->Generator[tuple[Node, Node], None, None]:
        """
        A generator method that implements the two-pointer technique to traverse the linked list.
        Yields:
            tuple[Node, Node]: A tuple containing the slow pointer and the fast pointer.
                - slow_pointer: Moves one step at a time.
                - fast_pointer: Moves two steps at a time.
        """
        slow_pointer = self.__head
        fast_pointer = self.__head
        
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            yield slow_pointer, fast_pointer  # Generador que devuelve ambos punteros

    def find_middle_node(self)->Optional[Node]:
        """
        Finds the middle node of the linked list using the two-pointer method.

        This method uses two pointers, `slow` and `fast`, where `slow` moves one step
        at a time and `fast` moves two steps at a time. When `fast` reaches the end
        of the list, `slow` will be at the middle node.

        Returns:
            Optional[Node]: The middle node of the linked list, or None if the list is empty.
        """
        for slow, fast in self.__two_pointer_method():
            pass  # Solo necesitamos el valor de slow al final
        return slow

    def has_loop(self)->bool:
        """
        Determines if the linked list contains a loop.

        This method uses the two-pointer technique (Floyd's Tortoise and Hare algorithm)
        to detect if there is a cycle in the linked list. If the slow pointer and the 
        fast pointer meet at some point, it indicates the presence of a loop.

        Returns:
            bool: True if a loop is detected, False otherwise.
        """
        for slow, fast in self.__two_pointer_method():
            if slow is fast:
                return True
        return False

    def find_kth_from_end(self, k: int) -> Optional[Node]:
        """
        Finds the k-th node from the end of the linked list.
        This method uses two pointers to find the k-th node from the end of the list.
        The `fast` pointer is moved k nodes ahead of the `slow` pointer. Then, both
        pointers are moved one node at a time until the `fast` pointer reaches the end
        of the list. At this point, the `slow` pointer will be at the k-th node from the end.
        Args:
            k (int): The position from the end of the list to find the node.
        Returns:
            Optional[Node]: The k-th node from the end of the list, or None if the list
                            has fewer than k nodes.
        """
        slow = self.__head
        fast = self.__head

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

    def partition_list(self, x: int) -> None:
        """
        Rearranges the linked list such that all nodes with values less than `x` come before nodes with values 
        greater than or equal to `x`. The relative order of nodes in each partition is preserved.
        Args:
            x (int): The partitioning value.
        Returns:
            None: This method modifies the list in place and does not return a value.
        Notes:
            - If the list is empty, the method returns immediately.
            - Two dummy nodes are used to create two separate lists: one for nodes with values less than `x` 
              and one for nodes with values greater than or equal to `x`.
            - The two lists are then connected, and the head and tail of the original list are updated accordingly.
        """
        # If the list is empty, return immediately
        if self.__head is None:
            return None
        
        # Create two dummy nodes
        dummy1 = Node(0)  # For nodes < x
        dummy2 = Node(0)  # For nodes >= x
        
        prev1 = dummy1  # Pointer for the lesser list
        prev2 = dummy2  # Pointer for the greater or equal list
        
        current = self.__head
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
        self.__head = dummy1.next

        # Update the tail of the list
        if prev2 != dummy2:  # If there are nodes in the greater or equal list
            self.tail = prev2  # The tail is the last node of the greater or equal list
        else:
            self.tail = prev1  # If there are no nodes greater or equal, the tail is the last node of the lesser list

    def remove_duplicates(self) -> None:
        """
        Removes duplicate values from the linked list. This method traverses the
        linked list, keeping track of seen values using a set. If a duplicate value
        is found, the corresponding node is skipped. The method updates the tail
        to the last unique node found.
        Returns:
            None
        """
        current = self.__head
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

    def binary_to_decimal(self)->int:
        """
        Converts a binary number represented by the linked list into its decimal equivalent.
        The linked list is assumed to represent a binary number where each node contains a single binary digit (0 or 1).
        The head of the linked list represents the most significant bit (MSB).
        Returns:
            int: The decimal equivalent of the binary number.
        """
        current = self.__head
        decimal_value = 0
        position = 0

        while current:
            decimal_value += current.value * (2 ** (self.length - position - 1))
            position += 1
            current = current.next

        return decimal_value

    def reverse_between(self, start_index:int, end_index:int)->None:
        """
        Reverse the nodes of the linked list from start_index to end_index.
        This method reverses the nodes in the linked list between the given
        start_index and end_index (inclusive). The indices are zero-based.
        Args:
            start_index (int): The starting index of the sublist to reverse.
            end_index (int): The ending index of the sublist to reverse.
        Returns:
            None: This method does not return any value.
        Raises:
            IndexError: If start_index or end_index is out of bounds.
        Example:
            Given the linked list: 1 -> 2 -> 3 -> 4 -> 5
            Calling reverse_between(1, 3) will modify the list to: 1 -> 4 -> 3 -> 2 -> 5
        """
        if not self.__head or start_index == end_index:
            return None
        
        # Dummy node to handle edge cases like reversing from the head
        dummy = Node(0)
        dummy.next = self.__head
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
        self.__head = dummy.next

	  # Update tail
        if self.__head is None:  # If the list is empty
            self.tail = None
        else:
            # Traverse to get the new tail
            current = self.__head
            while current.next:
                current = current.next
            self.tail = current  # Set tail to the last node

    def __str__(self)->str:
        """
        Returns a string representation of the linked list.
        
        The string is formatted as a sequence of node value values separated by ' -> ',
        ending with 'None' to indicate the end of the list.

        Returns:
            str: A string representation of the linked list.
        """
        temp = self.__head
        string = ""
        while temp is not None:
            string += f"{temp.value} -> "
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
    