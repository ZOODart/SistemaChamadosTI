import sqlite3

def conectar():
    conexao = sqlite3.connect("banco/chamados.db")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

## tabela usuario

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                classe TEXT NOT NULL,
                ativo INTEGER DEFAULT 1
            )
        """)
    
## tabela colegio

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
    
## tabela usuario colegio

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios_colegios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                colegio_id INTEGER NOT NULL,
                ativo INTEGER DEFAULT 1,

                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (colegio_id) REFERENCES colegios(id)
            )
        """)
    
    conexao.commit()
    conexao.close()

## cadastrar usuario

def cadastrar_usuario(nome, senha, classe):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, senha, classe) VALUES (?, ?, ?)
    """, (nome, senha, classe)
    )
    
    conexao.commit()
    conexao.close()

## cadastrar colegio

def cadastrar_colegio(nome, cor_tema, observacoes):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO colegios (nome, cor_tema, observacoes) VALUES (?, ?, ?)
    """, (nome, cor_tema, observacoes)
    )

    conexao.commit()
    conexao.close()

## cadastrar usuario no colegio

def cadastrar_usuario_colegio(usuario_id, colegio_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios_colegios (usuario_id, colegio_id) VALUES (?, ?)
    """,(usuario_id, colegio_id)
    )

    conexao.commit()
    conexao.close()

## listar usuarios

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    conexao.close()
    
    return usuarios

## listar colegio

def listar_colegios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM colegios")

    colegios = cursor.fetchall()

    conexao.close()
    
    return colegios

