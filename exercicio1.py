class Lista:
    def __init__(self,info=None):
        self.info = info
        self.prox = None
        
def lista_cria():
    return None

def lista_insere(lst,valor):
    novo_numero = Lista(valor)
    novo_numero.prox = lst
    return novo_numero

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

#def lista_vazia(lst):
    #if lst:
        #return True

def lista_busca(lst,valor):
    atual = lst
    while atual is not None:
        if valor == atual.info:
            print("Achei:",atual.info)
            break
        else:
            print("Não achei")
        atual = atual.prox

def lista_retira(lst,valor):
    atual = lst
    if atual is not None and valor == atual.info:
        lst = atual.prox
        
    while atual is not None:
        if atual.prox is not None and valor == atual.prox.info:
            atual.prox = atual.prox.prox
            break
        atual = atual.prox
    return lst

lst = lista_cria()

lst = lista_insere(lst,50)
lst = lista_insere(lst,60)
lst = lista_insere(lst,70)
lst = lista_insere(lst,80)
lst = lista_retira(lst,50)
lista_imprime(lst)
#lista_vazia(lst)
lista_busca(lst,80)
