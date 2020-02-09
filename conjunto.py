
class Conjunto():
	
	def __init__(self, nome):
		self.lista = []
		self.nome = nome
		
	def inserirElemento(self, valor):
		if valor not in self.lista:
			self.lista.append(valor) 

	def tamanhoConjunto(self):
		return len(self.lista)

	def imprimir(self):
		print(f'{self.nome.upper()} = {self.lista}')
	
		
#####################################

