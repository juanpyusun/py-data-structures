class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
            vertex: The vertex to be added to the graph.

        Returns:
            bool: True if the vertex was added successfully, False if the vertex already exists in the graph.
        """
        if vertex not in self.__adjacency_list.keys():
            self.__adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two vertices in the graph.

        Parameters:
        vertex1 (hashable): The first vertex.
        vertex2 (hashable): The second vertex.

        Returns:
        bool: True if the edge was successfully added, False otherwise.

        Note:
        Both vertices must already exist in the adjacency list for the edge to be added.
        """
        if vertex1 in self.__adjacency_list.keys() and vertex2 in self.__adjacency_list.keys():
            self.__adjacency_list[vertex1].append(vertex2)
            self.__adjacency_list[vertex2].append(vertex1)
            return True
        return False
        
    def remove_edge(self, vertex1, vertex2):
        """
        Removes the edge between two vertices in the graph.

        Parameters:
        vertex1 (hashable): The first vertex.
        vertex2 (hashable): The second vertex.

        Returns:
        bool: True if the edge was successfully removed, False otherwise.

        Note:
        If either vertex1 or vertex2 does not exist in the adjacency list, 
        or if there is no edge between them, the method will return False.
        """
        if vertex1 in self.__adjacency_list.keys() and vertex2 in self.__adjacency_list.keys():
            try:
                self.__adjacency_list[vertex1].remove(vertex2)
                self.__adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        """
        Removes a vertex and all its associated edges from the graph.

        Parameters:
        vertex (any): The vertex to be removed from the graph.

        Returns:
        bool: True if the vertex was successfully removed, False if the vertex was not found in the graph.
        """
        if vertex in self.__adjacency_list.keys():
            for other_vertex in self.__adjacency_list[vertex]:
                self.__adjacency_list[other_vertex].remove(vertex)
            del self.__adjacency_list[vertex]
            return True
        return False
        
    def __str__(self):
        """
        Returns a string representation of the graph.

        The string representation includes all vertices and their corresponding
        adjacency lists in a dictionary-like format.

        Returns:
            str: A string representation of the graph.
        """
        string = "{\n"
        for vertex in self.__adjacency_list.keys():
            string += f"  {vertex}: {self.__adjacency_list[vertex]}\n"
        return string + "}"
    