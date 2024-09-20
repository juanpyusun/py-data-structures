class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True # Esta linea es para una funcion posterior

    
    def __str__(self):
        temp = self.head
        string = ""
        while temp is not None:
            string += f"{temp.value} -> "
            temp = temp.next
        return string
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f"head:{self.head}, tail:{self.tail}, length:{self.length}"