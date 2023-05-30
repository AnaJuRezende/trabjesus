from tkinter import messagebox
from tkinter import *
import re
import sqlite3
import tkinter as tk

janela = Tk()
janela.title("Página Principal")
janela.geometry("500x500")
janela.configure(bg="#F8F8F8")

def salvar():
  messagebox.showinfo("Sucesso", "Salvo com sucesso!")

def carregar():
  messagebox.showinfo("Sucesso!", "Carregado com sucesso!")

def sair():
  janela.destroy()

mainmenu = Menu(janela)
mainmenu.add_command(label="Salvar", command=salvar)
mainmenu.add_command(label="Carregar", command=carregar)
mainmenu.add_command(label="Sair", command=sair)

janela.config(menu=mainmenu)

def abrir_janela_login():
  janela_login = Toplevel(janela)
  janela_login.title("Página de Login")
  janela_login.geometry("500x500")
  janela_login.configure(bg="#F8F8F8")

  titulo_label = Label(janela_login,
                       text="Login",
                       font="Times 16 bold",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=20)

  frame = Frame(janela_login, bg="#F8F8F8")
  frame.pack(pady=10)

  cpf_label = Label(frame,
                    text="CPF:",
                    font="Times 12",
                    bg="#F8F8F8",
                    fg="#333333")
  cpf_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
  cpf_entry = Entry(frame, font="Times 12")
  cpf_entry.grid(row=0, column=1, padx=5, pady=5)

  senha_label = Label(frame,
                      text="Senha:",
                      font="Times 12",
                      bg="#F8F8F8",
                      fg="#333333")
  senha_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
  senha_entry = Entry(frame, show="*", font="Times 12")
  senha_entry.grid(row=1, column=1, padx=5, pady=5)

  def login():
    cpf = cpf_entry.get()
    global senha
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cpf, senha FROM usuarios WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    if resultado and resultado[1] == senha:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "CPF ou senha incorretos!")
    cursor.close()
    conn.close()
    login(cpf_entry.get(), senha_entry.get())

  login_button = Button(janela_login,
                        text="Login",
                        command=login,
                        font="Times 12",
                        bg="#333333",
                        fg="#FFFFFF",
                        relief=RAISED)
  login_button.pack(pady=10)

  titulo_label = Label(janela_login,
                       text="Não tem conta? Faça o seu cadastro!",
                       font="Times 12",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=20)

  cadastrar_button = Button(janela_login,
                            text="Cadastrar usuário",
                            command=janela_cadastro,
                            font="Times 12",
                            bg="#333333",
                            fg="#FFFFFF",
                            relief=RAISED)
  cadastrar_button.pack(pady=10)

  mainmenu = Menu(janela_login)
  mainmenu.add_command(label="Salvar", command=salvar)
  mainmenu.add_command(label="Carregar", command=carregar)
  mainmenu.add_command(label="Sair", command=sair)

  janela_login.config(menu=mainmenu)

  janela_login.mainloop()

