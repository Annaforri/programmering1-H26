# Dette er 'programmet' vårt. Vi importerer modulen vi laget, jsonmodul.py, og bruker funksjonene vi definerte der.

import jsonmodul

# Lager en dictionary, som vi ønsker å skrive til en json-fil senere
planet = {"navn":"Merkur", "tyngdekraft":3.73}
# Lagrer filnavnet vi ønsker å bruke i en variabel
file_name = 'planet2.json'

# Bruker skriv_json()-funksjonen vi definerte i vår jsonmodul, og sender med variablene vi akkurat opprettt som argumenter
# Vi får nå opprettet en ny fil med navnet planet2.json, og som inneholder en string med vår dictionary 
jsonmodul.skriv_json(planet,file_name)

# Bruker les_json()-funksjonen vi definerte i vår jsonmodul, og sender med navnet på fila vi ønsker å lese inn fra (lagret i variabelen file_name)
dict_from_file = jsonmodul.les_json(file_name)

print(dict_from_file)            # ser at variabelen inneholder det samme som fila
print(type(dict_from_file))      # datatypen til variabelen er dictionary (fila er string)
print(dict_from_file['navn'])    # vi kan derfor bruke anlig dictionary-syntax på variabelen




