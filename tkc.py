import customtkinter as ctk
ctk.set_appearance_mode("dark") #Tema

def validar_login():
    usuario = campo_user.get()
    senha = campo_senha.get()
    if usuario == 'root' and senha == '1234':
        resultado.configure(text="Login efetuado com sucesso!", text_color="green")
    else:
        resultado.configure(text="Login incorreto!", text_color="red")  

#criar as funcionalidades
app = ctk.CTk() #Função onde a janela vai ser aberta
app.title("Sistema de login")
app.geometry("500x500")

#Campo Usuario
lab_user = ctk.CTkLabel(app, text="Usuario")
lab_user.pack(pady=(10, 5)) #Para executar
campo_user = ctk.CTkEntry(app, placeholder_text="Digite o nome do usuario")
campo_user.pack(pady=(10, 5))

#Campo Senha
lab_senha = ctk.CTkLabel(app, text="Senha")
lab_senha.pack(pady=(10, 5)) #Para executar
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha")
campo_senha.pack(pady=(10, 5))

botao = ctk.CTkButton(app, text="Login", command = validar_login)
botao.pack(pady=10)
#Campo testar o login
resultado = ctk.CTkLabel(app,text="")
resultado.pack(pady=10)

app.mainloop()
