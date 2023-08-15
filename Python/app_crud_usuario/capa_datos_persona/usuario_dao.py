from capa_datos_persona.cursor_del_pool import CursorDelPool
from capa_datos_persona.usuario import Usuario
from capa_datos_persona.logger_base import log


class UsuarioDAO:
    """ Data Access Object """

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls) -> list[Usuario]:
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario: Usuario) -> int:
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario: Usuario) -> int:
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario: Usuario) -> int:
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario, )
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # usuario = Usuario(username='mtorres', password='123')
    # usuarios_insertados = UsuarioDAO.insertar(usuario)
    # log.debug(f'Usuarios insertados {usuarios_insertados}')

    # usuario = Usuario(username='jpena', password='222', id_usuario=1)
    # usuarios_actualizados = UsuarioDAO.actualizar(usuario)
    # log.debug(f'Usuarios insertados {usuarios_actualizados}')

    # usuario = Usuario(id_usuario=4)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario)
    # log.debug(f'Usuarios eliminados {usuarios_eliminados}')

    personas = UsuarioDAO.seleccionar()
    for usuario in personas:
        log.debug(usuario)