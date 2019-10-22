"""
	Ejercicio 4
	@iancarlosortega
"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]

nombres = ["Ángel", "José", "Ana"]

promedios = list(map(lambda x:sum(x)/len(x) , paraleloA))

print(list(zip(promedios, nombres)))