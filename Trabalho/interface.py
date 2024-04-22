from tkinter import *
from calculadora import insere_pilha, insere_lista

# Estrutura da janela
x = Tk()
x.title('Calculadora')
x.geometry('500x500+500+100')
x.resizable(width=False, height=False)
x.config(bg='#010a3b')  # Cor de fundo da janela


def btNumeros(numero):  # função que ativa os botões numéricos
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, END)
    campoNumeros.insert(0, str(pegaNumero) + str(numero))
    return

def limpa():
    campoNumeros.delete(0, END)
    return

def igual():
    expressao = campoNumeros.get()
    resultado = insere_pilha(insere_lista(expressao))
    campoNumeros.delete(0, END)
    campoNumeros.insert(0, str(resultado))

# entry
campoNumeros = Entry(x, width=50)
campoNumeros.place(x=90, y=25)

# botões
button1 = Button(x, text='1', relief=FLAT, width=10, height=3, command=lambda: btNumeros(1))
button1.place(x=50, y=150)

button2 = Button(x, text='2', relief=FLAT, width=10, height=3, command=lambda: btNumeros(2))
button2.place(x=150, y=150)

button3 = Button(x, text='3', relief=FLAT, width=10, height=3, command=lambda: btNumeros(3))
button3.place(x=250, y=150)

button4 = Button(x, text='4', relief=FLAT, width=10, height=3, command=lambda: btNumeros(4))
button4.place(x=50, y=225)

button5 = Button(x, text='5', relief=FLAT, width=10, height=3, command=lambda: btNumeros(5))
button5.place(x=150, y=225)

button6 = Button(x, text='6', relief=FLAT, width=10, height=3, command=lambda: btNumeros(6))
button6.place(x=250, y=225)

button7 = Button(x, text='7', relief=FLAT, width=10, height=3, command=lambda: btNumeros(7))
button7.place(x=50, y=300)

button_8 = Button(x, text='8', relief=FLAT, width=10, height=3, command=lambda: btNumeros(8))
button_8.place(x=150, y=300)

button_9 = Button(x, text='9', relief=FLAT, width=10, height=3, command=lambda: btNumeros(9))
button_9.place(x=250, y=300)

button_0 = Button(x, text='0', relief=FLAT, width=10, height=3, command=lambda: btNumeros(0))
button_0.place(x=150, y=375)

virgula_button = Button(x, text='Clear', relief=FLAT, width=10, height=3, command=limpa)
virgula_button.place(x=250, y=375)

brabo_button = Button(x, text='(┬┬﹏┬┬)', relief=FLAT, width=10, height=3, command=igual)
brabo_button.place(x=50, y=375)

igual_button = Button(x, text='=', relief=FLAT, width=10, height=3, command=igual)
igual_button.place(x=350, y=375)

divisao_button = Button(x, text='/', relief=FLAT, width=10, height=3, command=lambda: btNumeros('/'))
divisao_button.place(x=350, y=75)

multiplicacao_button = Button(x, text='*', relief=FLAT, width=10, height=3, command=lambda: btNumeros('*'))
multiplicacao_button.place(x=350, y=150)

soma_button = Button(x, text='+', relief=FLAT, width=10, height=3, command=lambda: btNumeros('+'))
soma_button.place(x=350, y=225)

subtracao_button = Button(x, text='-', relief=FLAT, width=10, height=3, command=lambda: btNumeros('-'))
subtracao_button.place(x=350, y=300)

botao_abre_parenteses = Button(x, text='(', relief=FLAT, width=10, height=3, command=lambda: btNumeros('('))
botao_abre_parenteses.place(x=50, y=75)

botao_fecha_parenteses = Button(x, text=')', relief=FLAT, width=10, height=3, command=lambda: btNumeros(')'))
botao_fecha_parenteses.place(x=150, y=75)

Potencia_button = Button(x, text='**', relief=FLAT, width=10, height=3, command=lambda: btNumeros('**'))
Potencia_button.place(x=250, y=75)

x.mainloop()



#(2*2)*7/2-1+2
#(2**3*2)-2
#(2*2/4*2)+2

