# importando as pendencias(muita coisa)
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from view import *

# definindo as cores q vou usar na interfacie
co0 = "#2e2d2b"  
co1 = "#feffff"   
co2 = "#e5e5e5" 
co3 = "#666464"  
co4 = "#403d3d"   
co6 = "#003452"   
co7 = "#ef5350"   
cor_1 = ['#fa5555','#99bb55','#5588bb']
cor_2 = ['#5588bb','#99bb55',]


# começando a janela
janela = Tk ()
janela.title ("")
janela.geometry('1050x580')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

frame_logo = Frame(janela, width=950, height=52, bg=co6, relief="flat")
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=2, ipadx=680)

frame_meio = Frame(janela, width=950, height=270, bg=co3, relief="flat")
frame_meio.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

# dividindo o frame Meio
frame_dados = Frame(frame_meio, width=425, height=280, bg=co1, relief="flat")
frame_dados.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frame_resultado = Frame(frame_meio, width=250, height=270, bg=co1, relief="flat")
frame_resultado.grid(row=0, column=1, pady=0, padx=2, sticky=NSEW)

frame_chart = Frame(frame_meio, width=370, height=270, bg=co1, relief="flat")
frame_chart.grid(row=0, column=2, pady=0, padx=0, sticky=NSEW)

# criando o frame tabela
frame_tabela = Frame(janela, width=650, height=150, bg=co1, relief="flat")
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW)


# frame para a logo e o titulo
app_lg  = Image.open('img/logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo,image=app_lg,  text=" CALCULADORA DE LUCRO PARA PRODUTOS -Calebe Emanoel ", width=1050, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 15'),bg=co1, fg=co4 )
app_logo.place(x=0, y=0)


