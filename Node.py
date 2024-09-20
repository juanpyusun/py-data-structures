class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"{self.value}"
    
    def __repr__(self):
        return f"value:{self.value}, next:{self.next}"

    def __len__(self):
        return 1
  