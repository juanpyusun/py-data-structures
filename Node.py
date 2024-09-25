from typing import Optional

class Node:    
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