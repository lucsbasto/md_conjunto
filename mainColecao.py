import conjunto 

c1 = conjunto.Conjunto('A')
c2 = conjunto.Conjunto('A')

c1.inserirElemento('B')
c1.inserirElemento('B')
c1.inserirElemento('A')
c1.inserirElemento('A')

print("Tamanho da Coleção:",c1.tamanhoConjunto())
c1.imprimir()

c2.inserirElemento('D')
c2.inserirElemento(c1.lista)

print("Tamanho da Coleção:",c2.tamanhoConjunto())
c2.imprimir()

#####################################

