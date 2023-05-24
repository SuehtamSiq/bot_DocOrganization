import tkinter
from tkinter import *
import os


def button1():
    app = Tk()
    app.title('OrgDoc')
    app.geometry("250x300")

    tit_orientacao = Label(app, text="Organizar Documentação")
    tit_orientacao.grid(column=5, row=0)

    chk_valor = tkinter.BooleanVar()
    chk_valor.set(True)

    chk_teste = tkinter.Checkbutton(app, text='Teste', variable=chk_valor)
    chk_teste.grid(column=0, row=5)

    def organize():
        user = os.getlogin()
        nome_pasta = 'Documents'
        diretorio = r'C:\Users\{}\Documents'.format(user)
        nova_pasta = nome_pasta
        contador = 1
        caminho_pasta = os.path.join(diretorio, nova_pasta) # Caminho completo para a pasta

        while os.path.exists(caminho_pasta):
            # Se a pasta já existe, adiciona um número sequencial ao final do nome
            nova_pasta = f'{nome_pasta}_{contador}'
            contador += 1
            caminho_pasta = os.path.join(diretorio, nova_pasta)
        os.mkdir(caminho_pasta) # Cria a nova pasta

    bot = Button(app, text="Avançar", command=organize)
    bot.grid(column=5, row=10)


# Criando Janela

janela = Tk()

janela.title("MDO")
janela.geometry("360x400")

texto_orientacao = Label(janela, text="============= Machine Doc Organization =============")
texto_orientacao.grid(column=0, row=0)

# Criando botões, e atríbuindo as respectivas funções.
botao = Button(janela, text="Organizar Documentos", command=button1)
botao.grid(column=0, row=1)

botao_2 = Button(janela, text="Enviar e-mail")
botao_2.grid(column=0, row=50)

janela.mainloop()

# By Matheus Siqueira