def janela_atualizarproduto():
  janela_atualizarproduto = Toplevel(janela)
  janela_atualizarproduto.title("Página de atualização de produto")
  janela_atualizarproduto.geometry("500x400")
  janela_atualizarproduto.configure(bg="#F8F8F8")

  global novo_nomeprodu_entry, novo_valor_entry, novo_fornecedor_entry, nova_quantidade_entry

  titulo_label = Label(janela_atualizarproduto,
                       text="Atualização de produto",
                       font="Times 14 bold",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=20)

  frame = Frame(janela_atualizarproduto, bg="#F8F8F8")
  frame.pack(pady=10)

  novo_nomeprodu_label = Label(frame,
                          text="Novo nome:",
                          font="Times 12",
                          bg="#F8F8F8",
                          fg="#333333")
  novo_nomeprodu_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
  novo_nomeprodu_entry = Entry(frame, font="Times 12")
  novo_nomeprodu_entry.grid(row=0, column=1, padx=5, pady=5)

  novo_fornecedor_label = Label(frame,
                           text="Novo fornecedor:",
                           font="Times 12",
                           bg="#F8F8F8",
                           fg="#333333")
  novo_fornecedor_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
  novo_fornecedor_entry = Entry(frame, font="Times 12")
  novo_fornecedor_entry.grid(row=1, column=1, padx=5, pady=5)

  novo_valor_label = Label(frame,
                      text="Novo valor:",
                      font="Times 12",
                      bg="#F8F8F8",
                      fg="#333333")
  novo_valor_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
  novo_valor_entry = Entry(frame, font="Times 12")
  novo_valor_entry.grid(row=2, column=1, padx=5, pady=5)

  nova_quantidade_label = Label(frame,
                           text="Nova quantidade:",
                           font="Times 12",
                           bg="#F8F8F8",
                           fg="#333333")
  nova_quantidade_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
  nova_quantidade_entry = Entry(frame, font="Times 12")
  nova_quantidade_entry.grid(row=3, column=1, padx=5, pady=5)

  atualizarproduto_button = Button(janela_atualizarproduto,
                                   text="Atualizar produto",
                                   command=salvar_edicao,
                                   font="Times 12",
                                   bg="#333333",
                                   fg="#FFFFFF",
                                   relief=RAISED)
  atualizarproduto_button.pack(pady=10)

  mainmenu = Menu(janela_atualizarproduto)
  mainmenu.add_command(label="Salvar", command=salvar)
  mainmenu.add_command(label="Carregar", command=carregar)
  mainmenu.add_command(label="Sair", command=sair)

  janela_atualizarproduto.config(menu=mainmenu)

  janela_atualizarproduto.mainloop()

def janela_cadastroproduto():
  janela_cadastroproduto = Toplevel(janela)
  janela_cadastroproduto.title("Página de cadastro de produto")
  janela_cadastroproduto.geometry("500x500")
  janela_cadastroproduto.configure(bg="#F8F8F8")

  global nomeprodu_entry, fornecedor_entry, quantidade_entry, valor_entry

  titulo_label = Label(janela_cadastroproduto,
                       text="Cadastro de produto",
                       font="Times 14 bold",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=10)

  frame = Frame(janela_cadastroproduto, bg="#F8F8F8")
  frame.pack(pady=10)

  nomeprodu_label = Label(frame,
                          text="Nome:",
                          font="Times 12",
                          bg="#F8F8F8",
                          fg="#333333")
  nomeprodu_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
  nomeprodu_entry = Entry(frame, font="Times 12")
  nomeprodu_entry.grid(row=0, column=1, padx=5, pady=5)

  fornecedor_label = Label(frame,
                           text="Fornecedor:",
                           font="Times 12",
                           bg="#F8F8F8",
                           fg="#333333")
  fornecedor_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
  fornecedor_entry = Entry(frame, font="Times 12")
  fornecedor_entry.grid(row=1, column=1, padx=5, pady=5)

  valor_label = Label(frame,
                      text="Valor:",
                      font="Times 12",
                      bg="#F8F8F8",
                      fg="#333333")
  valor_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
  valor_entry = Entry(frame, font="Times 12")
  valor_entry.grid(row=2, column=1, padx=5, pady=5)

  quantidade_label = Label(frame,
                           text="Quantidade:",
                           font="Times 12",
                           bg="#F8F8F8",
                           fg="#333333")
  quantidade_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
  quantidade_entry = Entry(frame, font="Times 12")
  quantidade_entry.grid(row=3, column=1, padx=5, pady=5)

  cadastroprodu_button = Button(janela_cadastroproduto,
                                text="Cadastrar produto",
                                command=cadastrar_produto,
                                font="Times 12",
                                bg="#333333",
                                fg="#FFFFFF",
                                relief=RAISED)
  cadastroprodu_button.pack(pady=10)

  mainmenu = Menu(janela_cadastroproduto)
  mainmenu.add_command(label="Salvar", command=salvar)
  mainmenu.add_command(label="Carregar", command=carregar)
  mainmenu.add_command(label="Sair", command=sair)

  janela_cadastroproduto.config(menu=mainmenu)

  janela_cadastroproduto.mainloop()

