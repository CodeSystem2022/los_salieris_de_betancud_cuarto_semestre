from capa_datos_persona.conexion import Conexion
from capa_datos_persona.cursor_del_pool import CursorDelPool
from capa_datos_persona.persona import Persona
from capa_datos_persona.logger_base import log


class PersonaDAO:
    """ Data Access Object """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'


    @classmethod
    def seleccionar(cls) -> list:
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona: Persona) -> int:
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona: Persona) -> int:
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona: Persona) -> int:
        with CursorDelPool() as cursor:
            valores = (persona.id, )
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    persona = Persona(nombre='Mateo', apellido='Torres', email='mtorres@email.com')
    personas_insertadas = PersonaDAO.insertar(persona)
    log.debug(f'Personas insertadas {personas_insertadas}')

    persona = Persona(nombre='Juan', apellido='Pena', email='jpena@email.com', id_persona=1)
    personas_actualizadas = PersonaDAO.actualizar(persona)
    log.debug(f'Personas insertadas {personas_actualizadas}')

    persona = Persona(id_persona=28)
    personas_eliminadas = PersonaDAO.eliminar(persona)
    log.debug(f'Personas eliminadas {personas_eliminadas}')

    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)