from nodestate_essentials_lib import *
import copy



class nodeState:
    def __init__(self, matriz, pai = None, movimento = None, nivel = 0):
        self.matriz = matriz
        self.filhos = []
        self.pai = pai
        self.movimento = movimento
        self.nivel = nivel
        self.errados = 0
        # ...
        
        

def atualizaErrados(node: nodeState, matrizobj):
    node.errados = 0

    for i in range(9):
        if node.matriz[i] != matrizobj[i]:
            node.errados += 1

    return node.errados   






def escolheMelhor(lista):
    if lista == []:
        exit(f'bro pq q a lista ta empty')

    node_escolhido = None
    menorvalor = 999

    #acha o nó da lista com menor .errados
    for node in lista:
        if node.errados < menorvalor:
            menorvalor = node.errados
            node_escolhido = node

    lista.remove(node_escolhido)
    return node_escolhido #envia o nó da lista com errados menor pro return
    








def heuristicabasica(raiz: nodeState, obj):
    atualizaErrados(raiz, obj)

    ABERTOS = [raiz]
    FECHADOS = []

    while ABERTOS != []:
        #pega o nó dos abertos (ou seja, sem filhos) com menor quant de errados
        X = escolheMelhor(ABERTOS) #escolheMelhor dá pop() em ABERTOS
        FECHADOS.append(X)

        atualizaErrados(X, obj)
        
        #se errados == 0, entao é o objetivo!
        if X.errados == 0: 
            return 'SUCESSO', X
        
        listanova = gerar_filhos(X)
        for node in listanova:
            [fazer: nao botar no igual no abertos]
            ABERTOS.append(node)
        
        printanode(X)







def heuristica_naobasica(raiz: nodeState, obj):
    return













    

if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([4, 3, 5,
                      1, 2, 6,
                      7, 0, 8])
    matrizObjetivo = [1, 2, 3,
                      4, 5, 6,
                      7, 8, 0]
    
    nivelMax = -1
    escolha = -1
    



    print(f'Quantidade máxima de níveis: ', end='')
    nivelMax = int(input())

    if nivelMax < 1:
        exit("maior q zero pls!")
    



    print(f'1-heuristica basica, 2-heuristica nao basica?: ', end='')
    escolha = int(input())
    
    match escolha:
        case 1:
            resultado, filhoFinal = heuristicabasica(raiz, matrizObjetivo)
        case 2:
            resultado, filhoFinal = heuristica_naobasica(raiz, matrizObjetivo)
        case _:
            exit("1 ou 2 pls!")
            




    print(f'\n\n\n{resultado}!')
    if resultado == 'SUCESSO':
        print(f'\n\tNível achado: {filhoFinal.nivel}, nó final:')
        printanode(filhoFinal)
        print(f'\tPrintando caminho:\n ', end='')
    
    movimentos = []
    while filhoFinal.pai != None:
        movimentos.append(filhoFinal.movimento)
        filhoFinal = filhoFinal.pai
    
    for i in reversed(range(len(movimentos))):
        print(f'{movimentos[i]}, ', end='')
    print(f'\n')
