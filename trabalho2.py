
import random


class Formiga:
    def __init__(self, partida, num):
        self.id = num
        self.solucao =[]
        self.solucao.append(partida)
    @staticmethod
    def evaporaferomonio(matrizflinha, matrizfauxlinha):
        print('ToDo')

    @staticmethod
    def addferomonio(self, matrizflinha,matrizfauxlinha):
        print('ToDo')

    @staticmethod
    def calcularota(self, matrizdlinha, matrizflinha):
        probabilidades = []
        possiveis = []
        for i in matrizdlinha:
            if i not in self.solucao:
                if i > 0:
                    possiveis.append(i)  #nó possivel é adicionado a lista de nós possíveis
                    probabilidades.append(self.calculaprob(self, i, 1, matrizdlinha, matrizflinha))
                    """"" 
                    acho que não é a melhor maneira de fazer isso, mas precisamos saber quais nós foram selecionados 
                    e temos que saber associar a probabilidade a esse nó, essa foi a maneira que consegui pensar"""
        selecionado = random.choices(possiveis, weights=probabilidades, k=1)
        self.solucao.append(selecionado)
        return selecionado

    @staticmethod
    def calculaprob(self, s, b, matrizdlinha, matrizflinha):
        """
        r = indice do nó atual
        s = nó destino
        b = peso do feromônio
        matrizdlinha = linha de indice r da matriz de distância
        matrizflinha = linha de indice r da matriz de feromônio
        visitadas = lista nós já visitados pela formiga
        """
        somad = 0
        somaf = 0
        """
        feromonio entre no atual e s(nó destino) multiplicado por 1/distancia entre os pontos r e s,
        tudo isso elevado a um b > 0
        sobre o somatorio do feromônio de todos os nós acessíveis de r multiplicado por somatorio de 1/distancia de
        todos os pontos acessíveis de r, tudo isso elevado a b
        retorna probabilidade da formiga escolher escolher a rota vindo de r indo para s
        """
        for i in range(0, len(matrizdlinha)):  #fazer os somatorios
            if matrizdlinha[i] > 0 & i not in self.solucao:  #até achar um valor > 0 que não foi visitado
                somad += 1 / matrizdlinha[i]  #se encontrar, adiciona 1/d no somatorio
                somaf += matrizflinha[i]  #adiciona o feromonio ao somatorio tambem
        probabilidade = pow((matrizflinha[s] * (1 / matrizdlinha[s])), b) / pow(somad * somaf, b)
        return probabilidade


def inicializamatrizes(n, matriz, matrizferomonio):
    listaaux = []
    lista = []  # auxiliar para passar os valores para a matriz
    for i in range(n):  # for para inicializar matrizes
        estring = f.readline()  # readline retorna uma string
        lista = [int(ele) for ele in estring.split()]
        matriz.append(lista)  # joga lista para a matriz
        listaaux.append(1)  # cria uma lista com n 0.1, n sendo o tamanho da linha da matriz
        matrizferomonio.append(listaaux)  # joga a lista criada para a matriz de feromonios
    return matriz, matrizferomonio


f = open("Entrada 10.txt", "r")
n = f.readline()  #tamanho da matriz
n = int(n)
matriz = []
matrizferomonio = []
ini=inicializamatrizes(n, matriz, matrizferomonio)
matriz = ini[0]
matrizferomonio = ini[1]
matrizferomonioaux = matrizferomonio
testelinhamatriz = matriz[1]
testelinhamatrizf = matrizferomonio[1]
Formiga1 = Formiga(1, 1)
Formiga1.calcularota(Formiga1, matriz[1], matrizferomonio[1])
print(Formiga1.solucao)
