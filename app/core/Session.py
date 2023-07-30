class Session:
    '''
        Este Singleton se lo usara como memoria volatil en donde se almacenará la sesion del usuario
        mientras la aplicacion esta viva
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.session = None
        return cls._instance

    def set_session(self, userSession):
        self.session = userSession

    def get_session(self):
        return self.session


class UserSession:
    def __init__(self, id, name, last_name, username, is_admin):
        self.name = name,
        self.id = id,
        self.username = username
        self.last_name = last_name
        self.is_admin = is_admin
