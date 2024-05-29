
import random
import numpy as np

numeroNos = 10          #Armazena o número de nós do grafo.
matrizIntensidades = []  #Basicamente, vai armazenar o valor de 𝑝𝑖,𝑗(𝑡) de cada caminho, em cada iteração

#ATENÇÃO!! MATRIZ DE FEROMONIO ---> Lembre que a matriz tem que ser simétrica, então tipo:
                                                    #matriz[x][y] = feromonio
                                                    #matriz[y][x] = feromonio tambem, pra ficar simetrico


def atualizaFeromonio(matrizFeromonio, feromDepositado, sigma):
    for i in range(numeroNos):
        for j in range(numeroNos):
            matrizFeromonio[i][j] = (((1 - sigma) * matrizFeromonio[i][j]) + (feromDepositado[i][j]))

def feromonioInicial(matrizFeromonio, intensidade, matrizCaminhos): # Insere o feromonio inicial em cada caminho
    for i in range(numeroNos):
        for j in range(numeroNos):
            if matrizCaminhos[i][j] != 0:
                matrizFeromonio[i][j] = intensidade

def feromonioXintensidade(alpha, beta, feromonio, distancia):
    if distancia == 0:
        return 0
    coiso = pow(feromonio, alpha) * pow((1/distancia), beta)
    if coiso == 0:
        return 0.00001  #Se o numero for tão pequeno, que o método da roleta causa divisão por 0...
    return coiso
    
def somaIntensidades(alpha, beta, linhaFeromonios, linhaDistancia):
    soma = 0
    listaIntensidades = []
    for i in range(numeroNos):
        listaIntensidades.append(feromonioXintensidade(alpha, beta, linhaFeromonios[i], linhaDistancia[i]))
    
    listaIntensidades.append(sum(listaIntensidades))
    
    return listaIntensidades
    

def evaporaFeromonio(linhaFeromonio, matrizfauxlinha):  #isso deve ser uma função no #escopo externo e não um metodo da classe formiga.
    print('ToDo')                                       #Func que vai evaporar o #feromonio da matriz

def addFeromonio(self, linhaFeromonio,matrizfauxlinha):   #Feromonio é soltado pela #formiga na linhaFeromonio
    print('ToDo')




