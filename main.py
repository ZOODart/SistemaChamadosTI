from banco.database import (
    criar_tabelas,
    cadastrar_usuario,
    listar_usuarios,
    cadastrar_colegio,
    listar_colegios,
    cadastrar_usuario_colegio,
    cadastrar_chamado,
    listar_chamados,
    buscar_chamado_por_id,
    alterar_status,
    alterar_solucao,
    encerrar_chamado,
    listar_chamados_por_status,
    listar_chamados_por_colegio,
    listar_chamados_por_tecnico,
    fazer_login,
    buscar_usuario_por_id,
    buscar_colegio_por_id,
    listar_colegios_do_usuario
) 

def main():
    criar_tabelas ()
    
def iniciar_sistema():
    nome = input("usuario: ")
    senha = input("senha: ")
    
    usuario = fazer_login(nome, senha)
    if usuario:
        print("login realizado com sucesso")
    else:
        print("Usuario ou senha invalidos")
    
print("sistema iniciado com sucesso!")
print("======================")

if __name__ == "__main__":
    main()
    iniciar_sistema()