# função lucro
def lucro():

    global img_salvar, img_calcular, img_deletar


    # função calcular
    def calcular():

        nome = e_nome.get()
        compra = e_compra.get()
        venda = e_venda.get()
        quantidade = e_quantidade.get()
        adicionais = e_adicionais.get()
        frete = e_frete.get()
        

        lista = [nome,compra,venda,quantidade,adicionais,frete]

        # verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # calcular lucro e mostrar dentro do label
        def calcular_lucro(nome_produto,preco_compra,preco_venda,quantidade,custos_adicionais,custo_frete):

            # onde o usuario coloca os dados que sao salvos no view
            nome_produto = nome_produto
            preco_compra = float(preco_compra)
            preco_venda = float(preco_venda)
            quantidade = int(quantidade)
            custos_adicionais = float(custos_adicionais)
            custo_frete = float(custo_frete)

            # calcular o lucro
            custo_total = (preco_compra + custos_adicionais + custo_frete) * quantidade
            lucro = (preco_venda - preco_compra - custos_adicionais - custo_frete) * quantidade
            margem_lucro = lucro / (preco_venda * quantidade) * 100

            # resultados das operações
            l_nome_lucro['text'] = "O lucro do produto {} é de R${:.2f} e a margem de lucro é de {:.2f}%.".format(nome_produto, lucro, margem_lucro)
            l_lucro['text'] = 'R${:.2f}'.format(lucro)
            l_custo['text'] = '{:.2f}%'.format(margem_lucro)
            

        # fazendo o calculo 
        calcular_lucro(nome,compra,venda,quantidade,adicionais,frete)

    # funcao para salvar os dados na planilha
    def salvar_dados():
        nome = e_nome.get()
        compra = e_compra.get()
        venda = e_venda.get()
        quantidade = e_quantidade.get()
        adicionais = e_adicionais.get()
        frete = e_frete.get()
        

        lista = [nome,compra,venda,quantidade,adicionais,frete]

        # verificando caso algum campo esteja vazio
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return

        # fazendo o calculo 
        salvar_produto(nome,compra,venda,quantidade,adicionais,frete)

        # janelinha pra quando der certo
        messagebox.showinfo('Sucesso', 'Produto adicionado com sucesso!')

        # limpando os campos de entradas
        e_nome.delete(0,END)
        e_compra.delete(0,END)
        e_venda.delete(0,END)
        e_quantidade.delete(0,END)
        e_adicionais.delete(0,END)
        e_frete.delete(0,END)

        # mostrando os dados salvos
        grafico_bar()
        mostrar()

    
    # funcao deletar para dados no Excel
    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            valor = treev_lista[0]
            valor = str(valor)
            
            deletar_linha_por_nome(valor,"dados.xlsx")
                    
            messagebox.showinfo('Sucesso', 'Produto eliminado com sucesso!')
            
            # atualizar dados
            mostrar()
            grafico_bar()

        except IndexError:
            messagebox.showerror('Erro', 'Por favor, selecione um dos produtos da tabela!')



    app_ = Label(frame_dados,text="Adicione seu produto!!",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'),bg=co1, fg=co4)
    app_.place(x=0, y=10)
    l_linha = Label(frame_dados, width=500, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.place(x=7, y=47)
    l_linha = Label(frame_dados, width=500, height=1,anchor=NW, font=('Verdana 1 '), bg=co1, fg=co1)
    l_linha.place(x=7, y=50)

    l_nome = Label(frame_dados, text="Nome do produto *", height=1,anchor=NW, font=(' Ivy 10 bold'), bg=co1, fg=co4)
    l_nome.place(x=4, y=70)
    e_nome = Entry(frame_dados, width=20, justify='left',font=(' Ivy 10'),relief=GROOVE, bg=co1,fg=co4)
    e_nome.place(x=7, y=100)

    l_quantidade = Label(frame_dados, text="Qtd do produto *", height=1,anchor=NW, font=(' Ivy 10 bold'), bg=co1, fg=co4)
    l_quantidade.place(x=170, y=70)
    e_quantidade = Entry(frame_dados, width=8, justify='center',font=(' Ivy 10'),relief=GROOVE, bg=co1,fg=co4)
    e_quantidade.place(x=173, y=100)

    l_compra = Label(frame_dados, text="Preço de compra *", height=1,anchor=NW, font=(' Ivy 10 bold'), bg=co1, fg=co4)
    l_compra.place(x=4, y=130)
    e_compra = Entry(frame_dados, width=8,justify='center',font=(' Ivy 10'),relief=GROOVE, bg=co1,fg=co4)
    e_compra.place(x=7, y=160)

    l_venda = Label(frame_dados, text="Preço de venda *", height=1,anchor=NW, font=(' Ivy 10 bold'), bg=co1, fg=co4)
    l_venda.place(x=170, y=130)
    e_venda = Entry(frame_dados, width=8, justify='center',font=(' Ivy 10'),relief=GROOVE, bg=co1,fg=co4)
    e_venda.place(x=173, y=160)

    l_frete = Label(frame_dados, text="Custo médio de frete *", height=1,anchor=NW, font=(' Ivy 10 bold'), bg=co1, fg=co4)
    l_frete.place(x=4, y=200)
    e_frete = Entry(frame_dados, width=8,justify='center',font=(' Ivy 10'),relief=GROOVE, bg=co1,fg=co4)
    e_frete.place(x=7, y=230)

    l_adicionais = Label(frame_dados, text="Custos adicionais *", height=1,anchor=NW, font=(' Ivy 10 bold'), bg=co1, fg=co4)
    l_adicionais.place(x=170, y=200)
    e_adicionais = Entry(frame_dados, width=8, justify='center',font=(' Ivy 10'),relief=GROOVE, bg=co1,fg=co4)
    e_adicionais.place(x=173, y=230)
    
    #botões
    img_calcular = Image.open('img/calcular.png')
    img_calcular = img_calcular.resize((18, 18))
    img_calcular = ImageTk.PhotoImage(img_calcular)
    b_calcular = Button(frame_dados, command=calcular, image=img_calcular, compound=LEFT,width=100, text='  Calcular' ,bg=co1, fg=co4,font=('Ivy 11'), overrelief=RIDGE)
    b_calcular.place(x=312, y=140)

    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frame_dados, command=salvar_dados, image=img_salvar, compound=LEFT,width=100, text='  Salvar' ,bg=co1, fg=co4,font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.place(x=312, y=180)

    img_deletar = Image.open('img/delete.png')
    img_deletar = img_deletar.resize((18, 18))
    img_deletar = ImageTk.PhotoImage(img_deletar)
    b_deletar = Button(frame_dados, command=deletar, image=img_deletar, compound=LEFT,width=100, text='  Deletar' ,bg=co1, fg=co4,font=('Ivy 11'), overrelief=RIDGE)
    b_deletar.place(x=312, y=220)

    # linhas para deixar mais organizado
    l_linha = Label(frame_dados, width=1, height=100,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.place(x=152, y=137)
    l_linha = Label(frame_dados, width=1, height=100,anchor=NW, font=('Verdana 1 '), bg=co1, fg=co1)
    l_linha.place(x=150, y=137)

    l_linha = Label(frame_dados, width=1, height=100,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.place(x=298, y=137)
    l_linha = Label(frame_dados, width=1, height=100,anchor=NW, font=('Verdana 1 '), bg=co1, fg=co1)
    l_linha.place(x=296, y=137)


    #resultado
    app_ = Label(frame_resultado,text="Resultado da operacao",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'),bg=co1, fg=co4)
    app_.place(x=0, y=10)
    l_linha = Label(frame_resultado, width=500, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.place(x=7, y=47)
    l_linha = Label(frame_resultado, width=500, height=1,anchor=NW, font=('Verdana 1 '), bg=co1, fg=co1)
    l_linha.place(x=7, y=50)

    l_nome_lucro = Label(frame_resultado, text="",wraplength=220, justify=LEFT, pady=2, height=3,anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_nome_lucro.place(x=4, y=70)
    l_lucro = Label(frame_resultado, text="R$0,00",width=20, height=1,anchor=E, relief=RIDGE, font=(' Ivy 15'), bg=co1, fg=co4)
    l_lucro.place(x=4, y=140)

    l_custo = Label(frame_resultado, text="0,00%",width=20, height=1,anchor=E, relief=RIDGE, font=(' Ivy 15'), bg=co1, fg=co4)
    l_custo.place(x=4, y=180)
    

lucro()


# parte complicada(grafico da direita)
def grafico_bar():

    app_ = Label(frame_chart,text="Estatisticas dos produtos salvados",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'),bg=co1, fg=co4)
    app_.place(x=0, y=10)
    l_linha = Label(frame_chart, width=500, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.place(x=7, y=47)
    l_linha = Label(frame_chart, width=500, height=1,anchor=NW, font=('Verdana 1 '), bg=co1, fg=co1)
    l_linha.place(x=7, y=50)


    # obtendo valores colocados pelo usuario
    lista_nomes = ['Valor total de custo', 'Lucro líquido total','Margem de lucro total']
    lista_valores = estatistica()
    simbolos = ['R$','R$','%']

    # essa parte foi mt complicada entao peguei um modelinho prono dos elementos do grafico
    figura = plt.Figure(figsize=(6.2, 3.5), dpi=60)
    ax = figura.add_subplot(111)
    ax.bar(lista_nomes, lista_valores,  color=cor_1, width=0.5)
    c = 0
    for i in ax.patches:
        if c==2:
            ax.text(i.get_x()-.001, i.get_height()+.5,str("{:,.0f}".format(lista_valores[c])+simbolos[c]), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        else:
            ax.text(i.get_x()-.001, i.get_height()+.5,str(simbolos[c]+"{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1
    ax.set_xticklabels(lista_nomes,fontsize=12)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_chart)
    canva.get_tk_widget().place(x=10, y=50)

grafico_bar()


# funcao para mostrar os dados 
def mostrar():   
    
    lista_dados = ['Nome do produto','Preço de Compra($)',  'Preço de Venda(R$)','Qtd','Custos Adicionais(R$)','Custo Médio de Frete(R$)','Custo total','Lucro Líquido(R$)','Margem de Lucro (%)']

    df_list = obter_dados_excel("dados.xlsx")
    
    global tree
    
    tree = ttk.Treeview(frame_tabela, selectmode="extended",columns=lista_dados, show="headings")
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["nw","center","center","center","center","center","center","center","center"]
    h=[150,120,110,40,130,150,80,110,130]
    n=0

    for col in lista_dados:
        tree.heading(col, text=col.title(), anchor=NW)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in df_list:
        tree.insert('', 'end', values=item)

mostrar()

janela.mainloop ()

#este foi o codigo para adicionar a interfacie para minha calculadora de lucros. - 
#Calebe Emanoel Santos Rabelo