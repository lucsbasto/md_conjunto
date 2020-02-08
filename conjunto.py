
class Conjunto():
	
	def __init__(self, nome):
		self.lista = []
		self.nome = nome
		
	def inserirElemento(self, valor):
		if valor in self.lista:
			return False
		self.lista.append(valor) 

	def tamanhoConjunto(self):
		return len(self.lista)

	def imprimir(self):
		print(f'Nome conjunto: {self.nome} \n Conjunto:{self.lista}')
	
		
#####################################

