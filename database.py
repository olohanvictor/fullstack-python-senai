import sqlite3

def conectar():
    conn = sqlite3.connect("escola.db")
    return conn 


#Fazendo as funções do CRUD
def criar_tabela(): 

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL)              
    """)

    conn.commit() 
    conn.close() 

#CREATE: Criando a tabela alunos
def criar_aluno(nome, idade, nota):
    conn = conectar() #conecto
    cursor = conn.cursor() #crio o cursor

    cursor.execute("INSERT INTO alunos(nome, idade, nota) VALUES (?, ?, ?)", (nome, idade, nota))

    conn.commit() #commito o que eu fiz
    conn.close() #fecho a conexão


#READ: Procurando e exibindo alunos no banco de dados
def buscar_aluno(nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE nome = ?",
        (nome,)
    )

    alunos = cursor.fetchall()

    conn.close()
    return alunos

#UPDATE: Alterando informações dos alunos
def editar_aluno(id, nome, idade, nota):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE alunos
        SET nome = ?, idade = ?, nota = ?
        WHERE ID = ?
    """, (nome, idade, nota, id))

    conn.commit()
    conn.close()

#DELETE: SUMINDO com os alunos chatos pra cacete
def deletar_aluno(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alunos WHERE ID = ?", (id,))

    conn.commit()
    conn.close()