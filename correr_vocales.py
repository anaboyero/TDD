""" 
Devuelve una cadena con las vocales corridas un lugar.

- sencillo ✓
- consonantes? ✓
- cadena vacía? ✓
- otro tipo diferente? ✓
- None ✓
- mayusculas/ min? ✓
- frase mas complicada


"""






def correr_vocales(my_string):

    if my_string is None:
         return "No hay ninguna cadena que transformar"
    if my_string == "":
         return ""
    
    if not isinstance(my_string, str):
        return "Por favor, introduzca una cadena de texto"
    
    cadena = ""
    for letter in my_string:
        if letter.isupper():
            mayuscula = True
        else: 
            mayuscula = False
        
        letter = letter.lower()
    
        if letter == 'a' and mayuscula:
                cadena += 'E'
        elif letter == 'a':
            cadena += 'e'

        elif letter == 'e' and mayuscula:
                cadena += 'I'
        elif letter == 'e':
            cadena += 'i'

        elif letter == 'i' and mayuscula:
                cadena += 'O'
        elif letter == 'i':
            cadena += 'o'

        elif letter == 'o' and mayuscula:
                cadena += 'U'
        elif letter == 'o':
            cadena += 'u'

        elif letter == 'u' and mayuscula:
                cadena += 'A'
        elif letter == 'u':
            cadena += 'a'
        else:
            if (mayuscula):
                cadena += letter.upper() 
            else:           
                cadena += letter 
    return cadena


"""
ULTIMA V



def correr_vocales(my_string):
    cadena = ""
    vocales_min = "aeiou"
    vocales_may = "AEIOU"

    for letter in my_string:
        if letter in vocales_may:
            mayuscula = True
        else: 
            mayuscula = False
        
        letter = letter.lower()
    
        if letter == 'a' and mayuscula:
                cadena += 'E'
        elif letter == 'a':
            cadena += 'e'

        elif letter == 'e' and mayuscula:
                cadena += 'I'
        elif letter == 'e':
            cadena += 'i'

        elif letter == 'i' and mayuscula:
                cadena += 'O'
        elif letter == 'i':
            cadena += 'o'

        elif letter == 'o' and mayuscula:
                cadena += 'U'
        elif letter == 'o':
            cadena += 'u'

        elif letter == 'u' and mayuscula:
                cadena += 'A'
        elif letter == 'u':
            cadena += 'a'
        else:
            if (mayuscula):
                cadena += letter.upper() 
            else:           
                cadena += letter 
    return cadena

    
"""