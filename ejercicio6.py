"""
	Ejercicio 6
	@iancarlosortega
"""

paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]

promedios = list(map(lambda x:sum(x)/len(x) , paraleloA))

suma = list(map(lambda x:sum(x), paraleloA))

listaFinal = list(zip(promedios, suma, nombres))

print(list(filter(lambda x:x[0]<=5, listaFinal)))

