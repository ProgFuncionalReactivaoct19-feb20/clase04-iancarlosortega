"""
	Ejercicio 1
	@iancarlosortega
"""

# Declaracion de listas

listaA = [10,2,3,4]

listaB = ["a","b","c","d"]

# Ordenar las listas de acuerdo a lo que pide el problema

lista1 = sorted(listaA)

lista2 = sorted(listaB, reverse = True) # Reverse para invertir la lista

listaFinal = list(zip(lista1,lista2)) # Zip para juntar las listas

maximo = max(listaFinal, key = lambda x:x[0]) # Max para sacar el maximo 

# Mostrar los resultados

print(listaFinal)
print(maximo)