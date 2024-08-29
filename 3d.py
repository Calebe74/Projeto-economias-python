from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk  # Correção na importação

from tkinter import filedialog

# Cores
co0 = "#f0f3f5"  # Preto
co1 = "#feffff"  # Branco
co2 = "#4fa882"  # Verde 
co3 = "#38576b"  # Valor 
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # Profit

# Janela
janela = Tk()
janela.title("Desenhando Páginas")
janela.geometry('300x380')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

# Abrindo logo
app_img = Image.open('img/lapis.png')
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)  # Correção no uso do ImageTk

app_logo = Label(janela, image=app_img, text='Imagem para > Desenho a Lápis', width=300, compound=LEFT, relief=RAISED, anchor=NW, font=('System', 15, 'bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

global imagem_original
imagem_original = ['']
#função para anexar img
def escolher_img():
    imagem = fd.askopenfilename() ############erradoooooooooooooooooo
    imagem_original.append(imagem)





# Abrindo a imagem
imagem = Image.open('img/sua_imagem.png')  # Caminho da imagem corrigido
imagem = imagem.resize((170, 170))
imagem = ImageTk.PhotoImage(imagem)  # Corrigido para usar a imagem redimensionada

I_imagem = Label(janela, image=imagem, text='Imagem para > Desenho a Lápis', width=300, compound=LEFT, relief=RAISED, anchor=NW, font=('System', 15, 'bold'), bg=co1, fg=co4)
I_imagem.place(x=60, y=60)

# Opções
I_opcao = Label(janela, text="Configurando ---------------------------------".upper(), anchor=NW, font=('Verdana', 17, 'bold'), bg=co1, fg=co4)
I_opcao.place(x=-10, y=260)

escala = Scale(janela, from_= 0, to= 250 , length = 120, bg = co1 , fg = 'red' , orient = HORIZONTAL )
escala.place(x=-10 , y = 300)

b_escolher = Button(janela, text="Escolher imagem ",width=15,overrelief=RIDGE, anchor=NW, font=('ivy', 10, 'bold'), bg=co1, fg=co4)
b_escolher.place(x=-147, y=287)

b_salvar = Button(janela, text="Salvar ",width=15,overrelief=RIDGE, anchor=NW, font=('ivy', 10, 'bold'), bg=co2, fg=co1)
b_salvar.place(x=-147, y=317)

janela.mainloop()
