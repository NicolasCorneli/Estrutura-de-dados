class Heap:
    def __init__(self):
        self.nos = 0
        self.heap = []

def insere_max_heap(arv,valor):
    if arv is None:
        arv = Heap()

    arv.heap.append(valor)
    arv.nos += 1
    f = arv.nos - 1
    
    #Heapify up
    while f > 0:
        p = (f-1) // 2
        if arv.heap[p] >= arv.heap[f]:
            break
        else:
            arv.heap[p], arv.heap[f] = arv.heap[f], arv.heap[p]
            f = p
    return arv

def insere_min_heap(arv2,valor):
    if arv2 is None:
        arv2 = Heap()

    arv2.heap.append(valor)
    arv2.nos += 1
    f = arv2.nos - 1

    #Heapify up
    while f > 0:
        p = (f-1) // 2
        if arv2.heap[p] <= arv2.heap[f]:
            break
        else:
            arv2.heap[p], arv2.heap[f] = arv2.heap[f], arv2.heap[p]
            f = p
    return arv2

# Função para remover o elemento máximo do Max Heap
def remove_max_heap(arv):
    if arv is None or arv.nos == 0:
        print("O heap está vazio")
        return None
    
    # Substitui a raiz pelo último elemento
    raiz = arv.heap[0]
    arv.heap[0] = arv.heap[-1]
    arv.heap.pop()
    arv.nos -= 1

    #Heapify down
    p = 0  # Índice do pai (raiz inicial)
    while True:
        f1 = 2 * p + 1  # Índice do filho da esquerda
        f2 = 2 * p + 2  # Índice do filho da direita
        maior = p

        # Verifica se o filho da esquerda é maior
        if f1 < arv.nos and arv.heap[f1] > arv.heap[maior]:
            maior = f1
        
        # Verifica se o filho da direita é maior
        if f2 < arv.nos and arv.heap[f2] > arv.heap[maior]:
            maior = f2
        
        # Se o pai é maior que ambos os filhos, a estrutura está correta
        if maior == p:
            break
        
        # Caso contrário, troca o pai com o maior dos filhos
        arv.heap[p], arv.heap[maior] = arv.heap[maior], arv.heap[p]
        p = maior  # Continua para o próximo nível
    
    return raiz

def remove_min_heap(arv2):
    if arv2 is None or arv2.nos == 0:
        print("O heap está vazio")
        return None
    
    # Substitui a raiz pelo último elemento
    raiz = arv2.heap[0]
    arv2.heap[0] = arv2.heap[-1]
    arv2.heap.pop()
    arv2.nos -= 1

    #Heapify down
    p = 0  # Índice do pai (raiz inicial)
    while True:
        f1 = 2 * p + 1  # Índice do filho da esquerda
        f2 = 2 * p + 2  # Índice do filho da direita
        menor = p

        # Verifica se o filho da esquerda é maior
        if f1 < arv2.nos and arv2.heap[f1] < arv2.heap[menor]:
            menor = f1
        
        # Verifica se o filho da direita é maior
        if f2 < arv2.nos and arv2.heap[f2] < arv2.heap[menor]:
            menor = f2
        
        # Se o pai é maior que ambos os filhos, a estrutura está correta
        if menor == p:
            break
        
        # Caso contrário, troca o pai com o maior dos filhos
        arv2.heap[p], arv2.heap[menor] = arv2.heap[menor], arv2.heap[p]
        p = menor  # Continua para o próximo nível
    
    return raiz

def busca_heap_max(arv,valor):
    if arv is None or arv.nos == 0:
        print("O heap está vazio")
        return

    if valor == arv.heap[0]:
        return valor
    elif valor > arv.heap[0]:
        print("Valor não existe no heap")
        return
    else:
        contador = 0
        while contador < arv.nos:
            no = arv.heap[contador+1]
            if no == valor:
                return valor
            elif valor <= arv.heap[(2 * contador + 1)] or valor <= arv.heap[(2 * contador + 2)]:
                contador += 1
            else:
                print("Valor não existe no heap")
                return

def busca_heap_min(arv2,valor2):
    if arv2 is None or arv2.nos == 0:
        print("O heap está vazio")
        return

    if valor2 == arv2.heap[0]:
        return valor
    elif valor2 < arv2.heap[0]:
        print("Valor não existe no heap")
        return
    else:
        contador = 0
        while contador < arv2.nos:
            no = arv2.heap[contador+1]
            if no == valor2:
                return valor2
            elif valor2 >= arv2.heap[(2 * contador + 1)] or valor2 >= arv2.heap[(2 * contador + 2)]:
                contador += 1
            else:
                print("Valor não existe no heap")
                return 
            
def mostra_max_heap(arv):
    if arv is None or arv.nos == 0:
        print("A árvore está vazia")
        return
    
    # Nível atual
    nivel_atual = 0
    # Número de nós no nível atual
    nos_nivel_atual = 1

    # Índice do próximo nó a ser impresso
    indice = 0

    while indice < arv.nos:
        # Imprimir todos os nós no nível atual
        for _ in range(nos_nivel_atual): #O uso de _ em um for loop no Python é uma convenção para indicar que a variável que itera não será usada dentro do loop.
            if indice < arv.nos:
                print(arv.heap[indice], end=" ")
                indice += 1
            else:
                break
        print()  # Nova linha após cada nível
        
        # Mudar para o próximo nível
        nivel_atual += 1
        nos_nivel_atual *= 2  # Cada nível tem o dobro de nós do que o anterior

def mostra_min_heap(arv2):
    if arv2 is None or arv2.nos == 0:
        print("A árvore está vazia")
        return
    
    # Nível atual
    nivel_atual = 0
    # Número de nós no nível atual
    nos_nivel_atual = 1
    # Índice do próximo nó a ser impresso
    indice = 0

    while indice < arv2.nos:
        # Imprimir todos os nós no nível atual
        for _ in range(nos_nivel_atual): #O uso de _ em um for loop no Python é uma convenção para indicar que a variável que itera não será usada dentro do loop.
            if indice < arv2.nos:
                print(arv2.heap[indice], end=" ")
                indice += 1
            else:
                break
        print()  # Nova linha após cada nível
        
        # Mudar para o próximo nível
        nivel_atual += 1
        nos_nivel_atual *= 2  # Cada nível tem o dobro de nós do que o anterior

arv = None
arv2 = None
#Max Heap
arv = insere_max_heap(arv,17)
arv = insere_max_heap(arv,36)
arv = insere_max_heap(arv,25)
arv = insere_max_heap(arv,7)
arv = insere_max_heap(arv,3)
arv = insere_max_heap(arv,100)
arv = insere_max_heap(arv,1)
arv = insere_max_heap(arv,2)
arv = insere_max_heap(arv,19)
remove_max_heap(arv)
#Min Heap
arv2 = insere_min_heap(arv2,17)
arv2 = insere_min_heap(arv2,36)
arv2 = insere_min_heap(arv2,25)
arv2 = insere_min_heap(arv2,7)
arv2 = insere_min_heap(arv2,3)
arv2 = insere_min_heap(arv2,100)
arv2 = insere_min_heap(arv2,1)
arv2 = insere_min_heap(arv2,2)
arv2 = insere_min_heap(arv2,19)
remove_min_heap(arv2)

mostra_max_heap(arv)
print()
mostra_min_heap(arv2)

print()
valor = busca_heap_max(arv,25)
print("Valor encontrado:",valor)

print()
valor2 = busca_heap_min(arv2,3)
print("Valor encontrado:",valor2)

