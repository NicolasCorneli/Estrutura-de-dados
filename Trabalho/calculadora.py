class Pilha:
    def __init__(self, max):
        self.max = max
        self.n = 0  # Número de elementos na pilha
        self.vet = []  # Vetor // Topo da pilha --> p.vet[p.n - 1]


def cria_pilha_operandos(max):
    pilha_operandos = Pilha(max)
    return pilha_operandos


def cria_pilha_operadores(max):
    pilha_operadores = Pilha(max)
    return pilha_operadores


def pilha_vazia_operandos(pilha_operandos):
    return pilha_operandos.n == 0


def pilha_vazia_operadores(pilha_operadores):
    return pilha_operadores.n == 0

def push_pilha_operandos(pilha_operandos, v):
    # Insere na pilha dos operandos
    pilha_operandos.vet.insert(pilha_operandos.n, v)
    pilha_operandos.n = pilha_operandos.n + 1


def push_pilha_operadores(pilha_operadores, v):
    # Insere na pilha dos operadores
    pilha_operadores.vet.insert(pilha_operadores.n, v)
    pilha_operadores.n = pilha_operadores.n + 1


def pop_pilha_operandos(pilha_operandos):
    # Tira da pilha dos operandos
    if pilha_vazia_operandos(pilha_operandos):
        print("Pilha dos operandos está vazia")
        return False
    elemento_retirado_operandos = pilha_operandos.vet.pop()
    pilha_operandos.n = pilha_operandos.n - 1
    return elemento_retirado_operandos


def pop_pilha_operadores(pilha_operadores):
    # Tira da pilha dos operadores
    if pilha_vazia_operadores(pilha_operadores):
        print("Pilha dos operadores está vazia")
        return False
    elemento_retirado_operadores = pilha_operadores.vet.pop()
    pilha_operadores.n = pilha_operadores.n - 1
    return elemento_retirado_operadores

pilha_operadores = cria_pilha_operadores(50)
pilha_operandos = cria_pilha_operandos(50)


def calculadora(pilha_operandos, pilha_operadores):
    operador = pop_pilha_operadores(pilha_operadores)
    if operador is False:
        exit() # Operador não disponível, expressão inválida

    operando2 = pop_pilha_operandos(pilha_operandos)
    operando1 = pop_pilha_operandos(pilha_operandos)

    if not pilha_vazia_operadores(pilha_operadores) and pilha_operadores.vet[-1] == "-":
        operando1 = pilha_operadores.vet[-1] + operando1
        pop_pilha_operadores(pilha_operadores)

        if operando1 is False or operando2 is False:
            print("Expressão inválida - operandos insuficientes")
            exit()
        if operador == "+":
            resultado = float(operando1) + float(operando2)
        elif operador == "-":
            resultado = float(operando1) - float(operando2)
        elif operador == "*":
            resultado = float(operando1) * float(operando2)
        elif operador == "/":
            if float(operando2) == 0:
                print("Divisão Por Zero -- Expressão Inválida")
                exit()
            resultado = float(operando1) / float(operando2)
        elif operador == "**":
            resultado = float(operando1) ** float(operando2)
        if not pilha_vazia_operandos(pilha_operandos) and resultado > 0:
            push_pilha_operadores(pilha_operadores, "+")
        elif not pilha_vazia_operandos(pilha_operandos) and resultado < 0:
            push_pilha_operadores(pilha_operadores, "-")
    else:
        if operando1 is False or operando2 is False:
            print("Expressão inválida - operandos insuficientes")
            exit()
        if operador == "+":
            resultado = float(operando1) + float(operando2)
        elif operador == "-":
            resultado = float(operando1) - float(operando2)
        elif operador == "*":
            resultado = float(operando1) * float(operando2)
        elif operador == "/":
            if float(operando2) == 0:
                print("Divisão Por Zero -- Expressão Inválida")
                exit()
            resultado = float(operando1) / float(operando2)
        elif operador == "**":
            resultado = float(operando1) ** float(operando2)
    push_pilha_operandos(pilha_operandos, resultado)


def insere_lista(expressao):
    expressao_lista = []
    i = 0
    while i < len(expressao):
        if expressao[i].isdigit():
            if i + 1 < len(expressao) and expressao[i + 1].isdigit():
                junta_numero = expressao[i]
                while i + 1 < len(expressao) and expressao[i + 1].isdigit():
                    junta_numero = junta_numero + expressao[i + 1]
                    i += 1  # Avança mais um índice para pular para o próximo dígito
                expressao_lista.append(junta_numero)
            else:
                expressao_lista.append(expressao[i])
                
        elif expressao[i] == "*" and expressao[i + 1] == "*":
            junta_operador = expressao[i] + expressao[i + 1]
            expressao_lista.append(junta_operador)
            i += 1  # Pula o outro sinal de vezes, sem causar problemas ao código.
        elif expressao[i] == "+" or expressao[i] == "-" or expressao[i] == "*" or expressao[i] == "/" or expressao[i] == "(" or expressao[i] == ")":
            expressao_lista.append(expressao[i])

        i += 1  # Avança para o próximo caractere na expressão
    return expressao_lista

expressao = input("")
expressao_lista = insere_lista(expressao)

def valida_parenteses(expressao_lista):
    if "(" in expressao_lista and ")" not in expressao_lista:
        return False
    elif ")" in expressao_lista and "(" not in expressao_lista:
        return False
    else:
        return True


resultado_parenteses = valida_parenteses(expressao_lista)

if resultado_parenteses == False:
    print("Expressão Inválida")
    exit()

def insere_pilha(expressao_lista):
    for x in range(len(expressao_lista)):
        if expressao_lista[x].isdigit():
            # Acrescenta número na pilha dos operandos
            push_pilha_operandos(pilha_operandos, expressao_lista[x])
        else:
            if expressao_lista[x] == "(":
                push_pilha_operadores(pilha_operadores, expressao_lista[x])
            else:
                while not pilha_vazia_operadores(pilha_operadores) and (
                        (expressao_lista[x] == "+" or expressao_lista[x] == "-" or expressao_lista[x] == "*" or
                         expressao_lista[x] == "/") and (pilha_operadores.vet[-1] == "**")):
                    calculadora(pilha_operandos, pilha_operadores)

                while not pilha_vazia_operadores(pilha_operadores) and (
                        (expressao_lista[x] == "+" or expressao_lista[x] == "-") and (
                        pilha_operadores.vet[-1] == "*" or pilha_operadores.vet[-1] == "/")):
                    calculadora(pilha_operandos, pilha_operadores)
                
                while not pilha_vazia_operadores(pilha_operadores) and (
                    (expressao_lista[x] == "*" or expressao_lista[x] == "/") and (pilha_operadores.vet[-1] == "*" or pilha_operadores.vet[-1] == "/")):
                    calculadora(pilha_operandos,pilha_operadores)

                if expressao_lista[x] == ")":
                    while pilha_operadores.vet[-1] != "(":
                        calculadora(pilha_operandos, pilha_operadores)
                    pop_pilha_operadores(pilha_operadores)
                else:
                    # Acrescenta operador na pilha dos operadores
                    push_pilha_operadores(pilha_operadores, expressao_lista[x])

    while not pilha_vazia_operadores(pilha_operadores):
        calculadora(pilha_operandos, pilha_operadores)

    # Retorna o resultado final do cálculo
    return pilha_operandos.vet[-1]
