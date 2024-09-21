class LinkedList:
    def __init__(self, value=None):
        """
        Initializes a new linked list. If a value is provided, it creates the head and tail nodes.

        :param value: The initial value to be stored in the first node of the list (optional).
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
    def head(self):
        """
        Gets the head node of the linked list.

        :return: The head node of the linked list.
        """
        return self.__head

    @property
    def tail(self):
        """
        Gets the tail node of the linked list.

        :return: The tail node of the linked list.
        """
        return self.__tail

    @property
    def length(self):
        """
        Gets the number of nodes in the linked list.

        :return: The number of nodes in the linked list.
        """
        return self.__length

    def append(self, value):
        """
        Adds a new node with the provided value to the end of the linked list.

        :param value: The value to be added to the linked list.
        :return: True if the operation was successful.
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

    def get(self, index):
        """
        Retrieves the node at the specified index in the linked list.

        :param index: The index of the node to retrieve.
        :return: The node at the specified index, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.__length:
            return None

        temp = self.__head
        
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
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

    def insert(self, index, value):
        """
        Inserts a new node with the provided value at the specified index.

        :param index: The index at which to insert the new node.
        :param value: The value to be added to the linked list.
        :return: True if the operation was successful, False otherwise.
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

    def remove(self, index):
        """
        Removes the node at the specified index from the linked list.

        :param index: The index of the node to remove.
        :return: The removed node, or None if the index is out of bounds.
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

    def reverse(self):
        """
        Reverses the linked list in place.
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

    def pop(self):
        """
        Removes and returns the last node from the linked list.

        :return: The removed node, or None if the list is empty.
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

    def prepend(self, value):
        """
        Adds a new node with the provided value to the beginning of the linked list.

        :param value: The value to be added to the linked list.
        :return: True if the operation was successful.
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

    def pop_first(self):
        """
        Removes and returns the first node from the linked list.

        :return: The removed node, or None if the list is empty.
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

    def __str__(self):
        """
        Returns a string representation of the linked list.

        :return: A string showing the values of the linked list nodes.
        """
        temp = self.__head
        string = ""
        while temp is not None:
            string += f"{temp.data} -> "
            temp = temp.next
        return string + "None"

    def __len__(self):
        """
        Returns the number of nodes in the linked list.

        :return: The number of nodes in the linked list.
        """
        return self.__length

    def __repr__(self):
        """
        Returns a string representation for debugging purposes.

        :return: A string showing the head, tail, and length of the linked list.
        """
        return f"LinkedList(head={self.__head}, tail={self.__tail}, length={self.__length})"