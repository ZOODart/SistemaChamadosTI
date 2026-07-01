from banco.database import (
    criar_tabelas,
    cadastrar_usuario,
    listar_usuarios
) 

def main():
    criar_tabelas ()
    
    print("sistema iniciado com sucesso!")

if __name__ == "__main__":
    main()
