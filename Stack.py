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

    def __str__(self)->str:
        temp = self.__top
        string = ""
        while temp:
            string += f"<- {temp.data} |"
            temp = temp.next
        return string + "|"
