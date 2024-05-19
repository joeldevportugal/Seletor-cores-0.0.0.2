# importar as Bibliotecas a Usar ---------------------------------------------------
from tkinter import Label, messagebox
import customtkinter
import pyperclip 
#------------------------------------------------------------------------------------
# criar Todo O back end -------------------------------------------------------------
def atualizar_cor(event=None):
    r = int(Svermelho.get())
    g = int(Sverde.get())
    b = int(SAzul.get())
    cor_hex = f'#{r:02x}{g:02x}{b:02x}'
    Lcor.config(bg=cor_hex)
    Lvermelho.config(text=f'Vermelho {r}')
    Lverde.config(text=f'Verde {g}')
    LAzul.config(text=f'Azul {b}')
    EHexa.delete(0, 'end')
    EHexa.insert(0, cor_hex)

def Limpar ():
   Svermelho.set(0)
   Sverde.set(0)
   SAzul.set(0)
   Lvermelho.config(text="Vermelho 0")
   Lverde.config(text="Verde 0")
   LAzul.config(text="Azul 0")
   Lcor.config(bg=co2)
   EHexa.delete(0, 'end')
   messagebox.showinfo("Limpeza", "Limpeza de dados efectuada Com Sucesso ...")

def copiar():
    pyperclip.copy(EHexa.get())
    messagebox.showinfo("Copia", "Dados copiados Com sucesso")

def sair():
    resposta = messagebox.askyesno("Fechar Aplicação", "Você deseja fechar a aplicação?")
    if resposta:
        Janela.quit()     
#-----------------------------------------------------------------------------------
# defenir as Cores a Usar --------------------------------------------------------
Co1 ="#FFFFFF" # cor Branca Para Janela 
co2 ="#000000" # cor preta para Lcor
co3 ="#F1EEE3" # Cor Verde Claro Botões 
#---------------------------------------------------------------------------------
Janela = customtkinter.CTk()
Janela.geometry('644x480+100+100')
Janela.resizable(False, False)
Janela.config(bg=Co1)
Janela.title('Selector 0.0.0.2 Dev Joel Portugal 2024 ©')
#---------------------------------------------------------------------------------
# criar Todo O front End ---------------------------------------------------------
# criar O Lcor ------------------------------------------------------------------
Lcor = Label(Janela, width=110, height=20, bg=co2)
Lcor.place(x=10, y=0)
# --------------------------------------------------------------------------------
# criar Os Labels de Control -----------------------------------------------------
Lvermelho = Label(Janela, text='Vermelho 0', font=('arial 14'), bg=Co1)
Lvermelho.place(x=10, y=315)
Lverde = Label(Janela, text='Verde 0', font=('arial 14'), bg=Co1)
Lverde.place(x=10, y=385)
LAzul = Label(Janela, text='Azul 0', font=('arial 14'), bg=Co1)
LAzul.place(x=10, y=450)
# -------------------------------------------------------------------------------
# criar os Sliders --------------------------------------------------------------
Svermelho = customtkinter.CTkSlider(Janela, width=620, bg_color=Co1, to=0, from_=255, command=atualizar_cor)
Svermelho.place(x=10, y=285)
Sverde = customtkinter.CTkSlider(Janela, width=620, bg_color=Co1, to=0, from_=255, command=atualizar_cor)
Sverde.place(x=10, y=335)
SAzul = customtkinter.CTkSlider(Janela, width=620, bg_color=Co1, to=0, from_=255, command=atualizar_cor)
SAzul.place(x=10, y=395)
# ------------------------------------------------------------------------------
# criar a Entry ----------------------------------------------------------------
EHexa = customtkinter.CTkEntry(Janela, width=85, bg_color=Co1)
EHexa.place(x=10, y=435)
# -----------------------------------------------------------------------------
# criar Os Botões  ------------------------------------------------------------
Bcopiar = customtkinter.CTkButton(Janela, text='Copiar', width=85, bg_color=Co1, fg_color=co3, text_color=co2,command=copiar)
Bcopiar.place(x=100, y=435)
Blimpar = customtkinter.CTkButton(Janela, text='Limpar', width=85, bg_color=Co1, fg_color=co3,text_color=co2,command=Limpar)
Blimpar.place(x=190, y=435)
BSair = customtkinter.CTkButton(Janela, text='Sair', width=85, bg_color=Co1, fg_color=co3,text_color=co2,command=sair)
BSair.place(x=280, y=435)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Iniciar a Nossa Janela ------------------------------------------------------
Janela.mainloop()
#------------------------------------------------------------------------------