#1. Considere listas de valores inteiros e implemente uma função que receba
#como parâmetros uma lista encadeada e um valor inteiro n, retire da lista
#todas as ocorrências de n e retorne a lista resultante. Esta função deve
#obedecer ao protótipo:

#def retira_n(lst, n):

class Lista:
    def __init__(self,valor=None):
        self.valor = valor
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst,valor):
    novo_no = Lista(valor)
    novo_no.prox = lst
    return novo_no

def imprime_lista(lst):
    atual = lst
    while atual:
        print(atual.valor)
        atual = atual.prox

def retira_n(lst,n):
    ant = None
    atual = lst
    while atual is not None:
        if atual.valor == n:
            if ant is not None:
                ant.prox = atual.prox
            else:
                lst = atual.prox
        else:
            ant = atual
        atual = atual.prox

    return lst

lst = cria_lista()
lst = insere_lista(lst,5)
lst = insere_lista(lst,10)
lst = insere_lista(lst,15)
lst = insere_lista(lst,20)
lst = insere_lista(lst,10)
lst = insere_lista(lst,25)
lst = insere_lista(lst,30)
lst = insere_lista(lst,10)
imprime_lista(lst)
lst = retira_n(lst,10)
print("---Nova lista---")
imprime_lista(lst)

#2. Considere listas de valores inteiros e implemente uma função que receba
#como parâmetro uma lista encadeada e um valor inteiro n e divida a lista em
#duas, de forma a segunda lista começar no primeiro nó logo após a
#ocorrência de n na lista original. A figura a seguir ilustra esta separação:

#A função deve retornar a referência para a segunda subdivisão da lista
#original, enquanto lst deve continuar apontando para o primeiro elemento da
#primeira subdivisão da lista. Essa função deve obedecer ao protótipo:

#def separa(lst, n):

class Lista:
    def __init__(self,valor=None):
        self.valor = valor
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst,valor):
    novo_no = Lista(valor)
    novo_no.prox = lst
    return novo_no

def imprime_lista(lst):
    atual = lst
    while atual:
        print(atual.valor)
        atual = atual.prox

def separa(lst,n):
    atual = lst
    while atual is not None and atual.valor != n:
        atual = atual.prox

    if atual.valor == n:
        lst2 = atual.prox
        atual.prox = None
    return lst2


lst = cria_lista()
lst = insere_lista(lst,5)
lst = insere_lista(lst,10)
lst = insere_lista(lst,15)
lst = insere_lista(lst,20)
lst = insere_lista(lst,25)
lst = insere_lista(lst,30)
lst2 = separa(lst,15)
imprime_lista(lst)
imprime_lista(lst2)

#3. Considere listas que armazenam cadeias de caracteres e implemente uma
#função para testar se duas listas passadas como parâmetros são iguais. Essa
#função deve obedecer ao protótipo:

#def igual(l1, l2):

class Lista:
    def __init__(self,valor=None):
        self.valor = valor
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst,valor):
    novo_no = Lista(valor)
    novo_no.prox = lst
    return novo_no

def insere_lista2(lst2,valor):
    novo_no2 = Lista(valor)
    novo_no2.prox = lst2
    return novo_no2

def imprime_lista(lst):
    atual = lst
    while atual:
        print(atual.valor)
        atual = atual.prox

def igual(lst,lst2):
    atual = lst
    atual2 = lst2
    while atual is not None and atual2 is not None:
        if atual.valor == atual2.valor:
            atual = atual.prox
            atual2 = atual2.prox
        else:
            print("As listas são diferentes")
            break
    if atual is None and atual2 is None:
        print("As listas são iguais")
    if atual is None and atual2 is not None:
        print("As listas são diferentes, a segunda lista é maior")
    if atual is not None and atual2 is None:
        print("As listas são diferentes, a primeira lista é maior")


lst = cria_lista()
lst2 = cria_lista()
lst = insere_lista(lst,"aaaa")
lst = insere_lista(lst,"aaaa")
lst = insere_lista(lst,"aaaa")
lst2 = insere_lista2(lst2,"aaaa")
lst2 = insere_lista(lst2,"aaaa")
lst2 = insere_lista(lst2,"aaaa")
print("---Lista 1---")
imprime_lista(lst)
print("---Lista 2---")
imprime_lista(lst2)
igual(lst,lst2)

#4. Implemente funções para inserir e retirar um elemento de uma lista circular
#simplesmente encadeada (obtenha informações adicionais sobre listas
#circulares na bibliografia básica da disciplina).

class Lista:
    def __init__(self,valor=None):
        self.valor = valor
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst,valor):
    novo_no = Lista(valor)
    novo_no.prox = lst
    return novo_no

def imprime_lista(lst,ultimo_no):
    atual = lst
    while atual:
        print(atual.valor)
        atual = atual.prox
        if atual == ultimo_no:
            print(atual.valor)
            break

def circula_lista(lst):
    atual = lst
    while atual is not None:
        ultimo_no = atual
        atual = atual.prox
    ultimo_no.prox = lst
    return lst,ultimo_no

def remove_number(lst,ultimo_no,valor):
    ant = None
    atual = lst
    while atual.valor != valor:
        ant = atual
        atual = atual.prox
        if atual.valor == ultimo_no and ultimo_no != valor:
            break
    
    if ant is None:
        lst = atual.prox

    else:
        ant.prox = atual.prox
        if valor == ultimo_no.valor:
            ultimo_no = ant
    
    return lst,ultimo_no

    
lst = cria_lista()
lst = insere_lista(lst,5)
lst = insere_lista(lst,10)
lst = insere_lista(lst,15)
lst = insere_lista(lst,20)
lst,ultimo_no = circula_lista(lst)
lst,ultimo_no = remove_number(lst,ultimo_no,5)
imprime_lista(lst,ultimo_no)