def janela_cadastro():
  janela_cadastro = Toplevel(janela)
  janela_cadastro.title("Página de Cadastro")
  janela_cadastro.geometry("500x500")
  janela_cadastro.configure(bg="#F8F8F8")
  
  global nome_entry, email_entry, cpf_entry, senha_entry

  titulo_label = Label(janela_cadastro,
                       text="Cadastro de usuário",
                       font="Times 14 bold",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=20)

  frame = Frame(janela_cadastro, bg="#F8F8F8")
  frame.pack(pady=10)
  
  nome_label = Label(frame,
                     text="Nome:",
                     font="Times 12",
                     bg="#F8F8F8",
                     fg="#333333")
  nome_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
  nome_entry = Entry(frame, font="Times 12")
  nome_entry.grid(row=0, column=1, padx=5, pady=5)

  email_label = Label(frame,
                      text="E-mail:",
                      font="Times 12",
                      bg="#F8F8F8",
                      fg="#333333")
  email_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
  email_entry = Entry(frame, font="Times 12")
  email_entry.grid(row=1, column=1, padx=5, pady=5)

  cpf_label = Label(frame,
                    text="CPF:",
                    font="Times 12",
                    bg="#F8F8F8",
                    fg="#333333")
  cpf_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
  cpf_entry = Entry(frame, font="Times 12")
  cpf_entry.grid(row=2, column=1, padx=5, pady=5)

  senha_label = Label(frame,
                      text="Senha:",
                      font="Times 12",
                      bg="#F8F8F8",
                      fg="#333333")
  senha_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
  senha_entry = Entry(frame, show="*", font="Times 12")
  senha_entry.grid(row=3, column=1, padx=5, pady=5)

  titulo_label = Label(janela_cadastro,
                       text="*Sua senha deve conter até 8 caracteres!",
                       font="Times 10",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=5)

  cadastrar_button = Button(janela_cadastro,
                            text="Cadastrar usuário",
                            command=cadastrar_usuario,
                            font="Times 12",
                            bg="#333333",
                            fg="#FFFFFF",
                            relief=RAISED)
  cadastrar_button.pack(pady=10)

  titulo_label = Label(janela_cadastro,
                       text="Já tem conta? Faça login",
                       font="Times 12",
                       bg="#F8F8F8",
                       fg="#333333")
  titulo_label.pack(pady=20)

  login_button = Button(janela_cadastro,
                        text="Login",
                        command=abrir_janela_login,
                        font="Times 12",
                        bg="#333333",
                        fg="#FFFFFF",
                        relief=RAISED)
  login_button.pack(pady=10)

  mainmenu = Menu(janela_cadastro)
  mainmenu.add_command(label="Salvar", command=salvar)
  mainmenu.add_command(label="Carregar", command=carregar)
  mainmenu.add_command(label="Sair", command=sair)

  janela_cadastro.config(menu=mainmenu)

  janela_cadastro.mainloop()

titulo_label = Label(janela,
                     text="Seja bem-vindo!",
                     font="Times 14 bold",
                     bg="#F8F8F8",
                     fg="#333333")
titulo_label.pack(pady=10)

titulo_label = Label(janela,
                     text="Já tem conta? Faça login!",
                     font="Times 12",
                     bg="#F8F8F8",
                     fg="#333333")
titulo_label.pack(pady=10)

login_button = Button(janela,
                      text="Login",
                      command=abrir_janela_login,
                      font="Times 12",
                      bg="#333333",
                      fg="#FFFFFF",
                      relief=RAISED)
login_button.pack(pady=4)

