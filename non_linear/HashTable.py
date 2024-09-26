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
 
# Ineficiente
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# Mejorado
def item_in_common(list1, list2):
    my_dict = {}
    for new_index in list1:
        my_dict[new_index] = True

    for element_to_compare in list2:
        if element_to_compare in my_dict:
            return True

    return False   

def find_duplicates(nums):
    # Create a dictionary to store the count of each number
    count_dict = {}
    duplicates = []

    # Count occurrences of each number
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find all numbers that appear more than once
    for num, count in count_dict.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

def first_non_repeating_char(string):
    # Create a dictionary to store the count of each character
    char_count = {}

    # Count occurrences of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for char in string:
        if char_count[char] == 1:
            return char

    return None  # Return None if there are no non-repeating characters

def group_anagrams(strings):
    # Create a dictionary to hold the groups of anagrams
    anagram_dict = {}

    # Iterate through each string in the input list
    for string in strings:
        # Sort the string to get the anagram key
        sorted_string = ''.join(sorted(string))
        
        # Add the original string to the corresponding anagram group
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]

    # Return the list of anagram groups
    return list(anagram_dict.values())

def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_dict = {}

    # Iterate over the list of numbers
    for index, num in enumerate(nums):
        # Calculate the complement that we need to find
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], index]  # Return the indices of the two numbers

        # Store the current number and its index in the dictionary
        num_dict[num] = index

    return []  # Return an empty list if no pair is found

def subarray_sum(nums, target):
    # Create a dictionary to store the cumulative sum and its index
    cumulative_sum_dict = {0: -1}  # Initialize with sum 0 at index -1
    current_sum = 0

    # Iterate through the list of numbers
    for index, num in enumerate(nums):
        current_sum += num  # Update the cumulative sum
        
        # Check if the (current_sum - target) exists in the dictionary
        if (current_sum - target) in cumulative_sum_dict:
            start_index = cumulative_sum_dict[current_sum - target] + 1
            return [start_index, index]  # Return the starting and ending indices

        # Store the current cumulative sum and its index
        cumulative_sum_dict[current_sum] = index

    return []  # Return an empty list if no subarray found

# Using Sets that also implements HashTables
def remove_duplicates(my_list):
    # Use a set to remove duplicates
    unique_values = set(my_list)
    # Convert the set back to a list
    return list(unique_values)

def has_unique_chars(input_string):
    # Create a set to store unique characters
    seen_chars = set()
    
    # Iterate over each character in the input string
    for char in input_string:
        # Check if the character has already been seen
        if char in seen_chars:
            return False  # Duplicate found, return False
        seen_chars.add(char)  # Add the character to the set
    
    return True  # All characters are unique

def find_pairs(arr1, arr2, target):
    # Convert arr1 to a set for efficient look-up
    arr1_set = set(arr1)
    pairs = []

    # Iterate through each number in arr2
    for num in arr2:
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in arr1_set
        if complement in arr1_set:
            pairs.append((complement, num))  # Append the pair as a tuple

    return pairs

def longest_consecutive_sequence(nums):
    # Use a set to store the numbers for O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    # Iterate through each number in the set
    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count the length of the consecutive sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak
    