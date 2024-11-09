"""

REQUIREMENTS
- The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
- Return the average of the marks array for the student name provided, showing 2 places after the decimal.

"""

""" 
- Calcula la nota media - OK
- Dos decimales - OK
- Diccionario con varios alumnos - OK
- Entrada vacía -  OK
- Lista vacía de notas - OK
- Diferente tipo de datos
- float/ int - OK
- Name no está en el diccionario- OK

"""

def nota_media(dic, name):
    if dic is None or name not in dic.keys():
        return None 
    lista_notas = dic[name]
    if len(lista_notas) == 0:
        return None
    promedio = round(sum(lista_notas)/ len(lista_notas), 2)
    return promedio