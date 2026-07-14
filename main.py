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

## fazer login 

def iniciar_sistema():
    nome = input("usuario: ")
    senha = input("senha: ")
    
    usuario = fazer_login(nome, senha)
    if usuario:
        print("login realizado com sucesso")

        colegio = selecionar_colegio(usuario)
        if colegio:
            menu_principal(usuario, colegio)
    else:
        print("Usuario ou senha invalidos")
    
print("sistema iniciado com sucesso!")
print("=============================")

## escolher colegio

def selecionar_colegio(usuario):
    colegios = listar_colegios_do_usuario(usuario[0])

    if len(colegios) == 0:
        print("Este usuario nao tem colegios cadastrado.")
        return None
    
    while True:
        print("\n=============================")
        print("       selecione o colegio")
        print("===============================")

        for i, colegio in enumerate(colegios, start=1):
            print(f"{i} - {colegio[1]}")

        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
                return None
            
        if opcao.isdigit():
                opcao = int(opcao)

                if 1 <= opcao <= len(colegios):
                    return colegios[opcao - 1]
                print("\nOpção invalida. Tente novamente.")

## menu principal

def menu_principal(usuario, colegio):
    while True:
        print("=====================================")
        print(" Sistema de Chamados")
        print("=======================================")

        print(f"Tecnico: {usuario[1]}")
        print(f"Colegio: {colegio[1]}")
        print()
        print("1 - Abrir chamado")
        print("2 - Chamados abertos")
        print("3 - Listar chamado")
        print("4 - Buscar chamado")
        print("5 - Trocar de usuario")
        print("6 - Chamados encerrados")
        print("7 - Relatorios")
        print("8 - Configuração")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção:")
        
        if opcao == "1":
            print(abrir_chamado(usuario, colegio))

        elif opcao == "2":
             print("Chamados abertos")

        elif opcao == "3":
             print("Lista de chamados")

        elif opcao == "4":
             return
        
        elif opcao == "5":
             print("Escolha o usuario")

        elif opcao == "6":
             print("Chamados encerrados")

        elif opcao == "7":
             print("opções de relatorios")

        elif opcao == "8":
             print("Configurações")
        
        elif opcao == "0":
             exit()

        else:
             print("\nOpção invalida")

## abrir chamado

def abrir_chamado(usuario, colegio):
    titulo = input("Titudo do chamado: ")
    descricao = input("Descrição: ") 
    equipamento = input("Qual equipamento: ")
    status = input("Status:")
    prioridade = input("Prioridade: ")
     
    cadastrar_chamado(
        colegio[0],
        usuario[0], 
         titulo, descricao, equipamento, status, prioridade
        )
    
    print("Chamado cadastrado com sucesso!")

if __name__ == "__main__":
    main()
    iniciar_sistema()