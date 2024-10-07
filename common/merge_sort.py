# Este metodo es distinto de los demas, dado que los demas hacen el ordenamiento in place, mientras que merge lo hace en otra lista la cual devuelve por aparte
# necesita un helper, una funcion para hacer parte del proceso
# list1 and list2 need to be sorted
def merge(list1, list2):
    if not list1:
        return list2
    
    if not list2:
        return list1
    combined = []
    i = 0 # index of list1
    j = 0 # index of list2
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
    	    combined.append(list1[i])
    	    i += 1
        else:
    	    combined.append(list2[j])
    	    j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list1):
        combined.append(list2[j])
        j += 1	  
    return combined

def merge_sort(my_list):
    # Paso 2: ... Hasta que se llegue al caso base when len(my_list) is 1
    if len(my_list) == 1:
        return my_list

    # Paso 1: Estas lineas de codigo  rompen la lista en la mitad recursivamente
    # aqui se debe analizar con el stack de llamada y la instancia de cada llamado de las funciones (cada item del stack), dado que hay varios return anidados por la recursividad
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    # Paso 3: Finalmente usamos merge() para (arre)juntar todo
    return merge(left, right)