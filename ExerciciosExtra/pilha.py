class Pilha:
    def __init__(self,max):
        self.max = max
        self.n = 0
        self.vet = []

def cria_pilha(max):
    p = Pilha(max)
    return p

def pilha_vazia(p):
    return p.n == 0

def pilha_cheia(p):
    return p.max == p.n
    

def pilha_push(p,v):
    if pilha_cheia(p):
        print("Pilha cheia")
        return False
    palavra = []
    p.vet.insert(p.n,v)
    palavra.append(v)
    print("Valores acrescentados a pilha:",v)
    p.n = p.n + 1
    return palavra

def pilha_pop(p):
    if pilha_vazia(p):
        print("Pilha vazia")
        return False
    valor_retirado = p.vet.pop()
    p.n = p.n - 1
    palavra2 = []
    palavra2.append(valor_retirado)
    print("Valores retirados da pilha:", valor_retirado)
    return valor_retirado,palavra2

def esvazia(p):
    while not pilha_vazia(p):
        pilha_pop(p)

def palindromo(palavra,palavra2):
    if palavra == palavra2:
        print("Essa palavra é um Palíndromo")
        return True
    else:
        print("Essa palavra não é um Palíndromo")
        return False
    

def questao3(p):
    if not pilha_vazia(p):
        return p.n, p.vet[-1]
    else:
        print("Pilha Vazia, não há objetos para retornar")

p = cria_pilha(5)
pilha_cheia(p)
pilha_vazia(p)


#Questão 1 está na função pilha_push(p)

#2.a)
#pilha_push(p,4)
#pilha_push(p,3)
#valor_retirado = pilha_pop(p)
#pilha_push(p,8)
#valor_retirado = pilha_pop(p)

#2.b)I.
#pilha_push(p,3)
#valor_retirado = pilha_pop(p)
#valor_retirado = pilha_pop(p)
#pilha_push(p,4)

#2.b)II.
#pilha_push(p,1)
#valor_retirado = pilha_pop(p)
#pilha_push(p,2)
#pilha_push(p,3)
#pilha_push(p,4)
#pilha_push(p,5)
#pilha_push(p,6)
#pilha_push(p,7)
#pilha_push(p,8)

#3.
#pilha_push(p,1)
#pilha_push(p,2)
#pilha_push(p,4)
#numero_de_objetos,objeto_topo = questao3(p)
#print("Número de objetos na pilha:",numero_de_objetos)
#print("Objeto no topo da pilha:",objeto_topo)

#4.
#esvazia(p)

#5.
#palavra = pilha_push(p,"a")
#palavra = pilha_push(p,"r")
#palavra = pilha_push(p,"a")
#palavra = pilha_push(p,"r")
#palavra = pilha_push(p,"a")
#valor_retirado, palavra2 = pilha_pop(p)
#valor_retirado, palavra2 = pilha_pop(p)
#valor_retirado, palavra2 = pilha_pop(p)
#valor_retirado, palavra2 = pilha_pop(p)
#valor_retirado, palavra2 = pilha_pop(p)
#valor = palindromo(palavra,palavra2)
#print(valor)


class Pilha:
    def __init__(self,max):
        self.max = max
        self.n = 0
        self.vet = []

def cria_pilha1(max):
    pilha1 = Pilha(max)
    return pilha1

def cria_pilha2(max):
    pilha2 = Pilha(max)
    return pilha2

def pilha1_vazia(pilha1):
    return pilha1.n == 0

def pilha2_vazia(pilha2):
    return pilha2.n == 0

def push_pilha1(pilha1,v):
    pilha1.vet.insert(pilha1.n,v)
    pilha1.n = pilha1.n + 1

def push_pilha2(pilha2,v):
    pilha2.vet.insert(pilha2.n,v)
    pilha2.n = pilha2.n + 1

def pop_pilha1(pilha1):
    if pilha1_vazia(pilha1):
        print("Pilha 1 Vazia")
        return False
    valor_retirado_p1 = pilha1.vet.pop()
    pilha1.n = pilha1.n - 1
    return valor_retirado_p1

def pop_pilha2(pilha2):
    if pilha2_vazia(pilha2):
        print("Pilha 2 Vazia")
        return False
    valor_retirado_p2 = pilha2.vet.pop()
    pilha2.n = pilha2.n - 1
    return valor_retirado_p2

def concatena(pilha1,pilha2):
    lista_valores = []
    while not pilha2_vazia(pilha2):
        valor = pop_pilha2(pilha2)
        lista_valores.append(valor)
    lista_valores = lista_valores[::-1]
    for x in lista_valores:
        push_pilha1(pilha1,x)
    

pilha1 = cria_pilha1(10)
pilha2 = cria_pilha2(10)

push_pilha1(pilha1,1)
push_pilha1(pilha1,2)
push_pilha1(pilha1,3)
push_pilha2(pilha2,4)
push_pilha2(pilha2,5)
push_pilha2(pilha2,6)

concatena(pilha1,pilha2)

if not pilha2_vazia(pilha2):
    print(pilha2.vet[-1])

if not pilha1_vazia(pilha1):
    print(pilha1.vet[-1])
    print(pilha1.vet[-2])
    print(pilha1.vet[-3])
    print(pilha1.vet[-4])
    print(pilha1.vet[-5])
    print(pilha1.vet[-6])

