import tkinter as tk
from tkinter import messagebox
import os
import shutil


def organize(extensoes, nomes_pastas):
    extensoes_selecionadas = [ext for ext, var in zip(extensoes, checkbox_vars) if var.get()]
    nomes_pastas_selecionados = [nome for nome, var in zip(nomes_pastas, checkbox_vars) if var.get()]

    if extensoes_selecionadas:
        user = os.getlogin()
        diretorio = r'C:\Users\{}\Documents'.format(user)
        contador = 1
        arquivos_encontrados = False  # Variável para verificar se foram encontrados arquivos para organização

        # Obter o caminho para o diretório de downloads
        diretorio_down = r'C:\Users\{}\Downloads'.format(user)
        pasta_downloads = os.path.join(diretorio_down)

        # Obter todos os arquivos com as extensões selecionadas na pasta de downloads
        arquivos = [f for f in os.listdir(pasta_downloads) if os.path.splitext(f)[1] in extensoes_selecionadas]

        # Verificar se foram encontrados arquivos para organização
        if arquivos:
            for nome_pasta in nomes_pastas_selecionados:
                caminho_pasta = os.path.join(diretorio, nome_pasta)

                while os.path.exists(caminho_pasta):
                    # Se a pasta já existe, adiciona um número sequencial ao final do nome
                    nome_pasta = f'{nome_pasta}_{contador}'
                    contador += 1
                    caminho_pasta = os.path.join(diretorio, nome_pasta)  # Caminho completo para a pasta

                os.mkdir(caminho_pasta)  # Cria a nova pasta

            # Mover os arquivos para as respectivas pastas
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_downloads, arquivo)
                extensao = os.path.splitext(arquivo)[1]
                for nome_pasta, ext in zip(nomes_pastas_selecionados, extensoes_selecionadas):
                    if ext == extensao:
                        caminho_pasta = os.path.join(diretorio, nome_pasta)
                        shutil.move(caminho_arquivo, caminho_pasta)
                        arquivos_encontrados = True  # Indica que pelo menos um arquivo foi encontrado

            messagebox.showinfo('Sucesso', 'Pastas criadas com sucesso e arquivos movidos!')
        else:
            resposta = messagebox.askquestion('Atenção',
                                              'Não foram encontrados arquivos com as extensões selecionadas. '
                                              'Deseja criar as pastas mesmo assim?')
            if resposta == 'yes':
                for nome_pasta in nomes_pastas_selecionados:
                    caminho_pasta = os.path.join(diretorio, nome_pasta)

                    while os.path.exists(caminho_pasta):
                        # Se a pasta já existe, adiciona um número sequencial ao final do nome
                        nome_pasta = f'{nome_pasta}_{contador}'
                        contador += 1
                        caminho_pasta = os.path.join(diretorio, nome_pasta)  # Caminho completo para a pasta

                    os.mkdir(caminho_pasta)  # Cria a nova pasta

                messagebox.showinfo('Sucesso', 'Pastas criadas com sucesso!')
            else:
                messagebox.showinfo('Aviso', 'Nenhuma pasta foi criada.')

    else:
        messagebox.showwarning('Atenção', 'Você precisa selecionar pelo menos uma extensão.')


def open_second_window():
    # Criando janela secundária
    second_window = tk.Toplevel(janela)
    second_window.title('DocOgn')
    second_window.geometry('200x100')

    # Criando caixa de seleção e botão para cada extensão desejada
    extensoes = ['.pdf', '.docx', '.xlsx']  # Exemplo de extensões
    nomes_pastas = ['Documents', 'WordFiles', 'ExcelFiles']  # Exemplo de nomes de pastas

    for extensao, nome_pasta, var in zip(extensoes, nomes_pastas, checkbox_vars):
        checkbox = tk.Checkbutton(second_window, text=extensao, variable=var)
        checkbox.pack()

    button = tk.Button(second_window, text='Avançar',
                       command=lambda: close_second_window(second_window, extensoes, nomes_pastas))
    button.pack()


def close_second_window(window, extensoes, nomes_pastas):
    organize(extensoes, nomes_pastas)
    window.destroy()


# Criando Janela Principal
janela = tk.Tk()
janela.title('MDO')
janela.geometry('360x400')

texto_orientacao = tk.Label(janela, text='============= Machine Doc Organization =============')
texto_orientacao.grid(column=0, row=0)

# Criando botões e atribuindo as respectivas funções
botao = tk.Button(janela, text='Organizar Documentos', command=open_second_window)
botao.grid(column=0, row=1)

botao_2 = tk.Button(janela, text='Enviar e-mail')
botao_2.grid(column=0, row=50)

# Criar uma lista de variáveis Booleanas para controlar as caixas de seleção
checkbox_vars = [tk.BooleanVar() for _ in range(3)]

janela.mainloop()

# By Matheus Siqueira
