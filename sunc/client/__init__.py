from sunc.settings import DEFAULT_NOTION_VERSION

from sunc.request import Request

from sunc.client.databases import NotionDatabaseClient
from sunc.client.pages import NotionPageClient
from sunc.client.blocks import NotionBlockClient
from sunc.client.search import NotionSearchClient
from sunc.client.users import NotionUserClient


class NotionClient:
    def __init__(self, notion_access_token, notion_version=DEFAULT_NOTION_VERSION):
        self.__notion_acces_token = notion_access_token
        self.__session = Request(headers={
            'Notion-Version': notion_version,
            'Authorization': 'Bearer %s' % (self.__notion_acces_token),
        })

        self.databases = NotionDatabaseClient(self.__session)
        self.pages = NotionPageClient(self.__session)
        self.blocks = NotionBlockClient(self.__session)
        self.search = NotionSearchClient(self.__session)
        self.users = NotionUserClient(self.__session)
