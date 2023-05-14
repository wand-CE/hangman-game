"""
Wanderson Soares dos Santos - UTF-8 - Pt-br - 31-03-2023
Model_definição das classes do jogo
"""
from tkinter import *
from tkinter import ttk
from random import choice
from tkinter.messagebox import askyesno
from string import ascii_uppercase
from dao import dicionario

class Tela(Tk):
    """Cria a classe Tela herdando da super classe Tk"""
    def __init__(self):
        super().__init__()
        self.geometry('1200x500')
        self.resizable(False, False)
        self.title('Jogo da Forca')
        self.principal = Label(self)
        self.principal.place(x=0, y=0, w=1200, h=500)
        self.tela_principal()


    def tela_principal(self):
        """método com caracteristicas para a pagina inicial"""
        self.imagem()
        self.contador_erro = 1
        self.letras_preenchidas = 0
        self.lista_botoes_alfabeto = []
        self.lista_letras_na_tela = []
        self.alfabeto()
        self.palavra = self.escolhe_palavra()
        self.label_dica = Label(self.principal, text=f'DICA: {self.palavra[0]}', font=('Arial', 25)).place(x=300,y=20, h=50, w=350)
        for i in range(len(self.palavra[1])):
            self.linha = Label(self.principal, text='_', font=('Arial', 50)).place(x=(300+(i*60)),y=170, h=100, w=50)


    def escolhe_palavra(self):
        """método que escolhe aleatoriamente dentro do dicionario.txt uma palavra para jogar"""
        self.dicionario = dicionario()
        key = choice(list(self.dicionario))
        word = choice(self.dicionario[key])
        return key, word

    def imagem(self):
        """método que coloca a imagem da forca na tela"""
        self.img = PhotoImage(file='imagens/corpo_1.png')
        self.label_forca = Label(self, image=self.img)
        self.label_forca.place(x=20,y=20, h=460, w=260)

    def popula_palavra(self, letra, posicao):
        """metodo que verifica se a letra apertada esta na palavra, e caso esteja coloca a mesma na tela"""
        self.lista_botoes_alfabeto[posicao].config(state='disabled')
        pos_letras = [i for i,e in enumerate(self.palavra[1]) if e==letra]
        if len(pos_letras) == 0:
            self.contador_erro += 1
            self.img['file'] = f'imagens/corpo_{self.contador_erro}.png'
            self.label_forca['image']=self.img
            if self.contador_erro == 7:
                jogar = askyesno(title='Jogar Novamente',
                                         message=f'Você Perdeu!!!\nA palavra era: {self.palavra[1]}\nDeseja jogar novamente??')
                self.destroy() if not jogar else self.reiniciar()

        else:
            for i in range(len(pos_letras)):
                word = Label(self, text=letra.upper(), fg='black', font=('Arial', 40))
                word.place(x=(300+(pos_letras[i]*60)),y=190, h=50, w=50)
                self.lista_letras_na_tela.append(word)
                self.letras_preenchidas += 1
            if self.letras_preenchidas == len(self.palavra[1]):
                jogar = askyesno(title='Jogar Novamente',
                                         message='Você Venceu!!!\nDeseja jogar novamente??')
                self.reiniciar() if jogar else self.destroy()

    def alfabeto(self):
        """metodo que coloca na tela as letras do alfabeto em forma de botão"""
        alfabeto = list(ascii_uppercase)
        for i in range(3):
            for j in range(9):
                try:
                    texto = alfabeto[(i*9)+j]
                    s = ttk.Style()
                    s.configure('my.TButton', font=('Helvetica', 20))
                    botao_teclado = ttk.Button(self.principal, text=texto, style='my.TButton',
                                               command=lambda texto=texto.lower(), posicao=(i*9)+j: self.popula_palavra(texto, posicao))
                    botao_teclado.place(x=(300+(j*60)),y=(300+(i*60)), h=60, w=60)
                    self.lista_botoes_alfabeto.append(botao_teclado)
                except IndexError:
                    pass



    def reiniciar(self):
        """método que reinicia o jogo com uma nova palavra"""
        [widget.destroy() for widget in self.principal.winfo_children()]
        for i in range(len(self.lista_letras_na_tela)):
            self.lista_letras_na_tela[i].destroy()
        self.tela_principal()