#Classe formiga. Para cada nova formiga, será necessário instanciar uma nova classe
class Formiga:
    def __init__(self, partida, num):   #"Parâmetros privados"
        self.id = num               #Identificador da formiga. Usado apenas nos gráficos
        self.solucao =[]            #Vetor final que armazena o caminho andado pela formiga
        self.visitados=[]           #Vetor que armazena quais cidades ela já visitou. Pode ser essencial caso a gente for adicionar a busca por profundidade
        self.solucao.append(partida)
        self.custo = 0              #Custo da solução encontrada pela formiga

    @staticmethod
    def depositaFeromonio(self, feromoniosDepositados, Q):
        saida = self.solucao[0]
        chegada = self.solucao[1]
        rij = (Q / self.custo)
        prox = 2
        
        for i in range(numeroNos):
            saida = self.solucao[i]
            chegada = self.solucao[i + 1]
            feromoniosDepositados[saida][chegada] += rij
            feromoniosDepositados[chegada][saida] += rij

    @staticmethod
    def calcularota(self, linhaDistancia, linhaFeromonio, feromDepositado, linhaIntensidades):      # Atualmente, as rotas são calculadas por força bruta. É quase impossível achar uma rota válida para grafos grandes
        
        #[------------- Inicializamos vetores auxiliares
        possiveis = []          # Lista com caminhos possíveis
        probabilidades = []     # Probabilidade de cada caminho ser escolhido
        
        
        #[------------- Definimos os caminhos válidos
        for i in range(len(linhaDistancia)):    # Para cada elemento na linha
            if i not in self.visitados:         # Se ele nao tiver sido visitado
                if linhaDistancia[i] > 0:       # E for maior que 0 (visitável)
                    possiveis.append(i)         # Definimos ele como uma possibilidade de se visitar
        i = 0
        
        
        #[------------- Calculamos a probabilidade de escolher cada caminho
        for i in range(len(possiveis)):     # Para cada elemento na lista de nós possíveis, calculamos sua probabilidade de ser escolhido
            probabilidades.append(self.calculaprob(self, possiveis[i], 1, linhaDistancia, linhaFeromonio, linhaIntensidades))
            # acho que não é a melhor maneira de fazer isso, mas precisamos saber quais nós foram selecionados
            # e temos que saber associar a probabilidade a esse nó, essa foi a maneira que consegui pensar
        #print("----------Probabilidades eh ---------------")
        #print(probabilidades)

        #[------------- Agora escolhemos o próximo node:
        
        #[--------- Se tivermos caminhado por todo o grafo:
        if not bool(possiveis): # (no python, se uma lista está vazia ela é considerada false)
            #[--------- Caso a solução atual tenha nodes repetidos:
            if (len(self.solucao) != numeroNos + 1) or (self.solucao[0] != self.solucao[-1]):  
                #[----- Se não foram visitados todos os nós, ou se a origem for diferente do destino,
                self.solucao = [partida]    # Reseta a solução, volta a ponto de partida e tenta de novo
                self.visitados = []
                self.custo = 0
                return 0
            else:
                return "finished"   # Esse retorno indica que a solução encontrada pela formiguinha foi aceita
            
        #[--------- Não caminhamos por todo o grafo:
        else: 
            selecionado = random.choices(possiveis, weights=probabilidades, k=1)    # Escolhemos o próximo node, com base nos pesos dos feormonios
            novoNode = selecionado[0]       # Usamos uma variável auxiliar, para nao ter que acessar o vetor 4 vezes
            self.solucao.append(novoNode)       # Colocamos o node selecionado na lista solução e visitados
            self.visitados.append(novoNode)     # random.choices retorna uma lista de 1 posição, por isso o [0]
            self.custo += linhaDistancia[novoNode]  #acha na matriz de distância o indice do nó selecionado, e soma o custo
            return novoNode                 # Retorna o node escolhido

    @staticmethod
    def calculaprob(self, destino, b, linhaDistancia, linhaFeromonio, linhaIntensidade):
        probabilidade = 0
        probabilidade = linhaIntensidade[destino] / linhaIntensidade[-1]    # Já calculamos 𝑝𝑖,𝑗(𝑡) antes. Então só fazemos a roleta com ele
                                                                                # Σ 𝑝𝑖,𝑗(𝑡) está em linhaIntensidade[-1]
        #print("|||||||||| Aqui em calcprob ||||||||||")
        #print(linhaIntensidade[destino])
        #print(linhaIntensidade[-1])
        #print(probabilidade)
        return probabilidade


def inicializamatrizes(n, matriz):             
    #listaaux = [] # auxiliar para passar os valores para a matriz
    for i in range(n):  # for para inicializar matrizes
        estring = f.readline()  # readline retorna uma string
        lista = [int(ele) for ele in estring.split()]
        matriz.append(lista)  # joga lista para a matriz
        #listaaux.append(1)  # cria uma lista com n 0.1, n sendo o tamanho da linha da matriz
        #matrizFeromonio.append(listaaux)  # joga a lista criada para a matriz de feromonios
    return matriz



#int main() { 
#[------------- Vamos pegar os parâmetros do usuário:
op = input("Deseja usar parâmetros padrão? [1 - Sim] [~1 - Não]\nR: ") 

if op == 1:
    #[------ Primeiro, pegamos o endereço do arquivo com o grafo:
    f = open(input("Insira o endereço do arquivo com o grafo (ex: Grafos/Entrada 10.txt)\nR: "), "r") # f vai ser um ponteiro para o arquivo aberto (?)

    #[------ Agora, pedimos pro usuário definir o número de formigas
    nFormigas = input("Quantas formigas terão na colônia?\nR: ")
    
    #[------ Agora, pedimos pro usuário definir o número de formigas
    iteracoes = input("Qual vai ser o numero maximo de iteracoes?\nR: ")

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
    nFormigas = 2                       # Número de formigas
    randomFlag = False
    partida = 0                         # Ponto de partida
    alpha, beta, sigma, Tij, Q = 1, 1, 0.01, 0.1, 10    #Parâmetros
    convPrematura = 10                  # Num máximo de soluções repetidas
    iteracoes = 1


