
import random


class Formiga:
    def __init__(self, partida, num):
        self.id = num
        self.solucao =[]
        self.solucao.append(partida)
        self.custo = 0
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
        for i in range(len(matrizdlinha)):
            if i not in self.solucao:
                if matrizdlinha[i] > 0:
                    possiveis.append(i)  #nó possivel é adicionado a lista de nós possíveis
        i=0
        for i in range(len(possiveis)): #percorre a lista de nós possiveis e calcula as probabilidades
            probabilidades.append(self.calculaprob(self, possiveis[i], 1, matrizdlinha, matrizflinha))
            # acho que não é a melhor maneira de fazer isso, mas precisamos saber quais nós foram selecionados
            # e temos que saber associar a probabilidade a esse nó, essa foi a maneira que consegui pensar

        if not bool(possiveis): #no python, se uma lista está vazia ela é considerada false
                if len(self.solucao) < 10:  #nada elegante, mas garante que todos os nos são visitadas
                    self.solucao = [0]  #reseta a solução, volta a ponto de partida e tenta de novo
                    self.custo = 0      #vai ser um problema quando tivermos o feromonio implementado, pois quando chega nesse
                    return 0            #ponto a formiga ja visitou muitos nos e ja depositou feromonio
                else:
                    return "finished"   #eu penso em criar mais uma matriz que salva os feromonios antes de uma formiga
                                        #percorrer o grafo e, se der errado, reseta a matriz feromonio
                  
                
        else:
            selecionado = random.choices(possiveis, weights=probabilidades, k=1)
            self.solucao.append(selecionado[0])  #random.choices retorna uma lista de 1 posição
            self.custo += matrizdlinha[selecionado[0]]  #acha na matriz de distância o indice do nó selecionado, e soma o custo
            return selecionado[0]

    @staticmethod
    def calculaprob(self, s, b, matrizdlinha, matrizflinha):
        """
        r = indice do nó atual
        s = indice do nó destino
        b = peso do feromônio
        matrizdlinha = linha de indice r da matriz de distância
        matrizflinha = linha de indice r da matriz de feromônio
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
        for i in range( len(matrizdlinha)):  #fazer os somatorios
            if matrizdlinha[i] > 0:
                if i not in self.solucao:  #até achar um valor > 0 que não foi visitado
                    somad = somad + 1 / matrizdlinha[i]  #se encontrar, adiciona 1/d no somatorio
                    somaf = somaf + matrizflinha[i]  #adiciona o feromonio ao somatorio tambem
        probabilidade = pow((matrizflinha[s] * (1 / matrizdlinha[s])), b) / pow(somad * somaf, b)
        return probabilidade


def inicializamatrizes(n, matriz, matrizferomonio):
    listaaux = [] # auxiliar para passar os valores para a matriz
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
ini=inicializamatrizes(n, matriz, matrizferomonio) #tamanho da matriz, matriz distancia e matriz feromonio
matriz = ini[0]
matrizferomonio = ini[1]
matrizferomonioaux = matrizferomonio
Formiga1 = Formiga(0, 1) #instanciamos uma formiga, com ponto de partida no nó 0 e a id 1
atual = 0
prox = 0
while prox!="finished":
    prox = Formiga1.calcularota(Formiga1, matriz[atual], matrizferomonio[atual]) #(instancia da formiga, ponto de partida, feromonio do ponto de partida)
    atual = prox
print(Formiga1.solucao)
print(Formiga1.custo)
