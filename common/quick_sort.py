from typing import List, Any

# Helper function to quick_sort 
def pivot(my_list: List[Any], pivot_index: int, end_index: int) -> int:
    swap_index = pivot_index
    
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    # Al ser la lista un objeto mutable, la siguiente funcion hara el cambio en el propio objeto, por eso no es necesario instanciarla
    swap(my_list, pivot_index, swap_index)
    return swap_index


def swap(my_list: List[Any], index1: int, index2: int) -> None:
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    
def quick_sort_helper(my_list: List[Any], left: int, right: int) -> List[Any]:
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list: List[Any]) -> List[Any]:
    return quick_sort_helper(my_list, 0, len(my_list) - 1)
