import cv2
print(cv2.__version__)
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def executar_cadastro():
    # Executa o cadastro.py
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cadastro.py')
    subprocess.run([sys.executable, script_path])

def executar_login():
    # Executa o login.py
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login.py')
    subprocess.run([sys.executable, script_path])

def listar_usuarios():
    # Mostra os usuários cadastrados
    if not os.path.exists('usuarios'):
        messagebox.showinfo("Usuários cadastrados", "Nenhum usuário encontrado.")
        return

    usuarios = os.listdir('usuarios')
    nomes = [os.path.splitext(usuario)[0] for usuario in usuarios]

    if not nomes:
        messagebox.showinfo("Usuários cadastrados", "Nenhum usuário encontrado.")
        return

    janela = tk.Toplevel(root)
    janela.title("Usuários Cadastrados")

    label = tk.Label(janela, text="Usuários cadastrados:")
    label.pack(pady=10)

    for nome in nomes:
        tk.Label(janela, text=nome).pack()

def excluir_usuario():
    # Exclui usuários cadastrados
    if not os.path.exists('usuarios'):
        messagebox.showinfo("Excluir usuário", "Nenhum usuário cadastrado.")
        return

    usuarios = os.listdir('usuarios')
    nomes = [os.path.splitext(usuario)[0] for usuario in usuarios]

    if not nomes:
        messagebox.showinfo("Excluir usuário", "Nenhum usuário cadastrado.")
        return

    janela = tk.Toplevel(root)
    janela.title("Excluir Usuário")

    label = tk.Label(janela, text="Selecione o usuário a ser excluído:")
    label.pack(pady=10)

    lista = tk.Listbox(janela, height=10, width=30)
    for nome in nomes:
        lista.insert(tk.END, nome)
    lista.pack(pady=5)

    def confirmar_exclusao():
        selecionado = lista.get(tk.ACTIVE)
        if not selecionado:
            messagebox.showwarning("Aviso", "Nenhum usuário selecionado.")
            return
        caminho = os.path.join("usuarios", f"{selecionado}.jpg")
        if os.path.exists(caminho):
            os.remove(caminho)
            messagebox.showinfo("Sucesso", f"Usuário '{selecionado}' excluído com sucesso.")
            janela.destroy()
        else:
            messagebox.showerror("Erro", "Arquivo do usuário não encontrado.")

    botao_excluir = tk.Button(janela, text="Excluir", command=confirmar_exclusao)
    botao_excluir.pack(pady=10)

def sair():
    root.destroy()

# Cria a interface gráfica
root = tk.Tk()
root.title("Reconhecimento Facial")

label_title = tk.Label(root, text="Reconhecimento Facial", font=("Helvetica", 16))
label_title.pack(pady=20)

button_cadastrar = tk.Button(root, text="Cadastrar", width=20, command=executar_cadastro)
button_cadastrar.pack(pady=10)

button_login = tk.Button(root, text="Login", width=20, command=executar_login)
button_login.pack(pady=10)

button_listar = tk.Button(root, text="Ver usuários cadastrados", width=20, command=listar_usuarios)
button_listar.pack(pady=10)

button_excluir = tk.Button(root, text="Excluir Usuário", width=20, command=excluir_usuario)
button_excluir.pack(pady=10)

button_sair = tk.Button(root, text="Sair", width=20, command=sair)
button_sair.pack(pady=10)

root.mainloop()
