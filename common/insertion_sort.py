from typing import List, Any

def insertion_sort(my_list: List[Any]) -> List[Any]:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1

        # Move elements of my_list[0..i-1], that are greater than temp,
        # to one position ahead of their current position
        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1

        my_list[j + 1] = temp

    return my_list