#[------------- Abrimos o arquivo, e obtemos o número de nós do grafo
numeroNos = f.readline()                # Vai armazenar a ordem da matriz / número de nós do grafo
numeroNos = int(numeroNos)
print("Temos ", numeroNos, " cidades")

#[------------- Inicializamos as matrizes
matrizZeros = [[0 for _ in range(numeroNos)] for _ in range(numeroNos)] # Matriz com vários 0's. Usada pra reiniciar matrizes
matriz = []                             # Armazena a tabela de caminhos do grafo
matrizFeromonio = matrizZeros           # Armazena os feromônios nos caminhos - Usada na decisão entre caminhos
feromDepositado = []                    # Armazena os feromônios soltos pelas formigas

#[------------- Lemos os conteúdos do arquivo, e colocamos na matriz matriz[][]
matriz = inicializamatrizes(numeroNos, matriz) #tamanho da matriz, matriz distancia

#[------------- Calculamos o feromônio inicial de cada caminho
intensidadeInicial = 100 / (numeroNos * numeroNos) # Dividimos 100 unidades de feromônios pela matriz de feromônio inicial
feromonioInicial(matrizFeromonio, intensidadeInicial, matriz)
feromDepositado = matrizZeros           # Inicializamos ela em 0


melhorSolucao = []
melhorDistancia = float('inf')

#[------------- Loop de execução do algoritmo:
for i in range(iteracoes):
    feromDepositado = matrizZeros
    
    matrizIntensidades = []  # Removemos os valores da lista de intensidades
    for j in range(numeroNos):  # E calculamos 𝑝𝑖,𝑗(𝑡) para cada caminho
        matrizIntensidades.append(somaIntensidades(alpha, beta, matrizFeromonio[j], matriz[j]))
    
    print(" ")
    print("[------ Iteração ", i, " ------]")
    print("Menor solucao da iteracao:")
    print(melhorSolucao)
    print("Distancia percorrida:")
    print(melhorDistancia)
    print(" ")
    print("-- Matriz Feromonios --")
    for linha in matrizFeromonio:
        print(linha)
    print("[------------------------------]")
    
    for j in range(nFormigas):
        #print("Foi 1")
        if randomFlag == True:              # Caso o usuário querer que o ponto de partida/chegada seja aleatório...
            partida = random.randint(0, numeroNos - 1)  # O teto faz parte do conjunto de saída

        formiguinha = Formiga(partida, i)   # Instanciamos uma formiga, com ponto de partida no nó partida e a id i
        atual = partida
        prox = 0

        limite = 0                          # Ajuda a encontrar caminhos sem solução

        #print("Foi 2")
        while prox != "finished":           # A formiga caminha pelo grafo, até achar um caminho válido
            #print("------------------------ Foi 3 ---------------------------")
            #for linha in matrizIntensidades:
            #    print(linha)
            prox = formiguinha.calcularota(formiguinha, matriz[atual], matrizFeromonio[atual], feromDepositado[atual], matrizIntensidades[atual]) #(instancia da formiga, ponto de partida, feromonio do ponto de partida)
            atual = prox
            #print("Limite: ", limite)
            if limite == 80:
                #print("Foi 4")
                limite = 0
                partida = random.randint(0, numeroNos - 1)   # Se a formiguinha se demorar demais num ponto de saída, ela vai tentar começar por outro
            else:
                #print("Foi 5 -------------- Já escolhemos o caminho:")
                #print(formiguinha.solucao)
                limite += 1
            
        #[----- Formiguinha completou sua viagem
        print(formiguinha.visitados)
        print(formiguinha.solucao)
        print(formiguinha.custo)
        #[----- Hora de depositar os feromônios da furmiga na matriz feromDepositado[][]
        formiguinha.depositaFeromonio(formiguinha, feromDepositado, Q)
        
        if formiguinha.custo < melhorDistancia:
            melhorDistancia = formiguinha.custo
            melhorSolucao = formiguinha.solucao
    
    print("--------Vamos ver os feromonios depositados------------------")
    for linha in feromDepositado:
        print(linha)
    
    #[----- Todas as furmigas caminharam pelo grafo e depositaram seus feromônios em feromDepositado!
    atualizaFeromonio(matrizFeromonio, feromDepositado, sigma)
    
    
print("[------ Soluções: ------]")
print(melhorSolucao)
print(melhorDistancia)

#return 0
#}