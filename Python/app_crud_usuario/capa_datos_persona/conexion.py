import sys
from psycopg2 import pool
from capa_datos_persona.logger_base import log

class Conexion:
    _DB_NAME = 'UTN_laboratorioIV'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = '5432'
    _DB_HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def obtener_pool(cls):
        if cls._pool is not None:
            return cls._pool
        try:
            cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                    cls._MAX_CON,
                                                    host=cls._DB_HOST,
                                                    port=cls._DB_PORT,
                                                    database=cls._DB_NAME,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD)
            log.debug(f'Creación del pool exitosa {cls._pool}')
        except Exception as err:
            log.error(f'Ocurrió un error al crear el pool: {err}')
            sys.exit()
        return cls._pool
    
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresamos la conexión del pool: {conexion}')
    
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()


if __name__ == '__main__':
    conexion_1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion_1)
    conexion_2 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion_2)
    conexion_3 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion_3)
    conexion_4 = Conexion.obtener_conexion()
    conexion_5 = Conexion.obtener_conexion()
    conexion_6 = Conexion.obtener_conexion()