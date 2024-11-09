def bubblesort(list, desc=0):
    # this function receives two parametres: a list to sort and a flag that says if it will be ascending or descending
    length = len(list)
    for i in range(length -1):
        for j in range(length - 1 - i):
            if (list[j] > list [j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    if desc==1:
        list.reverse()
    return list

