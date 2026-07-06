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
    fazer_login
) 

def main():
    criar_tabelas ()
    
    usuario = fazer_login("Gustavo", "anglo2026")

    print("======================")
    if usuario:
        print("login realizado com sucesso")
    else:
        print("Usuario ou senha invalidos")
    print("======================")

    print("======================")
    print("sistema iniciado com sucesso!")
    print("======================")
if __name__ == "__main__":
    main()
