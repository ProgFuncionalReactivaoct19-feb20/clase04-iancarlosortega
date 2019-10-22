"""
	Ejercicio 2 : Encontrar la siguiente estructura
	@iancarlosortega
"""	


lista = [(100,2),(20,4),(30,1)]

lista2 = ["b","a","c"]

print(list(zip(sorted(lista2),sorted(lista,key = lambda x :x[1]))))