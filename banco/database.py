import sqlite3

def conectar():
    conexao = sqlite3.connect("banco/chamados.db")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                classe TEXT NOT NULL,
                ativo INTEGER DEFAULT 1
            )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colegios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cor_tema TEXT NOT NULL,
                logo TEXT,
                observacoes TEXT,
                ativo INTEGER DEFAULT 1,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    
    conexao.commit()
    conexao.close()

def cadastrar_usuario(nome, senha, classe):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, senha, classe) VALUES (?, ?, ?)
    """, (nome, senha, classe))
    
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    conexao.close()
    
    return usuarios

