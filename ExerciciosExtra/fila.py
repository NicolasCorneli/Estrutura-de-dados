#1
class Fila:
    def __init__(self,max):
        self.max = max
        self.ini = 0
        self.n = 0
        self.vet = []

def cria_fila(max):
    f = Fila(max)
    return f

def fila_vazia(f):
    return f.n == 0

def fila_cheia(f):
    return f.n == f.max

def insere_fila(f,v):
    if fila_cheia(f):
        print("Fila cheia")
        return False
    fim = (f.ini + f.n) % f.max
    f.vet.insert(fim,v)
    f.n = f.n + 1

def retira_fila(f):
    if fila_vazia(f):
        print("Fila vazia")
        return False
    valor_retirado = f.vet.pop(f.ini)
    f.n = f.n - 1
    return valor_retirado

f = cria_fila(5)

insere_fila(f,1)
insere_fila(f,2)
insere_fila(f,3)
insere_fila(f,4)
insere_fila(f,5)
retira_fila(f)
print(f.vet[f.ini])


#2

class Fila:
    def __init__(self,max):
        self.max = max
        self.ini = 0
        self.n = 0
        self.vet = []

def cria_fila1(max):
    f1 = Fila(max)
    return f1


def cria_fila2(max):
    f2 = Fila(max)
    return f2

def cria_fila3(max):
    f_res = Fila(max)
    return f_res

def fila_vazia1(f1):
    return f1.n == 0

def fila_vazia2(f2):
    return f2.n == 0

def insere_fila_f1(f1,v):
    fim = (f1.ini + f1.n) % f1.max
    f1.vet.insert(fim,v)
    f1.n = f1.n + 1

def retira_fila_f1(f1):
    valor_f1 = f1.vet.pop(f1.ini)
    f1.n = f1.n - 1
    return valor_f1

def insere_fila_f2(f2,v):
    fim = (f2.ini + f2.n) % f2.max
    f2.vet.insert(fim,v)
    f2.n = f2.n + 1

def retira_fila_f2(f2):
    valor_f2 = f2.vet.pop(f2.ini)
    f2.n = f2.n - 1
    return valor_f2

def insere_fila_f_res(f_res,v):
    fim = (f_res.ini + f_res.n) % f_res.max
    f_res.vet.insert(fim,v)
    f_res.n = f_res.n + 1

def retira_fila_f_res(f_res):
    valor_retirado_f_res = f_res.vet.pop(f_res.ini)
    f_res.n = f_res.n - 1
    return valor_retirado_f_res



def combina_filas(f1,f2,f_res):
    while not (fila_vazia1(f1) or fila_vazia2(f2)):
        valor_f1 = retira_fila_f1(f1)
        insere_fila_f_res(f_res,valor_f1)
        valor_f2 = retira_fila_f2(f2)
        insere_fila_f_res(f_res,valor_f2)
    if fila_vazia1(f1):
        while not fila_vazia2(f2):
            valor_f2 = retira_fila_f2(f2)
            insere_fila_f_res(f_res,valor_f2)
    elif fila_vazia2(f2):
        while not fila_vazia1(f1):
            valor_f1 = retira_fila_f1(f1)
            insere_fila_f_res(f_res,valor_f1)

f1 = cria_fila1(3)
f2 = cria_fila2(5)
f_res = cria_fila3(10)

insere_fila_f1(f1,1)
insere_fila_f1(f1,2)
insere_fila_f1(f1,3)
insere_fila_f2(f2,4)
insere_fila_f2(f2,5)
insere_fila_f2(f2,6)
insere_fila_f2(f2,7)
insere_fila_f2(f2,8)
combina_filas(f1,f2,f_res)
print(f_res.vet[f_res.ini])
print(f_res.vet[f_res.ini + 1])
print(f_res.vet[f_res.ini + 2])
print(f_res.vet[f_res.ini + 3])
print(f_res.vet[f_res.ini + 4])
print(f_res.vet[f_res.ini + 5])
print(f_res.vet[f_res.ini + 6])
print(f_res.vet[f_res.ini + 7])


#3

class Fila:
    def __init__(self,max):
        self.max = max
        self.ini = 0
        self.n = 0
        self.vet = []

def cria_fila1(max):
    f1 = Fila(max)
    return f1

def cria_fila2(max):
    f2 = Fila(max)
    return f2

def cria_fila3(max):
    f3 = Fila(max)
    return f3

def fila_vazia1(f1):
    return f1.n == 0

def fila_vazia2(f2):
    return f2.n == 0

def insere_fila_f1(f1,v):
    fim = (f1.ini + f1.n) % f1.max
    f1.vet.insert(fim,v)
    f1.n = f1.n + 1


def retira_fila_f1(f1):
    valor_f1 = f1.vet.pop(f1.ini)
    f1.n = f1.n - 1
    return valor_f1

def insere_fila_f2(f2,v):
    fim = (f2.ini + f2.n) % f2.max
    f2.vet.insert(fim,v)
    f2.n = f2.n + 1

def retira_fila_f2(f2):
    valor_f2 = f2.vet.pop(f2.ini)
    f2.n = f2.n - 1
    return valor_f2

def insere_fila_f3(f3,v):
    fim = (f3.ini + f3.n) % f3.max
    f3.vet.insert(fim,v)
    f3.n = f3.n + 1

def fila_frente_f1(f1):
    return f1.vet[f1.ini]

def fila_frente_f2(f2):
    return f2.vet[f2.ini]


def ordena_filas(f1,f2):
    f3 = cria_fila3(20)
    while not (fila_vazia1(f1) or fila_vazia2(f2)):
        if fila_frente_f1(f1) > fila_frente_f2(f2):
            insere_fila_f3(f3,retira_fila_f2(f2))
            insere_fila_f3(f3,retira_fila_f1(f1))
        else:
            insere_fila_f3(f3,retira_fila_f1(f1))
            insere_fila_f3(f3,retira_fila_f2(f2))
    
    if not fila_vazia2(f2):
        while not fila_vazia2(f2):
            insere_fila_f3(f3,retira_fila_f2(f2))
    elif not fila_vazia1(f1):
        while not fila_vazia1(f1):
            insere_fila_f3(f3,retira_fila_f1(f1))
    return f3

f1 = cria_fila1(20)
f2 = cria_fila2(20)

insere_fila_f1(f1,2)
insere_fila_f1(f1,4)
insere_fila_f1(f1,6)
insere_fila_f2(f2,1)
insere_fila_f2(f2,3)
insere_fila_f2(f2,5)
insere_fila_f2(f2,7)
insere_fila_f2(f2,9)

f3 = ordena_filas(f1,f2)

print(f3.vet[f3.ini])
print(f3.vet[f3.ini+1])
print(f3.vet[f3.ini+2])
print(f3.vet[f3.ini+3])
print(f3.vet[f3.ini+4])
print(f3.vet[f3.ini+5])
print(f3.vet[f3.ini+6])
print(f3.vet[f3.ini+7])








