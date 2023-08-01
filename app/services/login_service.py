from core.Session import UserSession, Session
from repositories.user import UserRepository


def sign_in(username, password):
    user = UserRepository.get_user_by_username(username=username)
    # FIXME: Descomentar
    # if user.password == password:
    session = UserSession(id=user.id, name=user.name, last_name=user.last_name, username=username,
                              is_admin=user.is_admin)
    Session().set_session(session)
    return True
    # return False
