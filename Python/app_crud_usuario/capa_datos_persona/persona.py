from logger_base import log


class Persona:
    def __init__(self, id_persona: int = None, nombre: str = None, apellido: str = None, email: str = None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
    
    def __str__(self) -> str:
        return f"""
            Id persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
        """
    
    @property
    def id(self) -> int:
        return self._id_persona
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def apellido(self) -> str:
        return self._apellido
    
    @property
    def email(self) -> str:
        return self._email
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido: str) -> None:
        self._apellido = apellido
    
    @email.setter
    def email(self, email: str) -> None:
        self._email = email



if __name__ == '__main__':
    persona_1 = Persona(1, 'Juan', 'Perez', 'jperez@email.com')
    log.debug(persona_1)
    persona_2 = Persona(nombre='Jose', apellido='Lepez', email='ljose@email.com')
    log.debug(persona_2)
    persona_1 = Persona(id_persona=1)
    log.debug(persona_1)