from typing import Optional

class HashTable:
    def __init__(self, size: int = 5)->None:
        self.__size = size
        self.__data_map = [None] * size
        
    @property
    def size(self)->int:
        return self.__size    
        
    def __hash(self, key: str)->int:
        """
        Generates a hash for a given key.

        This method takes a string key and computes its hash value using a 
        custom hashing algorithm. The hash value is calculated by iterating 
        over each character in the key, converting it to its ASCII value, 
        multiplying by 23, and then taking the modulus with the length of 
        the data map. The final hash value is the modulus of the computed 
        hash with the size of the hash table.

        Args:
            key (str): The key to be hashed.

        Returns:
            int: The hash value of the key.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.__data_map)
        return my_hash
    
    def set_item(self, key: str, value: str)->bool:
        """
        Inserts a key-value pair into the hash table.

        Args:
            key (str): The key to be inserted.
            value (str): The value to be associated with the key.

        Returns:
            bool: True if the item was successfully inserted.
        """
        index = self.__hash(key)
        if self.__data_map[index] is None:
            self.__data_map[index] = []
        self.__data_map[index].append([key, value])
        return True
    
    def get_item(self, key: str)->Optional[str]:
        """
        Retrieves the value associated with a given key.

        Args:
            key (str): The key to be searched.

        Returns:
            Optional[str]: The value associated with the key, or None if the key is not found.
        """
        index = self.__hash(key)
        
        if self.__data_map[index]:
            for item in self.__data_map[index]:
                if item[0] == key:
                    return item[1]
        return None
    
    def keys(self)->list:
        """
        Returns a list of all keys in the hash table.

        Returns:
            list: A list of all keys in the hash table.
        """
        all_keys = []
        for item in self.__data_map:
            if item:
                for key, _ in item:
                    all_keys.append(key)
        return all_keys
    
    def items(self)->list:
        """
        Returns a list of all key-value pairs in the hash table.

        Returns:
            list: A list of all key-value pairs in the hash table.
        """
        all_items = []
        for item in self.__data_map:
            if item:
                all_items.extend(item)
        return all_items
    
    def values(self)->list:
        """
        Returns a list of all values in the hash table.

        Returns:
            list: A list of all values in the hash table.
        """
        all_values = []
        for item in self.__data_map:
            if item:
                for _, value in item:
                    all_values.append(value)
        return all_values
        
    def __repr__(self)->str:
        return f"HashTable(size={self.__size})"
    
    def __str__(self)->str:
        lines = []
        for index, item in enumerate(self.__data_map):
            lines.append(f"{index}: {item}")
        return "\n".join(lines)
    
if __name__ == "__main__":
    ht = HashTable()
    print(ht)
    print(ht.size)
    ht.set_item("name", "John")
    ht.set_item("age", "25")
    ht.set_item("city", "New York")
    ht.set_item("country", "USA")
    ht.set_item("job", "Engineer")
    ht.set_item("company", "Google")
    ht.set_item("salary", "100000")
    ht.set_item("experience", "5 years")
    ht.set_item("degree", "Masters")
    ht.set_item("position", "Software Developer")
    print(ht)
    print(ht.size)
    print(ht.get_item("name"))
    print(ht.get_item("age"))
    print(ht.get_item("city"))
    print(ht.get_item("country"))
    print(ht.get_item("countries"))
    print(ht.keys())
    