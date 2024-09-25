from Node import Node
from typing import Optional

class Stack:
    def __init__(self, value=None)->None:
        if value:
            new_node = Node(value)
            self.__top = new_node
            self.__height = 1
        else:
            self.__top = None
            self.__height = 0
    
    def pop(self)->Optional[Node]:
        if self.__height == 0:
	      return None
	  temp = self.__top
	  self.__top = self.__top.next
	  temp.next = None
	  self.__height -= 1
	  return temp

    def push(self, value:int|str)->None:
        new_node = Node(value)
	  if self.__height == 0:
	      self.__top = new_node
	  else:
	      new_node.next = self.__top
		self.__top = new_node
	 
        self.__height += 1
	  return True		

    def __str__(self)->str:
        temp = self.__top
        string = ""
        while temp:
            string += f"<- {temp.data} |"
            temp = temp.next
        return string + "|"



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

