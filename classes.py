class Pessoa:
	def _init_(self, nome, id):
		self.nome = nome
		self.id = id

	def getNome(self):
		return self.nome

	def getID(self):
		return self.id

p1 = Pessoa('kayque', 1)
p2 = Pessoa('joana', 2)

print(p1.getNome)
print(p2.getNome)