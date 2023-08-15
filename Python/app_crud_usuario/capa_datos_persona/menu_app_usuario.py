import sys
from capa_datos_persona.usuario import Usuario
from capa_datos_persona.usuario_dao import UsuarioDAO


def show_menu() -> None:
    print('\nOpciones:')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Eliminar Usuario')
    print('5. Salir\n')


def main() -> None:
    while True:
        show_menu()
        option = int(input('Ingrese una opción (1-5): '))
        while option < 1 or option > 5:
            print('\nOpción inválida, vuelva a intentarlo')
            show_menu()
            option = int(input('Ingrese una opción (1-5): '))
        if option == 1:
            print(UsuarioDAO.seleccionar())
        elif option == 2:
            usuario = Usuario(
                username=input('Ingrese el nombre de usuario: '),
                password=input('Ingrese la contraseña: '),
            )
            UsuarioDAO.insertar(usuario)
            print('\nUsuario agregado exitosamente\n')
        elif option == 3:
            usuario = Usuario(
                username=input('Ingrese el nombre de usuario: '),
                password=input('Ingrese la contraseña: '),
                id_usuario=int(input('Ingrese el Id del usuario a modificar: ')),
            )
            UsuarioDAO.actualizar(usuario)
            print('\nUsuario actualizado exitosamente\n')
        elif option == 4:
            usuario = Usuario(id_usuario=int(input('Ingrese el Id del usuario a eliminar: ')))
            UsuarioDAO.eliminar(usuario)
            print('\nUsuario eliminado exitosamente\n')
        else:
            print('\nHasta luego\n')
            sys.exit(1)

if __name__ == '__main__':
    main()