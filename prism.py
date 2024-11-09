def calculate_volume(lista):
    if len(lista) == 0:
        return 0
    if len(lista) != 3:
        return -1
    volumen = 1
    for dimension in lista:
        volumen *= dimension
    return volumen 





    """ FUNCTIONALITY

    - Calculates volume of a 3 element list- OK

    - Check inputs:

            - Not a 3D list- OK
            - Empty list - OK
            - Not a number list 
            - How many decimals? """ 