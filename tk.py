from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("300x400") #Tamanho da tela
root.title("Aplicação") #Titulo da pagina
root.config(bg="grey") #Configurações de design 
label = tk.Label(
    text = "Olá, seja bem vindo!",
    bg='white',
    fg='black',
    width = 20,
    height = 5,
    font = 4
)
label.pack() #Para executar a variavel

label = tk.Label(text="Nome:",)
entry = tk.Entry(width=40)
label.pack(pady=(10, 5))
entry.pack(pady=(0, 5))

label = tk.Label(text="Email:",)
entry = tk.Entry(width=40)
label.pack(pady=(10, 5))
entry.pack(pady=(0, 5))

botao = tk.Button(root,text="Login",
width= 15,                  
)
botao.pack(pady=(10, 5))

root.mainloop() #Comando para funcionar, tem que está ao final do COD