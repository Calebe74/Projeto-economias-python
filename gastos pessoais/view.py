import sqlite3 as lite

#fazendo conexões
con = lite.connect('dados.db')




#inserindo categorias
def inserir_categorias(i):


    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute ( query,i  )

def inserir_receita(i):

#inserindo tabela receitas
    with con:
        cur = con.cursor()
        query = "INSERT INTO receitas (categoria, adicionado_em,valor) VALUES (?,?,?)"
        cur.execute ( query,i  )

def inserir_receita(i):

#inserindo tabela gastos
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute ( query,i  )


#funções de inserção----------------------------------------

#deletar receitas
def deletar_receitas(i):


    with con:
        cur = con.cursor()
        query = "DELETE FROM receitas Where ID=?"
        cur.execute( query, i)

#deletar gastos

def deletar_gastos(i):


    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos Where ID=?"
        cur.execute( query, i)

#funcoes para ver dados ----------------------------------------

#ver categorias
def ver_categorias():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT *FROM categoria")
        linha = cur.fetchall()
        for l in linha : 
            lista_itens.append(l)

    return lista_itens

print(ver_categorias())


#ver receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT *FROM receitas")
        linha = cur.fetchall()
        for l in linha : 
            lista_itens.append(l)

    return lista_itens




#ver gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT *FROM gastos")
        linha = cur.fetchall()
        for l in linha : 
            lista_itens.append(l)

    return lista_itens

