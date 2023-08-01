from services.parametrics_service import parametric_service
from core.Session import Session


def get_links_users():
    user_session = Session().get_session()
    links = parametric_service.get_links()
    if user_session.is_admin:
        return links
    else:
        return [link for link in links if not link[3]]
