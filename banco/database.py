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
    
## tabela chamado

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                colegio_id INTEGER NOT NULL,
                tecnico_id INTEGER NOT NULL,

                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,

                equipamento_id INTEGER,

                status TEXT NOT NULL,
                prioridade TEXT NOT NULL,

                solucao TEXT,

                aberto_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                encerrado_em TIMESTAMP,

                FOREIGN KEY (colegio_id) REFERENCES colegios(id),
                FOREIGN KEY (tecnico_id) REFERENCES usuario(id)
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

## cadastrar chamado

def cadastrar_chamado(
        colegio_id, tecnico_id, titulo, descricao, equipamento_id, status, prioridade
        ):
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO chamados (
                colegio_id, tecnico_id, titulo, descricao, equipamento_id, status, prioridade
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (colegio_id, tecnico_id, titulo, descricao, equipamento_id, status, prioridade)
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

## listar chamados

def listar_chamados():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM chamados")

    chamados = cursor.fetchall()

    conexao.close

    return chamados

## listar chamados por status

def listar_chamados_por_status(status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM chamados WHERE status = ?""", (status,) )

    chamados = cursor.fetchall()

    conexao.close

    return chamados

## listar chamados por colegio

def listar_chamados_por_colegio(colegio_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM chamados WHERE colegio_id = ?""", (colegio_id,) )

    chamados = cursor.fetchall()

    conexao.close

    return chamados

## listar chamados por tecnico

def listar_chamados_por_tecnico(tecnico_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM chamados WHERE tecnico_id = ?""", (tecnico_id,) )

    chamados = cursor.fetchall()

    conexao.close

    return chamados

## listar colegios do usuario

def listar_colegios_do_usuario(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT colegios.* FROM colegios JOIN usuarios_colegios 
            ON colegios.id = usuarios_colegios.colegio_id 
            WHERE usuarios_colegios.usuario_id = ?
            AND usuarios_colegios.ativo = 1
""", (usuario_id,)
        )
    
    colegios = cursor.fetchall()

    conexao.close

    return colegios

## buscar chamado

def buscar_chamado_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute ("""SELECT * FROM chamados WHERE id = ? 
""", (id,)
        )
    
    chamado = cursor.fetchone()

    conexao.close
    return chamado

## buscar usuario por id

def buscar_usuario_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute ("""SELECT * FROM usuarios WHERE id = ? 
""", (id,)
        )
    
    usuarios = cursor.fetchone()

    conexao.close
    return usuarios

## buscar colegio por id

def buscar_colegio_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute ("""SELECT * FROM colegios WHERE id = ? 
""", (id,)
        )
    
    colegios = cursor.fetchone()

    conexao.close
    return colegios

## alterar status

def alterar_status(id, status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute ("""UPDATE chamados SET status = ? WHERE id = ?
""", (status, id)
        )

    conexao.commit()
    conexao.close()
    
    ## alterar solucao

def alterar_solucao(id, solucao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute ("""UPDATE chamados SET 
                solucao = ? 
                WHERE id = ?
""", (solucao, id)
        )

    conexao.commit()
    conexao.close()

## encerrar chamado

def encerrar_chamado(id,solucao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute ("""UPDATE chamados SET
                status = ?,
                solucao = ?,
                encerrado_em = CURRENT_TIMESTAMP WHERE id = ? 
""", ("resolvido", solucao, id)
        )
    
    conexao.commit()
    conexao.close()

def fazer_login(nome, senha):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute ("""SELECT * FROM usuarios WHERE 
                        nome = ?
                        AND senha = ?
                        AND ativo = 1
""", (nome, senha)
        )
        
        usuario = cursor.fetchone()

        conexao.close() 

        return usuario