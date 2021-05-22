class NotionUserClient:
    def __init__(self, session):
        self.__session = session
        self.__paths = {
            'retrieve': '/users/{user_id}',
            'list_all': '/users'
        }

    def retrieve(self, user_id):
        path = self.__paths['retrieve_user'].format(user_id=user_id)
        return self.__session.get(path)

    def list_all(self, start_cursor=None, page_size=None):
        params = {}
        if start_cursor:
            params['start_cursor'] = start_cursor
        if page_size:
            params['page_size'] = page_size

        path = self.__paths['list_all']
        return self.__session.get(path, params=params)