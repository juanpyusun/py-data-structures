from typing import Optional

class Node:
    def __init__(self, value: int)->None:
        self.__value = value
        self.__left = None
        self.__right = None
    
    @property
    def value(self)->int:
        return self.__value
    
    @property
    def left(self)->Optional['Node']:
        return self.__left
    
    @property
    def right(self)->Optional['Node']:
        return self.__right
    
    @left.setter
    def left(self, node: 'Node')->None:
        self.__left = node
        
    @right.setter
    def right(self, node: 'Node')->None:
        self.__right = node
    
    @value.setter
    def value(self, value: int)->None:
        self.__value = value
    
    def __repr__(self)->str:
        return f"Node(value={self.__value})"
    
    def __str__(self)->str:
        return f"Node(value={self.__value})"
    
class BinarySearchTree:
    """
    BinarySearchTree is a class that implements a binary search tree (BST) data structure.
    A binary search tree is a node-based binary tree data structure which has the following properties:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - The left and right subtree each must also be a binary search tree.
    Attributes:
        __root (Node): The root node of the binary search tree.
        __length (int): The number of nodes in the binary search tree.
    Methods:
        __init__(value=None):
        __print_level(node, level, gap):
        __get_height(node):
        insert(value):
        search(value):
        __r_contains(current_node, value):
        r_contains(value):
        __r_insert(current_node, value):
        r_insert(value):
        __r_delete_node(current_node, value):
        find_min(current_node):
        r_delete_node(value):
        __repr__():
        __str__():
    """
    
    def __init__(self, value=None)->None:
        """
        Initializes a new instance of the BinarySearchTree class.

        Args:
            value (optional): The initial value to insert into the tree. Defaults to None.

        If a value is provided, a new node with that value is created and set as the root of the tree,
        and the length of the tree is set to 1. If no value is provided, the root is set to None and
        the length of the tree is set to 0.
        """
        if value:
            new_node = Node(value)
            self.__root = new_node
            self.__length = 1
        else:
            self.__root = None
            self.__length = 0
            
    def __print_level(self, node:Node, level:int, gap:str) -> str:
        """
        Recursively constructs a string representation of the nodes at a given level in the binary search tree.

        Args:
            node (Node): The current node being processed.
            level (int): The level of the tree to print.
            gap (str): A string used to format the output, typically for spacing.

        Returns:
            str: A string representation of the nodes at the specified level, with gaps for formatting.
        """
        if node is None:
            return gap + ".."
        if level == 1:
            return gap + str(node.value) + gap
        elif level > 1:
            left_str = self.__print_level(node.left, level - 1, gap)
            right_str = self.__print_level(node.right, level - 1, gap)
            return left_str + " " + right_str
        return ""

    def __get_height(self, node:Node) -> int:
        """
        Private method to calculate the height of a given node in the binary search tree.

        Args:
            node (Node): The node for which the height is to be calculated.

        Returns:
            int: The height of the node. Returns 0 if the node is None.
        """
        if node is None:
            return 0
        else:
            left_height = self.__get_height(node.left)
            right_height = self.__get_height(node.right)
            return 1 + max(left_height, right_height)
           
    def insert(self, value: int) -> bool:
        """
        Inserts a value into the binary search tree.
        Args:
            value (int): The value to be inserted into the tree.
        Returns:
            bool: True if the value was successfully inserted, False if the value already exists in the tree.
        Raises:
            None
        Example:
            bst = BinarySearchTree()
            bst.insert(10)  # Returns True
            bst.insert(5)   # Returns True
            bst.insert(10)  # Returns False
            """
        new_node = Node(value)
        
        if self.__root is None:
            self.__root = new_node
            self.__length += 1
            return True
        
        current_node = self.__root
        while True:
            if value == current_node.value:
                return False                
            
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    self.__length += 1
                    return True
                current_node = current_node.left
            
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    self.__length += 1
                    return True
                current_node = current_node.right
    
    def search(self, value: int) -> bool:
        """
        Searches for a value in the binary search tree.

        Args:
            value (int): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        if self.__root is None:
            return False
        
        current_node = self.__root
        while current_node:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
        return False
    
    def __r_contains(self, current_node: Node, value: int|str) -> bool:
        """
        Recursively searches for a value in the binary search tree.

        Args:
            current_node (Node): The current node being processed.
            value (int|str): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value: int|str) -> bool:
        """
        Searches for a value in the binary search tree using a recursive approach.

        Args:
            value (int|str): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        return self.__r_contains(self.__root, value)
    
    def __r_insert(self, current_node: Node, value: int) -> bool:
        """
        Recursively inserts a value into the binary search tree.

        Args:
            current_node (Node): The current node being processed.
            value (int): The value to be inserted into the tree.

        Returns:
            bool: True if the value was successfully inserted, False if the value already exists in the tree.
        """
        if current_node is None:
            self.__length += 1
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node            
        
    def r_insert(self, value: int) -> bool:
        """
        Recursively inserts a value into the binary search tree.

        Args:
            value (int): The value to be inserted into the tree.

        Returns:
            bool: True if the value was successfully inserted.
        """
        if self.__root is None:
            self.__root = Node(value)
        self.__r_insert(self.__root, value)
        return True
        
    def __r_delete_node(self, current_node: Node, value: int) -> Node:
        """
        Recursively deletes a node with a given value from the binary search tree.

        Args:
            current_node (Node): The current node being processed.
            value (int): The value of the node to be deleted.

        Returns:
            Node: The node that replaces the deleted node.
        """
        if current_node is None:
            return current_node
        if value < current_node.value:
            current_node.left = self.__r_delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.find_min(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete_node(current_node.right, sub_tree_min)
        return current_node
    
    def find_min(self, current_node: Node) -> int|str:
        """
        Method to find the minimum value in a subtree.

        This method traverses the left children of the given node until it 
        reaches the leftmost node, which contains the minimum value in the subtree.

        Args:
            current_node (Node): The root node of the subtree.

        Returns:
            int | str: The minimum value found in the subtree.
        """
        while current_node.left:
            current_node = current_node.left
        return current_node.value
    
    def r_delete_node(self, value: int) -> bool:
        """
        Recursively deletes a node with a given value from the binary search tree.

        Args:
            value (int): The value of the node to be deleted.

        Returns:
            bool: True if the value was successfully deleted.
        """
        self.__r_delete_node(self.__root, value)
        return True
    
    def is_balanced(self, node=None):
        """
        Check if the binary search tree is balanced.

        A binary search tree is considered balanced if, for every node, the height
        difference between the left and right subtrees is no more than 1.

        Args:
            node (TreeNode, optional): The root node of the subtree to check. 
                                       If None, the root of the entire tree is used.

        Returns:
            bool: True if the tree (or subtree) is balanced, False otherwise.
        """
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.__root if node is None else node)
        return balanced
        
    def inorder_traversal(self, node=None):
        """
        Perform an in-order traversal of the binary search tree.

        This method returns a list of elements in the tree in ascending order.

        Args:
            node (TreeNode, optional): The starting node for the traversal. 
                                       If None, the traversal starts from the root of the tree.

        Returns:
            list: A list of elements in the tree in ascending order.
        """
        if node is None:
            node = self.__root
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        """
        A helper function for performing an in-order traversal of the binary search tree.

        This function recursively traverses the tree in in-order (left, root, right) and appends
        the value of each visited node to the result list.

        Args:
            node (TreeNode): The current node being visited in the traversal.
            result (list): The list that accumulates the values of the nodes in in-order.
        """
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
                
    def sorted_list_to_bst(self, nums):
        """
        Converts a sorted list into a balanced binary search tree (BST).

        This method takes a sorted list of numbers and constructs a balanced BST
        from it. The root of the BST is stored in the instance variable `__root`.

        Args:
            nums (list): A list of numbers sorted in ascending order.

        Returns:
            None
        """
        self.__root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        """
        Converts a sorted list to a balanced binary search tree (BST).

        This function takes a sorted list and recursively constructs a balanced BST
        by selecting the middle element as the root and recursively doing the same
        for the left and right subtrees.

        Args:
            nums (List[int]): The sorted list of integers to be converted into a BST.
            left (int): The starting index of the current sublist.
            right (int): The ending index of the current sublist.

        Returns:
            Node: The root node of the balanced BST.
        """
        if left > right:
            return None

        mid = (left + right) // 2  # Find the middle index
        node = Node(nums[mid])  # Create a new tree node with the middle value

        # Recursively build the left and right subtrees
        node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        node.right = self.__sorted_list_to_bst(nums, mid + 1, right)

        return node

    def invert(self):
        """
        Inverts the binary search tree, swapping the left and right children
        of all nodes in the tree.

        This method calls a private helper method to perform the inversion
        starting from the root of the tree.
        """
        self.__invert_tree(self.__root)

    def __invert_tree(self, node):
        """
        Inverts the binary tree starting from the given node.
        This method swaps the left and right children of each node in the tree,
        effectively mirroring the tree.
        Args:
            node (TreeNode): The root node of the subtree to invert.
        Returns:
            TreeNode: The root node of the inverted subtree.
        """
        if node is None:
            return None
        
        # Swap the left and right children
        node.left, node.right = node.right, node.left
        
        # Recursively invert the left and right subtrees
        self.__invert_tree(node.left)
        self.__invert_tree(node.right)
        
        return node  # Return the root of the inverted tree

    # Breadth First Search Method
    def BFS(self):
        current_node = self.__root
        queue = []
        results = []
        queue.append(current_node)
    
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    # Depth First Search Pre-Order Method
    def dfs_pre_order(self):
        results = []
    
        # Recursive function to move on the BST
        def traverse(current_node):
            results.append(current_node.value)        
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
      
        # Aqui se llama la funcion recursiva
        traverse(self.__root)
        return results

    # Depth First Search Post-Order Method
    def dfs_post_order(self):
        results = []
      
        def traverse(current_node):        
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
      
        traverse(self.__root)
        return results

    # Depth First Search In-Order Method
    def dfs_in_order(self):
        results = []

        def traverse(current_node):        
            if current_node.left:
                traverse(current_node.left)        
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        
        traverse(self.__root)
        return results

    def is_valid_bst(self):
        # Get the node values in in-order traversal
        values = self.dfs_in_order()
        
        # Check if the values are in ascending order
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:  # If the current value is not greater than the previous
                return False
        return True

    def kth_smallest(self, k):
        self.kth_counter = 0
        self.kth_result = None
        
        def traverse(current_node):
            if current_node is None or self.kth_result is not None:
                return
            
            traverse(current_node.left)
            
            self.kth_counter += 1
            if self.kth_counter == k:
                self.kth_result = current_node.value
                return
            
            traverse(current_node.right)
        
        traverse(self.root)
        return self.kth_result


    def __repr__(self)->str:
        """
        Return a string representation of the BinarySearchTree instance.

        Returns:
            str: A string that represents the BinarySearchTree instance, 
                 including its length.
        """
        return f"BinarySearchTree(length={self.__length})"

    def __str__(self) -> str:
        """
        Returns a string representation of the binary search tree.

        The tree is represented level by level, with each level on a new line.
        Nodes at the same level are separated by spaces.

        Returns:
            str: A string representation of the binary search tree.
        """
        levels = []
        height = self.__get_height(self.__root)
        for level in range(1, height + 1):
            level_str = self.__print_level(self.__root, level, " ")
            levels.append(level_str)
        return "\n".join(levels)
