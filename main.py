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
        
        



        













    

if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([1, 2, 3, 4, 5, 6, 7, 0, 8])
    matrizObjetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    nivelMax = -1
    escolha = -1
    



    print(f'Quantidade máxima de níveis: ', end='')
    nivelMax = int(input())

    if nivelMax < 1:
        exit("maior q zero pls!")
    



    print(f'1-DFS, 2-BFS?: ', end='')
    escolha = int(input())
    
    match escolha:
        case 2:
            resultado, filhoFinal = BFS(raiz, matrizObjetivo, nivelMax)
        case 1:
            resultado, filhoFinal = DFS(raiz, matrizObjetivo, nivelMax)
        case _:
            exit("1 ou 2 pls!")
            



            
    print(f'{resultado}!')
    if resultado == 'SUCESSO':
        print(f' nível achado: {filhoFinal.nivel}, printando caminho:\n ')
    
    movimentos = []
    while filhoFinal.pai != None:
        movimentos.append(filhoFinal.movimento)
        filhoFinal = filhoFinal.pai
    
    for i in reversed(range(len(movimentos))):
        print(f'{movimentos[i]} ')
    
