from banco.database import (
    criar_tabelas,
    cadastrar_usuario,
    listar_usuarios,
    cadastrar_colegio,
    listar_colegios,
    cadastrar_usuario_colegio
) 

def main():
    criar_tabelas ()
    cadastrar_usuario_colegio(1, 1)

    listar_colegios()
    lista = listar_colegios()
    
    print("======================")
    print(lista)
    print("======================")

    print("======================")
    print("sistema iniciado com sucesso!")
    print("======================")
if __name__ == "__main__":
    main()
