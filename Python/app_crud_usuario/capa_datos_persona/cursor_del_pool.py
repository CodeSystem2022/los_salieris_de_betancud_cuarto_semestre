from capa_datos_persona.conexion import Conexion
from logger_base import log

class CursorDelPool():
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        log.debug('Inicio del método with y __enter__')
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, exc, value, detail):
        log.debug('Se ejecuta en método __exit__')
        if value:
            self._conexion.rollback()
            log.debug(f'Ocurrió un error: {value}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())