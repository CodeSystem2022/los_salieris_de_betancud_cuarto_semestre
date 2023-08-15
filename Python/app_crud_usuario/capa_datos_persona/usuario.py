class Usuario:

    def __init__(self, id_usuario: int = None, username: str = None, password: str = None) -> None:
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
    
    def __str__(self) -> str:
        return f'Usuario {self.id_usuario}: {self.username}'
    
    @property
    def id_usuario(self) -> int:
        return self._id_usuario
    
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def password(self) -> str:
        return self._password
    
    @id_usuario.setter
    def id_usuario(self, id_usuario: int) -> None:
        self._id_usuario = id_usuario
    
    @username.setter
    def username(self, username: str) -> None:
        self._username = username
    @password.setter
    def password(self, password: str) -> None:
        self._password = password