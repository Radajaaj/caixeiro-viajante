f = open("Entrada 10.txt","r")
n = f.readline() #tamanho da matriz
n=int(n)
matriz = [] 
lista = [] #auxiliar para passar os valores para a matriz
for i in range (n):
    estring = f.readline() #readline retorna uma string
    lista = [int(ele) for ele in estring.split()]
    matriz.append(lista) #joga lista para a matriz
print(matriz)
print(matriz[9][7])