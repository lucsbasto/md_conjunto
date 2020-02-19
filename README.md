# md_conjunto - Trabalho de Matemática Discreta - 01

## Atividade:

Implemente uma API/Biblioteca com funcionalidades de conjuntos. Principalmente, forneça a implementação de um tipo de dados "Conjunto", que forneça operações e funcionalidades que implementam os conceitos relacionados a conjuntos vistos em aula.

## Definição de conjunto (Apostila):

Um conjunto é uma coleção de zero ou mais objetos distintos, chamados elementos do
conjunto, os quais não possuem qualquer ordem associada.

## Conforme solicitado pelo exercícios foi criado um programa que implementasse um tipo de dado Conjunto. Para este exercício foram criados dois arquivos, um que contém a classe Conjunto e outro que utiliza as funções existentes. Para o desenvolvimento da soluçao foi utilizado a linguagem de programação Python.

## 01 - Class Conjunto - arquivo conjunto.py

### Nesta classe existem os métodos reponsáveis por criar um conjunto. Para que um objeto possa ser iniciado existe o construtor da classe '**init**' que possui o parâmetro nome, que recebe o nome do conjunto.

### inserirElemento(self, valor) - método utilizado para adicionar um elemento ao conjunto. Esse método possui uma condição verificadora que não permite que elementos repetidos sejam adiciondos ao conjunto (armazenado em forma de lista).

### tamanhoConjunto(self) - retorna o tamanho do conjunto.

### imprimir(self) - imprime o conjunto formatado.

### pertence(elemento, conjunto) - método que recebe como parametro um elemento e um conjunto e retorna se o elemento passado pertence ao conjunto informado.

### eh_subconjunto(conjunto1, conjunto2) - método que recebe como parametro dois conjuntos e retorna se o conjunto1 é subconjunto do conjunto2. Ps: Para ser subconjunto um conjunto deve estar contido no outro conjunto.

### conjuntopropriamente(conjunto1, conjunto2) - método que recebe como parametro dois conjuntos e retorna se o conjunto1 é subconjunto próprio do conjunto2. PS: Para ser subconjunto próprio o conjunto A deve estar contido dentro do conjunto B e deve existir pelo menos um elemento no conjunto B que não está presente no conjunto A.

## 02 - Arquivo de teste - mainColecao.py

### import conjunto - Comando para ter acesso ao arquivo conjunto.

### c1.conjunto.Conjunto('Nome do conjunto') - Crianção do objeto c1 para criar um conjnuto e acessar seus métodos.

### c1.inserirElemento('X') - Insere elemento no conjunto.

### c1.tamanhoConjunto() - Retorna o tamanho do conjunto

### c2.conjunto.Conjunto('Nome do conjunto') - segundo objeto criado que permite a inserção de um conjunto dentro de outro conjunto.
