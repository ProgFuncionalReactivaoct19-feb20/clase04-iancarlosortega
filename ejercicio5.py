"""
	Ejercicio 5
	@iancarlosortega
"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]

nombres = ["Ángel", "José", "Ana"]

promedios = list(map(lambda x:sum(x)/len(x) , paraleloA))

listaFinal = list(zip(promedios,nombres))

maximo = max(listaFinal, key=lambda x:x)

print(listaFinal)

print(maximo)

print(list(sorted(listaFinal, key=lambda x:x[1])))
