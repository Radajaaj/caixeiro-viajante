
import random
import numpy as np

numeroNos = 10      #Armazena o número de nós do grafo.


#ATENÇÃO!! MATRIZ DE FEROMONIO ---> Lembre que a matriz tem que ser simétrica, então tipo:
                                                    #matriz[x][y] = feromonio
                                                    #matriz[y][x] = feromonio tambem, pra ficar simetrico


#Classe formiga. Para cada nova formiga, será necessário instanciar uma nova classe
class Formiga:
    def __init__(self, partida, num):   #"Parâmetros privados"
        self.id = num               #Identificador da formiga. Usado apenas nos gráficos
        self.solucao =[]            #Vetor final que armazena o caminho andado pela formiga
        self.visitados=[]           #Vetor que armazena quais cidades ela já visitou. Pode ser essencial caso a gente for adicionar a busca por profundidade
        self.solucao.append(partida)
        self.custo = 0              #Custo da solução encontrada pela formiga
    #@staticmethod
    #def evaporaferomonio(matrizflinha, matrizfauxlinha):  #isso deve ser uma função no #escopo externo e não um metodo da classe formiga.
    #    print('ToDo')                                       #Func que vai evaporar o #feromonio da matriz
#
    #@staticmethod
    #def addferomonio(self, matrizflinha,matrizfauxlinha):   #Feromonio é soltado pela #formiga na matrizflinha
    #    print('ToDo')

    @staticmethod
    def calcularota(self, matrizdlinha, matrizflinha):      # Atualmente, as rotas são calculadas por força bruta. É quase impossível achar uma rota válida para grafos grandes
        probabilidades = []
        possiveis = []
        for i in range(len(matrizdlinha)):
            if i not in self.visitados:
                if matrizdlinha[i] > 0:
                    possiveis.append(i)  #nó possivel é adicionado a lista de nós possíveis
        i=0
        for i in range(len(possiveis)): #percorre a lista de nós possiveis e calcula as probabilidades
            probabilidades.append(self.calculaprob(self, possiveis[i], 1, matrizdlinha, matrizflinha))
            # acho que não é a melhor maneira de fazer isso, mas precisamos saber quais nós foram selecionados
            # e temos que saber associar a probabilidade a esse nó, essa foi a maneira que consegui pensar

        if not bool(possiveis): #no python, se uma lista está vazia ela é considerada false
                if (len(self.solucao) != numeroNos) or (self.solucao[0] != self.solucao[len(self.solucao)-1]):  #nada elegante, mas garante que todos os nos são visitadas
                    self.solucao = [partida]
                    self.visitados = [] #reseta a solução, volta a ponto de partida e tenta de novo
                    self.custo = 0
                    return 0
                else:
                    return "finished"
        else:
            selecionado = random.choices(possiveis, weights=probabilidades, k=1)
            self.solucao.append(selecionado[0])
            self.visitados.append(selecionado[0])  #random.choices retorna uma lista de 1 posição
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
                if i not in self.visitados:  #até achar um valor > 0 que não foi visitado
                    somad = somad + 1 / matrizdlinha[i]  #se encontrar, adiciona 1/d no somatorio
                    somaf = somaf + matrizflinha[i]  #adiciona o feromonio ao somatorio tambem
        probabilidade = pow((matrizflinha[s] * (1 / matrizdlinha[s])), b) / pow(somad * somaf, b)
        return probabilidade


def inicializamatrizes(n, matriz, matrizFeromonio):             
    listaaux = [] # auxiliar para passar os valores para a matriz
    for i in range(n):  # for para inicializar matrizes
        estring = f.readline()  # readline retorna uma string
        lista = [int(ele) for ele in estring.split()]
        matriz.append(lista)  # joga lista para a matriz
        listaaux.append(1)  # cria uma lista com n 0.1, n sendo o tamanho da linha da matriz
        matrizFeromonio.append(listaaux)  # joga a lista criada para a matriz de feromonios
    return matriz, matrizFeromonio


#int main() {
    
#[------------- Vamos pegar os parâmetros do usuário:
op = input("Deseja usar parâmetros padrão? [1 - Sim] [~1 - Não]\nR: ") 

