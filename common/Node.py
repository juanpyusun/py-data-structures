from typing import Optional

class Node:    
    """
    Node class represents a node in a doubly linked list with various operator overloads.
    Attributes:
        __value (int | str): The value stored in the node.
        __next (Optional[Node]): The next node in the list.
        __prev (Optional[Node]): The previous node in the list.
    Methods:
        __init__(value: int | str) -> None:
            Initializes a new node with the given value.
        prev -> Optional['Node']:
            Gets the previous node.
        prev(newprev: Optional['Node']) -> None:
            Sets the previous node.
        value -> int | str:
            Gets the value of the node.
        value(newvalue: int | str) -> None:
            Sets the value of the node.
        next -> Optional['Node']:
            Gets the next node.
        next(newnext: Optional['Node']) -> None:
            Sets the next node.
        __repr__() -> str:
            Returns a string representation of the node.
        __str__() -> str:
            Returns a string representation of the node.
        __eq__(other: 'Node') -> bool:
            Checks if the value of this node is equal to the value of another node.
        __ne__(other: 'Node') -> bool:
            Checks if the value of this node is not equal to the value of another node.
        __hash__() -> int:
            Returns the hash of the node's value.
        __len__() -> int:
            Returns the length of the node (always 1).
        __add__(other: 'Node') -> 'Node':
            Adds the value of this node to the value of another node and returns a new node.
        __sub__(other: 'Node') -> 'Node':
            Subtracts the value of another node from the value of this node and returns a new node.
        __mul__(other: 'Node') -> 'Node':
            Multiplies the value of this node by the value of another node and returns a new node.
        __truediv__(other: 'Node') -> 'Node':
            Divides the value of this node by the value of another node and returns a new node.
        __floordiv__(other: 'Node') -> 'Node':
            Floor divides the value of this node by the value of another node and returns a new node.
        __mod__(other: 'Node') -> 'Node':
            Returns a new node with the value of this node modulo the value of another node.
        __pow__(other: 'Node') -> 'Node':
            Raises the value of this node to the power of the value of another node and returns a new node.
        __lshift__(other: 'Node') -> 'Node':
            Left shifts the value of this node by the value of another node and returns a new node.
        __rshift__(other: 'Node') -> 'Node':
            Right shifts the value of this node by the value of another node and returns a new node.
        __and__(other: 'Node') -> 'Node':
            Performs a bitwise AND operation with the value of another node and returns a new node.
        __or__(other: 'Node') -> 'Node':
            Performs a bitwise OR operation with the value of another node and returns a new node.
        __xor__(other: 'Node') -> 'Node':
            Performs a bitwise XOR operation with the value of another node and returns a new node.
        __iadd__(other: 'Node') -> 'Node':
            In-place addition of the value of another node to this node.
        __isub__(other: 'Node') -> 'Node':
            In-place subtraction of the value of another node from this node.
        __imul__(other: 'Node') -> 'Node':
            In-place multiplication of the value of another node with this node.
        __itruediv__(other: 'Node') -> 'Node':
            In-place true division of the value of this node by the value of another node.
        __ifloordiv__(other: 'Node') -> 'Node':
            In-place floor division of the value of this node by the value of another node.
        __imod__(other: 'Node') -> 'Node':
            In-place modulo operation with the value of another node.
        __ipow__(other: 'Node') -> 'Node':
            In-place exponentiation of the value of this node by the value of another node.
        __ilshift__(other: 'Node') -> 'Node':
            In-place left shift of the value of this node by the value of another node.
        __irshift__(other: 'Node') -> 'Node':
            In-place right shift of the value of this node by the value of another node.
        __pos__() -> 'Node':
            Returns a new node with the positive value of this node.
        __neg__() -> 'Node':
            Returns a new node with the negative value of this node.
        __invert__() -> 'Node':
            Returns a new node with the bitwise inversion of the value of this node.
        __abs__() -> 'Node':
            Returns a new node with the absolute value of this node.
        __lt__(other: 'Node') -> bool:
            Checks if the value of this node is less than the value of another node.
        __le__(other: 'Node') -> bool:
            Checks if the value of this node is less than or equal to the value of another node.
        __gt__(other: 'Node') -> bool:
            Checks if the value of this node is greater than the value of another node.
        __ge__(other: 'Node') -> bool:
            Checks if the value of this node is greater than or equal to the value of another node.
        __contains__(item) -> bool:
            Checks if the node contains the given item (compares with the node's value).
        __getitem__(key) -> 'Node':
            Returns the node itself (for demonstration purposes).
        __setitem__(key, value) -> None:
            Sets the node's value (for demonstration purposes).
        __delitem__(key) -> None:
            Deletes the node's value (for demonstration purposes).
        __call__(*args, **kwargs) -> None:
            Prints the arguments and keyword arguments passed to the node.
        __iter__():
            Yields the node's value.
        __next__():
            Raises StopIteration (for demonstration purposes).
        __bool__() -> bool:
            Returns the boolean value of the node's value.
        __float__() -> float:
            Returns the float representation of the node's value.
        __int__() -> int:
            Returns the integer representation of the node's value.
        __reversed__():
            Returns a reversed iterator of a single-item list containing the node's value.
    """
    
    def __init__(self, value) -> None:
        self.__value = value  # Using __value to indicate it's a "private" attribute
        self.__next = None  # The next node is initialized as None
        self.__prev = None  # The previous node is initialized as None
        
    @property
    def prev(self) -> Optional['Node']:
        return self.__prev

    @prev.setter
    def prev(self, newprev: Optional['Node']) -> None:
        self.__prev = newprev
        
    @property
    def value(self) -> int | str:
        return self.__value

    @value.setter
    def value(self, newvalue: int | str) -> None:
        self.__value = newvalue

    @property
    def next(self) -> Optional['Node']:
        return self.__next

    @next.setter
    def next(self, newnext: Optional['Node']) -> None:
        self.__next = newnext

    def __repr__(self) -> str:
        return f"Node(value={self.__value})"

    def __str__(self) -> str:
        return f"Node(value={self.__value})"

    def __eq__(self, other: 'Node') -> bool:
        if isinstance(other, Node):
            return self.__value == other.value
        return NotImplemented

    def __ne__(self, other: 'Node') -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.__value)

    def __len__(self) -> int:
        return 1

    # Arithmetic operations
    def __add__(self, other: 'Node') -> 'Node':
        return Node(self.value + other.value)

    def __sub__(self, other: 'Node') -> 'Node':
        return Node(self.value - other.value)

    def __mul__(self, other: 'Node') -> 'Node':
        return Node(self.value * other.value)

    def __truediv__(self, other: 'Node') -> 'Node':
        return Node(self.value / other.value)

    def __floordiv__(self, other: 'Node') -> 'Node':
        return Node(self.value // other.value)

    def __mod__(self, other: 'Node') -> 'Node':
        return Node(self.value % other.value)

    def __pow__(self, other: 'Node') -> 'Node':
        return Node(self.value ** other.value)

    def __lshift__(self, other: 'Node') -> 'Node':
        return Node(self.value << other.value)

    def __rshift__(self, other: 'Node') -> 'Node':
        return Node(self.value >> other.value)

    # Bitwise operations
    def __and__(self, other: 'Node') -> 'Node':
        return Node(self.value & other.value)

    def __or__(self, other: 'Node') -> 'Node':
        return Node(self.value | other.value)

    def __xor__(self, other: 'Node') -> 'Node':
        return Node(self.value ^ other.value)

    # In-place operations
    def __iadd__(self, other: 'Node') -> 'Node':
        self.value += other.value
        return self

    def __isub__(self, other: 'Node') -> 'Node':
        self.value -= other.value
        return self

    def __imul__(self, other: 'Node') -> 'Node':
        self.value *= other.value
        return self

    def __itruediv__(self, other: 'Node') -> 'Node':
        self.value /= other.value
        return self

    def __ifloordiv__(self, other: 'Node') -> 'Node':
        self.value //= other.value
        return self

    def __imod__(self, other: 'Node') -> 'Node':
        self.value %= other.value
        return self

    def __ipow__(self, other: 'Node') -> 'Node':
        self.value **= other.value
        return self

    def __ilshift__(self, other: 'Node') -> 'Node':
        self.value <<= other.value
        return self

    def __irshift__(self, other: 'Node') -> 'Node':
        self.value >>= other.value
        return self

    # Unary operations
    def __pos__(self) -> 'Node':
        return Node(+self.value)

    def __neg__(self) -> 'Node':
        return Node(-self.value)

    def __invert__(self) -> 'Node':
        return Node(~self.value)

    def __abs__(self) -> 'Node':
        return Node(abs(self.value))

    # Comparison operations
    def __lt__(self, other: 'Node') -> bool:
        return self.value < other.value

    def __le__(self, other: 'Node') -> bool:
        return self.value <= other.value

    def __gt__(self, other: 'Node') -> bool:
        return self.value > other.value

    def __ge__(self, other: 'Node') -> bool:
        return self.value >= other.value

    def __contains__(self, item) -> bool:
        return self.value == item

    def __getitem__(self, key) -> 'Node':
        return self  # Not really applicable, but returning self for demonstration

    def __setitem__(self, key, value) -> None:
        self.value = value  # Not really applicable but setting self.value for demonstration

    def __delitem__(self, key) -> None:
        del self.value  # Not really applicable, but allowing deletion of the value

    def __call__(self, *args, **kwargs) -> None:
        print(f"Node called with args: {args}, kwargs: {kwargs}")

    def __iter__(self):
        yield self.value
        
    def __next__(self):
        raise StopIteration

    def __bool__(self) -> bool:
        return bool(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __int__(self) -> int:
        return int(self.value)

    def __repr__(self) -> str:
        return f"Node(value={self.__value})"

    def __reversed__(self):
        return reversed([self.value])  # Simple reversal of a single item list

    def __str__(self) -> str:
        return f"Node(value={self.__value})"