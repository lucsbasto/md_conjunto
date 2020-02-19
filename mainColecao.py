import conjunto 

c1 = conjunto.Conjunto('A')
c2 = conjunto.Conjunto('A')

c1.inserirElemento('B')
c1.inserirElemento('B')
c1.inserirElemento('A')
c1.inserirElemento('A')

print("Tamanho da Coleção:",c1.tamanhoConjunto())
c1.imprimir()

c2.inserirElemento('A')
#c2.inserirElemento(c1.lista)

#print("Tamanho da Coleção:",c2.tamanhoConjunto())
#c2.imprimir()
c1.inserirElemento(c2.conjunto())
print(c1.imprimir())

print(c1.pertence('A', c1.conjunto()))

print("c1:",c1.conjunto())
print("c2:",c2.conjunto())
print(c1.eh_subconjunto(c2.conjunto(), c1.conjunto()))
print("#################top")
print(c1.conjuntopropriamente(c2.conjunto(), c1.conjunto()))

#####################################

