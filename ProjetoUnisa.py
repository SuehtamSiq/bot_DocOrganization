import tkinter as tk
from tkinter import messagebox
import os
import shutil


def organize():
    if checkbox_var.get():
        user = os.getlogin()
        nome_pasta = 'Documents'
        diretorio = r'C:\Users\{}\Documents'.format(user)
        nova_pasta = nome_pasta
        contador = 1
        caminho_pasta = os.path.join(diretorio, nova_pasta)  # Caminho completo para a pasta

        while os.path.exists(caminho_pasta):
            # Se a pasta já existe, adiciona um número sequencial ao final do nome
            nova_pasta = f'{nome_pasta}_{contador}'
            contador += 1
            caminho_pasta = os.path.join(diretorio, nova_pasta)

        os.mkdir(caminho_pasta)  # Cria a nova pasta

        # Obter o caminho para o diretório de downloads
        diretorio_down = r'C:\Users\{}\Downloads'.format(user)
        pasta_downloads = os.path.join(diretorio_down)

        # Obter todos os arquivos com a extensão .pdf na pasta de downloads
        arquivos_pdf = [f for f in os.listdir(pasta_downloads) if f.endswith('.pdf')]

        # Mover os arquivos para a nova pasta
        for arquivo in arquivos_pdf:
            caminho_arquivo = os.path.join(pasta_downloads, arquivo)
            shutil.move(caminho_arquivo, caminho_pasta)

        messagebox.showinfo('Sucesso', 'Pasta criada com sucesso e arquivos PDF movidos!')
    else:
        messagebox.showwarning('Atenção', 'Você precisa selecionar a caixa de seleção.')


def button1():
    # Criando janela secundária
    second_window = tk.Toplevel(janela)
    second_window.title('DocOgn')
    second_window.geometry('200x100')

    checkbox = tk.Checkbutton(second_window, text='.pdf', variable=checkbox_var)
    checkbox.pack()

    button = tk.Button(second_window, text='Avançar', command=organize)
    button.pack()


# Criando Janela Principal
janela = tk.Tk()
janela.title('MDO')
janela.geometry('360x400')

texto_orientacao = tk.Label(janela, text='============= Machine Doc Organization =============')
texto_orientacao.grid(column=0, row=0)

# Criando botões e atribuindo as respectivas funções
botao = tk.Button(janela, text='Organizar Documentos', command=button1)
botao.grid(column=0, row=1)

botao_2 = tk.Button(janela, text='Enviar e-mail')
botao_2.grid(column=0, row=50)

# Variável para armazenar o estado da caixa de seleção
checkbox_var = tk.BooleanVar()

janela.mainloop()

# By Matheus Siqueira
