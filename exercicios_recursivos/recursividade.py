#1. Implemente uma função recursiva produto(n) que calcula o produto dos n
#primeiros números inteiros positivos.
#def produto(n):

def produto(n):
    if n <= 1:
        return 1
    else:
        return n * produto(n - 1)
    
print(produto(5))

#2. Faça uma função recursiva que imprima na tela os valores que estão
#dentro de um intervalo informado pelo usuário.
#def imprimir(min, max):

def imprimir(min,max):
    valor = min + 1
    if (valor + 1) == max:
        return valor
    print(valor)
    return (imprimir(valor,max))
    
print(imprimir(5,10))

#3. Implemente uma função recursiva que, dados dois números inteiros x e n,
#calcula o valor de x elevado na n.
#def potencia(x, n):

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x,n - 1)
    
print(potencia(5,2))

#4.Faça uma função recursiva que calcule e escreva o valor de S:
#def s(n, d):

def s(n,d):
    if d == 1:
        return 1
    else:
        return (n / d) + s(n-2,d-1)

print(s(99,50))

#5. Considere um sistema numérico que não tenha a operação de adição
#implementada e que você disponha somente dos operadores (funções)
#sucessor e predecessor. Então, pede-se para escrever uma função recursiva
#que calcule a soma de dois números x e y através desses dois operadores:
#sucessor e predecessor.
#def calcula_soma(x, y):

def calcula_soma(x,y):
    if y == 0:
        return x
    else:
        return calcula_soma(x+1,y-1)

print(calcula_soma(5,3))


#6. Faça um programa que implemente a busca binária de um valor v em um
#vetor ordenado vet de tamanho 10. A função deve retornar a posição onde o
#elemento se encontra. Caso não exista, retornar falso.
#def busca_binaria(vet, v, inf, sup):


def busca_binaria(vet, v, inf, sup):
    while inf <= sup:
        meio = (inf+sup) // 2
        if vet[meio] == v:
            return meio
        elif vet[meio] < v:
            inf = meio + 1
        else:
            sup = meio - 1
    return False

vetor = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
valor = 7
resultado = busca_binaria(vetor, valor, 0, len(vetor))
print(resultado)

#7. Um problema típico em ciência da computação consiste em converter um
#número da sua forma decimal para a forma binária. Por exemplo, o número
#12 tem a sua representação binária igual a 1100. A forma mais simples de
#fazer isso é dividir o número sucessivamente por 2, onde o resto da i-ésima
#divisão vai ser o dígito i do número binário (da direita para a esquerda). Por
#exemplo:
#● 12 / 2 = 6, resto 0 (1o dígito da direita para esquerda);
#● 6 / 2 = 3, resto 0 (2o dígito da direita para esquerda);
#● 3 / 2 = 1 resto 1 (3o dígito da direita para esquerda);
#● 1 / 2 = 0 resto 1 (4o dígito da direita para esquerda).
#Resultado: 12 = 1100
#Escreva uma função recursiva que dado um número decimal x imprima a sua
#representação binária corretamente.
#def binario(x):

def binario(x):
    if x == 0:
        return "0"
    else:
        resto = x % 2
        return binario(x // 2) + str(resto)
    
print(binario(12))
