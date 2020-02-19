
class Conjunto():
	
	def __init__(self, nome):
		self.lista = []
		self.nome = nome

	def conjunto(self):
		return self.lista
		
	def inserirElemento(self, valor):
		if valor not in self.lista:
			self.lista.append(valor) 

	def tamanhoConjunto(self):
		return len(self.lista)

	def pertence(self, elemento, conjunto):
		if elemento not in conjunto:
			return False
		return True

	def eh_subconjunto(self, conjunto1, conjunto2):
		for i in conjunto1:
			#print(i)
			if i not in conjunto2:
				return False
		return True

	
	def conjuntopropriamente(self, conjunto1, conjunto2):
		aux = False

		for i in conjunto1:
			#print(i)
			if i not in conjunto2:
				return False
		aux = True

		if aux == True:
			if conjunto1 == conjunto2:
				return False
		return True
			
		
	def imprimir(self):
		lista = str(self.lista)
		lista=lista.replace('[','{')
		lista=lista.replace(']','}')
		return f'{self.nome} = {lista}'
		#print(f'{self.nome.upper()} = {self.lista}')
	
		
#####################################

