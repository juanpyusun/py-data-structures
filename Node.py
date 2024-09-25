from typing import Optional

class Node:    
    def __init__(self, initdata) -> None:
        self.__data = initdata  # Using __data to indicate it's a "private" attribute
        self.__next = None  # The next node is initialized as None
        self.__prev = None  # The previous node is initialized as None
        
    @property
    def prev(self) -> Optional['Node']:
        return self.__prev

    @prev.setter
    def prev(self, newprev: Optional['Node']) -> None:
        self.__prev = newprev
        
    @property
    def data(self) -> int | str:
        return self.__data

    @data.setter
    def data(self, newdata: int | str) -> None:
        self.__data = newdata

    @property
    def next(self) -> Optional['Node']:
        return self.__next

    @next.setter
    def next(self, newnext: Optional['Node']) -> None:
        self.__next = newnext

    def __repr__(self) -> str:
        return f"Node(data={self.__data})"

    def __str__(self) -> str:
        return f"Node(data={self.__data})"

    def __eq__(self, other: 'Node') -> bool:
        if isinstance(other, Node):
            return self.__data == other.data
        return NotImplemented

    def __ne__(self, other: 'Node') -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.__data)

    def __len__(self) -> int:
        return 1

    # Arithmetic operations
    def __add__(self, other: 'Node') -> 'Node':
        return Node(self.data + other.data)

    def __sub__(self, other: 'Node') -> 'Node':
        return Node(self.data - other.data)

    def __mul__(self, other: 'Node') -> 'Node':
        return Node(self.data * other.data)

    def __truediv__(self, other: 'Node') -> 'Node':
        return Node(self.data / other.data)

    def __floordiv__(self, other: 'Node') -> 'Node':
        return Node(self.data // other.data)

    def __mod__(self, other: 'Node') -> 'Node':
        return Node(self.data % other.data)

    def __pow__(self, other: 'Node') -> 'Node':
        return Node(self.data ** other.data)

    def __lshift__(self, other: 'Node') -> 'Node':
        return Node(self.data << other.data)

    def __rshift__(self, other: 'Node') -> 'Node':
        return Node(self.data >> other.data)

    # Bitwise operations
    def __and__(self, other: 'Node') -> 'Node':
        return Node(self.data & other.data)

    def __or__(self, other: 'Node') -> 'Node':
        return Node(self.data | other.data)

    def __xor__(self, other: 'Node') -> 'Node':
        return Node(self.data ^ other.data)

    # In-place operations
    def __iadd__(self, other: 'Node') -> 'Node':
        self.data += other.data
        return self

    def __isub__(self, other: 'Node') -> 'Node':
        self.data -= other.data
        return self

    def __imul__(self, other: 'Node') -> 'Node':
        self.data *= other.data
        return self

    def __itruediv__(self, other: 'Node') -> 'Node':
        self.data /= other.data
        return self

    def __ifloordiv__(self, other: 'Node') -> 'Node':
        self.data //= other.data
        return self

    def __imod__(self, other: 'Node') -> 'Node':
        self.data %= other.data
        return self

    def __ipow__(self, other: 'Node') -> 'Node':
        self.data **= other.data
        return self

    def __ilshift__(self, other: 'Node') -> 'Node':
        self.data <<= other.data
        return self

    def __irshift__(self, other: 'Node') -> 'Node':
        self.data >>= other.data
        return self

    # Unary operations
    def __pos__(self) -> 'Node':
        return Node(+self.data)

    def __neg__(self) -> 'Node':
        return Node(-self.data)

    def __invert__(self) -> 'Node':
        return Node(~self.data)

    def __abs__(self) -> 'Node':
        return Node(abs(self.data))

    # Comparison operations
    def __lt__(self, other: 'Node') -> bool:
        return self.data < other.data

    def __le__(self, other: 'Node') -> bool:
        return self.data <= other.data

    def __gt__(self, other: 'Node') -> bool:
        return self.data > other.data

    def __ge__(self, other: 'Node') -> bool:
        return self.data >= other.data

    def __contains__(self, item) -> bool:
        return self.data == item

    def __getitem__(self, key) -> 'Node':
        return self  # Not really applicable, but returning self for demonstration

    def __setitem__(self, key, value) -> None:
        self.data = value  # Not really applicable but setting self.data for demonstration

    def __delitem__(self, key) -> None:
        del self.data  # Not really applicable, but allowing deletion of the data

    def __call__(self, *args, **kwargs) -> None:
        print(f"Node called with args: {args}, kwargs: {kwargs}")

    def __iter__(self):
        yield self.data
        
    def __next__(self):
        raise StopIteration

    def __bool__(self) -> bool:
        return bool(self.data)

    def __float__(self) -> float:
        return float(self.data)

    def __int__(self) -> int:
        return int(self.data)

    def __repr__(self) -> str:
        return f"Node(data={self.__data})"

    def __reversed__(self):
        return reversed([self.data])  # Simple reversal of a single item list

    def __str__(self) -> str:
        return f"Node(data={self.__data})"