if op == 1:
    #[------ Primeiro, pegamos o endereço do arquivo com o grafo:
    f = open(input("Insira o endereço do arquivo com o grafo (ex: Grafos/Entrada 10.txt)\nR: "), "r") # f vai ser um ponteiro para o arquivo aberto (?)

    #[------ Agora, pedimos pro usuário definir o número de formigas
    nFormigas = input("Quantas formigas terão na colônia?\nR: ")

    #[------ E definimos o nó de saída das formigas
    randomFlag = False
    partida = input("As formigas sairão de um único nó [0], ou de um nó aleatório [1]?\nR: ")
    if partida == 0:
        partida = input("De que nó as formigas sairão?\nR: ")
    else:
        randomFlag = True

    #[------ E também pedimos pro usuário definir as variáveis
    alpha = input("Defina o valor de Alpha (Sugestão = 1)\nR: ")    # Importancia do feromonio
    beta  = input("Defina o valor de Beta (Sugestão = 1)\nR: ")     # Importancia da distancia
    sigma = input("Defina o valor de Sigma (Sugestão = 0.01)\nR: ") # Fator de esvaecimento do feromônio
    Tij   = input("Defina o valor de Ti,j (Sugestão = 0.1)\nR: ")
    Q     = input("Defina o valor de Q (Sugestão = 10)\nR: ")       # Constante de atualização do feromônio
    

    #[------ Também pedimos para ele especificar uma convergência prematura
    convPrematura = input("Quantas soluções repetidas definem uma convergência prematura (Sugestão = 10)\nR: ")
else:
    #[------ Parâmetros genéricos
    f = open("Grafos/Entrada 10.txt", "r")  
    nFormigas = 10                       # Número de formigas
    randomFlag = True
    partida = 4                         # Ponto de partida
    alpha, beta, sigma, Tij, Q = 1, 1, 0.01, 0.1, 10    #Parâmetros
    convPrematura = 10                  # Num máximo de soluções repetidas


#[------------- Abrimos o arquivo, e obtemos o número de nós do grafo
numeroNos = f.readline()                # Vai armazenar a ordem da matriz / número de nós do grafo
numeroNos = int(numeroNos)
print("Temos ", numeroNos, " cidades")

#[------------- Inicializamos as matrizes
matriz = []                             # Armazena a tabela de caminhos do grafo
matrizFeromonio = []                    # Armazena os feromônios nos caminhos - Usada na decisão entre caminhos
feromDepositado = []                    # Armazena os feromônios soltos pelas formigas

#[------------- Lemos os conteúdos do arquivo, e colocamos na matriz matriz[][]
ini = inicializamatrizes(numeroNos, matriz, matrizFeromonio) #tamanho da matriz, matriz distancia e matriz feromonio
matriz = ini[0]                         # A função retorna duas matrizes: Uma com os conteúdos do arquivo
matrizFeromonio = ini[1]                # E oura com a intensidade dos feromônios iniciada em 
feromDepositado = [[0 for _ in range(numeroNos)] for _ in range(numeroNos)] # Inicializamos ela em 0


#[------------- Loop de execução do algoritmo:
for i in range(nFormigas):
    
    if randomFlag == True:              # Caso o usuário querer que o ponto de partida/chegada seja aleatório...
        partida = random.randint(0, numeroNos - 1)  # O teto faz parte do conjunto de saída
        
    formiguinha = Formiga(partida, i)   # Instanciamos uma formiga, com ponto de partida no nó partida e a id i
    atual = partida
    prox = 0
    
    limite = 0                          # Ajuda a encontrar caminhos sem solução

    while prox != "finished":           # A formiga caminha pelo grafo, até achar um caminho válido
        prox = formiguinha.calcularota(formiguinha, matriz[atual], matrizFeromonio[atual]) #(instancia da formiga, ponto de partida, feromonio do ponto de partida)
        atual = prox
        if limite == 10:
            limite = random.randint(0, numeroNos - 1)   # Se a formiguinha se demorar demais num ponto de saída, ela vai tentar começar por outro
        else:
            limite += 1
    
    print(formiguinha.visitados)
    print(formiguinha.solucao)
    print(formiguinha.custo)
