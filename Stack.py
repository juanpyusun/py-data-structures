from typing import Optional

class Node:    
    def __init__(self, value)->None:
        self.__value = value
        self.__next = None

    @property
    def value(self)->int|str:
        return self.__value

    def __repr__(self)->str:
        return f"Node(value={self.__value})"

    def __str__(self)->str:
        return f"Node(value={self.__value})"

class Stack:
    """
    Stack is a class that implements a basic stack data structure with push and pop operations.
    Attributes:
        __top (Node): The top node of the stack.
        __height (int): The current height of the stack.
    Methods:
        __init__(value: Optional[int|str] = None) -> None:
            Initializes the stack. If a value is provided, it creates a new node with that value as the top node.
        pop() -> Optional[Node]:
            Removes and returns the top node of the stack. If the stack is empty, returns None.
        push(value: int|str) -> None:
            Adds a new node with the given value to the top of the stack.
        __str__() -> str:
            Returns a string representation of the stack, showing all the values from top to bottom.
    """
    
    def __init__(self, value=None)->None:
        """
        Initializes a new Stack instance.

        Args:
            value (optional): The initial value to be added to the stack. 
                              If provided, a new node with this value is created 
                              and set as the top of the stack. Defaults to None.

        Attributes:
            __top (Node or None): The top node of the stack. None if the stack is empty.
            __height (int): The height of the stack. 0 if the stack is empty.
        """
        if value:
            new_node = Node(value)
            self.__top = new_node
            self.__height = 1
        else:
            self.__top = None
            self.__height = 0
    
    def is_empty(self)->bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.__height == 0
    
    def peek(self)->Optional[int|str]:
        """
        Returns the value of the top element of the stack without removing it.

        Returns:
            Optional[int|str]: The value of the top element if it exists, otherwise None.
        """
        if self.__height == 0:
            return None
        return self.__top.value
    
    def pop(self)->Optional[Node]:
        """
        Removes and returns the top element of the stack.

        Returns:
            Optional[Node]: The top element of the stack if it exists, otherwise None.
        """
        if self.__height == 0:
            return None
        temp = self.__top
        self.__top = self.__top.next
        temp.next = None
        self.__height -= 1
        return temp

    def push(self, value:int|str)->None:
        """
        Pushes a new value onto the stack.
        Args:
            value (int | str): The value to be pushed onto the stack. It can be either an integer or a string.
        Returns:
            None
        """
        new_node = Node(value)
        if self.__height == 0:
            self.__top = new_node
        else:
            new_node.next = self.__top
        self.__top = new_node

        self.__height += 1
        return True		

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        The string is formatted such that each element in the stack is 
        represented by its value, with arrows indicating the order from 
        top to bottom.

        Returns:
            str: A string representation of the stack.
        """
        temp = self.__top
        string = ""
        while temp:
            string += f"<- {temp.value} |"
            temp = temp.next
        return string + "|"


# METODOS ADICIONALES
def is_balanced_parentheses(s):
    stack = Stack()
    
    for char in s:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False  # More closing parentheses
            stack.pop()  # Match found for the last open parenthesis
    
    return stack.is_empty()

def reverse_string(string):
    stack = Stack()
    
    # Push each character onto the stack
    for char in string:
        stack.push(char)
    
    reversed_string = ""
    
    # Pop each character from the stack to form the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

def sort_stack(input_stack):
    sorted_stack = Stack()
    
    while not input_stack.is_empty():
        # Pop the top element from the input stack
        temp = input_stack.pop()

        # While sorted_stack is not empty and its top element is greater than temp
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            # Pop from sorted_stack and push back to input_stack
            input_stack.push(sorted_stack.pop())

        # Push temp onto sorted_stack
        sorted_stack.push(temp)

    # Transfer elements back to the input_stack
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())

