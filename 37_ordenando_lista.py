personas = ["sami", "luz", "sami","name"]
repite = max(set(personas), key = personas.count) #max es para saber cual es el elemento que mas se repite en la lista
print(repite)
print(personas.count(repite))

#set es para eliminar duplicados

for persona in personas:
   # print(persona)
    print(personas.index(persona)) #index es para saber la posicion de un elemento en la lista

print(personas.count("sami")) #count es para saber cuantas veces se repite un elemento en la lista
