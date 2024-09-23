from typing import Optional

class Node:    
    def __init__(self, initdata)->None:
        self.__data = initdata  # Using __data to indicate it's a "private" attribute
        self.__next = None # The next node is initialized as None
        self.__prev = None # The previous node is initialized as None
        
    @property
    def prev(self) -> Optional['Node']:
        """
        Returns the previous node in the collection.

        Returns:
            Optional[Node]: The previous node if it exists, otherwise None.
        """
        return self.__prev

    @prev.setter
    def prev(self, newprev: Optional['Node']) -> None:
        """
        Sets the previous node in the linked list.

        Args:
            newprev (Optional['Node']): The node to set as the previous node.

        Returns:
            None
        """
        self.__prev = newprev
        
    @property
    def data(self)->int|str:
        """
        Returns the data stored in the node.

        Returns:
            int | str: The data stored in the node, which can be either an integer or a string.
        """
        return self.__data

    @data.setter
    def data(self, newdata:int|str)->None:
        """
        Sets the data for the node.

        Args:
            newdata (int | str): The new data to be set for the node. It can be either an integer or a string.

        Returns:
            None
        """
        self.__data = newdata

    @property
    def next(self)->Optional['Node']:
        """
        Returns the next node in the collection.

        Returns:
            Optional[Node]: The next node if it exists, otherwise None.
        """
        return self.__next

    @next.setter
    def next(self, newnext:Optional['Node'])->None:
        """
        Sets the next node in the linked list.

        Args:
            newnext (Optional['Node']): The node to set as the next node.

        Returns:
            None
        """
        self.__next = newnext

    def __repr__(self)->str:
        """
        Return a string representation of the Node object.

        Returns:
            str: A string in the format "Node(data=<data>)" where <data> is the value stored in the node.
        """
        return f"Node(data={self.__data})"

    def __str__(self)->str:
        """
        Returns a string representation of the Node object.

        Returns:
            str: A string describing the Node with its data.
        """
        return f"Node(data={self.__data})"

    def __eq__(self, other: 'Node')->bool:
        """
        Compare this Node with another Node for equality.

        Args:
            other (Node): The other Node to compare against.

        Returns:
            bool: True if the data of both Nodes are equal, False otherwise.
        """
        if isinstance(other, Node):
            return self.__data == other.data
        return NotImplemented

    def __ne__(self, other: 'Node')->bool:
        """
        Check if this Node is not equal to another Node.

        Args:
            other (Node): The other Node to compare against.

        Returns:
            bool: True if the Nodes are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self)->int:
        """
        Returns the hash value of the node based on its data.

        This method allows the node to be used in hash-based collections
        such as sets and dictionaries.

        Returns:
            int: The hash value of the node's data.
        """
        return hash(self.__data)

    def __len__(self)->int:
        """
        Return the length of the node.

        Returns:
            int: The length of the node, which is always 1.
        """
        return 1