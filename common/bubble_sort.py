from typing import Any, List

def bubble_sort(my_list: List[Any]) -> List[Any]:
	# Vamos a recorrer el arreglo desde el ultimo elemento hasta el primero
	for i in range(len(my_list) - 1, 0, -1):
		for j in range(i):
			if my_list[j] > my_list[j + 1]:
				my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
	return my_list