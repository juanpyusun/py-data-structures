# Clase Nodo, cada elemento de la LinkedList
class Node:
    
    def __init__(self, initdata):
        """
        Initializes a new node with the provided data and sets the next node to None.

        :param initdata: The data to be stored in the node.
        """
        self.__data = initdata  # Using __data to indicate it's a "private" attribute
        self.__next = None      # The next node is initialized as None

    @property
    def data(self):
        """
        Gets the data of the node.

        :return: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, newdata):
        """
        Sets the data of the node to the provided new value.

        :param newdata: The new value to be assigned to the node's data.
        """
        self.__data = newdata

    @property
    def next(self):
        """
        Gets the next node.

        :return: The next node in the list.
        """
        return self.__next

    @next.setter
    def next(self, newnext):
        """
        Sets the next node to the provided node.

        :param newnext: The node to be assigned as the next node.
        """
        self.__next = newnext

    def __repr__(self):
        """
        Returns a string representation of the node.

        :return: A string showing the data of the node.
        """
        return f"Node(data={self.__data})"

    def __str__(self):
        """
        Returns a human-readable string of the node.

        :return: A representative string of the node.
        """
        return f"Node with data: {self.__data}"

    def __eq__(self, other):
        """
        Compares this node with another node by their data.

        :param other: The other node to compare.
        :return: True if the nodes have the same data, False otherwise.
        """
        if isinstance(other, Node):
            return self.__data == other.data
        return NotImplemented

    def __ne__(self, other):
        """
        Compares this node with another node for inequality based on their data.

        :param other: The other node to compare.
        :return: True if the nodes have different data, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self):
        """
        Returns a hash of the node based on its data.

        :return: A hash value representing the node's data.
        """
        return hash(self.__data)

    def __len__(self):
        """
        Returns the size of the node, which is constant.

        :return: Always returns 1, as a node represents a single element.
        """
        return 1