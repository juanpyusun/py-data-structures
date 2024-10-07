""" Problema # 1
List: Remove Element
Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.
The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.

Input:
A list of integers nums .
An integer val representing the value to be removed from the list.

Output:
An integer representing the new length of the modified list after removing all occurrences of val.

Constraints:
Do not use any built-in list methods, except for pop() to remove elements.
It is okay to have extra space at the end of the modified list after removing elements.
"""
def remove_element(nums, val):
    # Pointer to keep track of the position of the next element to keep
    position = 0
    
    # Iterate through the list
    for i in range(len(nums)):
        # If the current element is not the value to be removed
        if nums[i] != val:
            # Move the current element to the 'position' index
            nums[position] = nums[i]
            # Increment the position pointer
            position += 1
    
    # Remove the unwanted elements from the end of the list (optional)
    # This is just for clarity, as the problem allows extra space at the end
    while len(nums) > position:
        nums.pop()
    
    return position

# Example usage
nums = [3, 2, 2, 3]
val = 3
new_length = remove_element(nums, val)
print("New length:", new_length)  # Output: New length: 2
print("Modified list:", nums)      # Output: Modified list: [2, 2]

""" Problema # 2
List: Find Max Min
Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.
The function should have the following signature:

def find_max_min(myList):

Where myList is the list of integers to search for the maximum and minimum values.
The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.
For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value.
"""
def find_max_min(myList):
    # Check if the list is empty
    if not myList:
        return None  # or raise an exception

    # Initialize max and min with the first element of the list
    max_value = myList[0]
    min_value = myList[0]
    
    # Traverse through the list
    for num in myList:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
            
    # Return the max and min as a tuple
    return (max_value, min_value)

# Example usage
myList = [5, 3, 8, 1, 6, 9]
result = find_max_min(myList)
print("Max and Min:", result)  # Output: Max and Min: (9, 1)

""" Problema # 3
List: Find Longest String ( ** Interview Question)
Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.

Example:
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'
"""
def find_longest_string(string_list):
    # Check if the list is empty
    if not string_list:
        return None  # return "" or raise an exception

    # Initialize the longest string with the first element
    longest_string = string_list[0]
    
    # Iterate through each string in the list
    for string in string_list:
        # If the current string is longer than the longest_string
        if len(string) > len(longest_string):
            longest_string = string
            
    # Return the longest string found
    return longest_string

# Example usage
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # Output: 'banana'

""" Problema # 4
List: Remove Duplicates
Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.
Your function should return the new length of the list containing only unique elements. Note that you should not create a new list or use any additional data structures to solve this problem. The original list should be modified in-place.

Constraints:
The input list is sorted in non-decreasing order.
The input list may contain duplicates.
The function should have a time complexity of O(n), where n is the length of the input list.
The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new lists (this also means you cannot use a set like we did earlier in the course).

Example:
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] Function call: new_length = remove_duplicates(nums) Output: new_length = 5 Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)
Explanation: The function modifies the original list nums in-place, moving unique elements to the beginning of the list, followed by duplicate elements. The new length returned by the function is 5, indicating that there are 5 unique elements in the list. The first 5 elements of the modified list nums are the unique elements [0, 1, 2, 3, 4].

This code:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])

Should Output:
New length: 5
Unique values in list: [0, 1, 2, 3, 4]
"""
def remove_duplicates(nums):
    # Check if the list is empty
    if not nums:
        return 0  # If empty, return length 0

    # Initialize a pointer for the position of unique elements
    unique_position = 1

    # Iterate through the list starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous one
        if nums[i] != nums[i - 1]:
            # Place the unique element at the unique_position index
            nums[unique_position] = nums[i]
            # Increment the unique_position
            unique_position += 1

    # Return the length of the unique elements
    return unique_position

# Example usage
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)  # Output: New length: 5
print("Unique values in list:", nums[:new_length])  # Output: Unique values in list: [0, 1, 2, 3, 4]

""" Problema # 5
List: Max Profit ( ** Interview Question)
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.
You are allowed to buy one share of the stock on one day and sell it on a later day.
Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.
Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:
Each element of the input list is a positive integer representing the stock price for a specific day.

Function signature: def max_profit(prices):
Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""
def max_profit(prices):
    # Check if the list is empty or has less than 2 prices
    if not prices or len(prices) < 2:
        return 0  # No profit can be made

    # Initialize the minimum price to the first price and maximum profit to 0
    min_price = prices[0]
    max_profit = 0

    # Iterate through the stock prices
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the profit if selling at the current price
        current_profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Maximum Profit:", profit)  # Output: Maximum Profit: 5

""" Problema # 6
List: Rotate
You are given a list of n integers and a non-negative integer k.
Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.
The function should modify the input list in-place, and you should not return anything.

Constraints:
Each element of the input list is an integer.
The integer k is non-negative.

Function signature: def rotate(nums, k):
Example:
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Function call: rotate(nums, k)
Output: nums = [5, 6, 7, 1, 2, 3, 4]

Explanation: The list has been rotated to the right by 3 steps:
[7, 1, 2, 3, 4, 5, 6]
[6, 7, 1, 2, 3, 4, 5]
[5, 6, 7, 1, 2, 3, 4]
"""
def rotate(nums, k):
    # Get the length of the list
    n = len(nums)
    
    # Handle the case where k is greater than n
    if n == 0:
        return  # If the list is empty, do nothing
    k = k % n  # Normalize k to avoid unnecessary full rotations

    # Reverse the entire list
    nums.reverse()
    
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    
    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated list:", nums)  # Output: Rotated list: [5, 6, 7, 1, 2, 3, 4]

""" Problema # 6
List: Max Sub Array ( ** Interview Question)
Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.
Remember to also account for an array with 0 items.

Function Signature:
def max_subarray(nums):

Input:
A list of integers nums.

Output:
An integer representing the sum of the contiguous subarray with the largest sum.

Example:
max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output: 6
Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
"""
def max_subarray(nums):
    # Check if the list is empty
    if not nums:
        return 0  # Or raise an exception based on the requirements

    # Initialize variables
    max_sum = nums[0]  # This will hold the maximum sum found
    current_sum = nums[0]  # This will hold the current subarray sum

    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update current_sum to include the current number
        # If current_sum + num is less than num, start a new subarray
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
result = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Maximum subarray sum:", result)  # Output: Maximum subarray sum: 6