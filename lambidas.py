lista = list(range(1, 101))

print(lista)

def dobro(x):
	return x * 2
dobro(3)

lista_dobro = map(dobro, lista)
lista_dobro = map(lambda x: x * 2, lista)
list(lista_dobro)
print(lista_dobro)