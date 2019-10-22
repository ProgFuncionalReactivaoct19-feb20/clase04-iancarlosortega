"""
"""

lista = [(100, 2), (20, 4), (30, 1)]

lista2 = ["b", "a", "c"]

lista3 = list(map(lambda x:x.upper(), lista2))

print(list(zip(sorted(lista), sorted(lista3, reverse=True))))