titulo_label = Label(janela,
                     text="Não tem conta? Faça o seu cadastro!",
                     font="Times 12",
                     bg="#F8F8F8",
                     fg="#333333")
titulo_label.pack(pady=10)

cadastrar_button = Button(janela,
                          text="Cadastrar",
                          command=janela_cadastro,
                          font="Times 12",
                          bg="#333333",
                          fg="#FFFFFF",
                          relief=RAISED)
cadastrar_button.pack(pady=4)

titulo_label = Label(janela,
                     text="Deseja cadastrar algum produto?",
                     font="Times 12",
                     bg="#F8F8F8",
                     fg="#333333")
titulo_label.pack(pady=10)

cadastrarprodu_button = Button(janela,
                               text="Cadastrar produto",
                               command=janela_cadastroproduto,
                               font="Times 12",
                               bg="#333333",
                               fg="#FFFFFF",
                               relief=RAISED)
cadastrarprodu_button.pack(pady=4)

titulo_label = Label(janela,
                     text="Deseja atualizar os produtos?",
                     font="Times 12",
                     bg="#F8F8F8",
                     fg="#333333")
titulo_label.pack(pady=10)

atualizarproduto_button = Button(janela,
                                 text="Atualizar produto",
                                 command=janela_atualizarproduto,
                                 font="Times 12",
                                 bg="#333333",
                                 fg="#FFFFFF",
                                 relief=RAISED)
atualizarproduto_button.pack(pady=4)

def criar_tabela_usuarios():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE usuarios
                 (nome TEXT, email TEXT, cpf TEXT, senha TEXT)''')
    conn.commit()
    conn.close()

def criar_tabela_produtos():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE produtos
                 (nome TEXT, fornecedor TEXT, valor TEXT, quantidade INTEGER)''')
    conn.commit()
    conn.close()

def cadastrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    cpf = cpf_entry.get()
    senha = senha_entry.get()
    
    if nome == "" or email == "" or cpf == "" or senha == "":
        messagebox.showerror("Erro!", "Preencha todos os campos!")
        return
    if not re.match("^[a-zA-ZÀ-ÿ ]+$", nome):
        messagebox.showerror("Erro!", "Nome inválido, tente novamente!")
        return
    if not re.match("^[a-zA-Z0-9]{1,8}$", senha):
        messagebox.showerror("Erro!", "Senha inválida, tente novamente!")
        return
    if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        messagebox.showerror("Erro!", "Email inválido, tente novamente!")
        return
    if not re.match("^[0-9]{11}$", cpf):
        messagebox.showerror("Erro!", "CPF inválido, tente novamente!")
        return
    else:
       messagebox.showinfo("Sucesso!", "Usuário cadastrado com sucesso!")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", (nome, email, cpf, senha))
    conn.commit()
    conn.close()

def editar_produto(nomeprodu):
   if not nomeprodu:
    messagebox.showerror("Erro", "Por favor, insira o nome do produto existente")
    return
    
def salvar_edicao():
    novo_nomeprodu =  novo_nomeprodu_entry.get()
    novo_fornecedor =  novo_fornecedor_entry.get()
    novo_valor =  novo_valor_entry.get()
    nova_quantidade =  nova_quantidade_entry.get()
    global nomeprodu

    if not novo_nomeprodu or not novo_fornecedor or not novo_valor or not nova_quantidade:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        return
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE produtos SET nome = ?, fornecedor = ?, valor = ?, quantidade = ? WHERE nomeprodu = ?",
                 (novo_nomeprodu, novo_fornecedor, novo_valor, nova_quantidade, nomeprodu))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")

def cadastrar_produto():
    nomeprodu = nomeprodu_entry.get()
    fornecedor = fornecedor_entry.get()
    valor = valor_entry.get()
    quantidade = quantidade_entry.get()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?)", (nomeprodu, fornecedor, valor, quantidade))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso!", "Produto Cadastrado com Sucesso!")


janela.mainloop()
