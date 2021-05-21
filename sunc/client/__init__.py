from sunc.settings import DEFAULT_NOTION_VERSION, DEFAULT_NOTION_API_HOST

from sunc.request import Request

from sunc.client.databases import NotionDatabaseClient
from sunc.client.pages import NotionPageClient
from sunc.client.blocks import NotionBlockClient
from sunc.client.search import NotionSearchClient
from sunc.client.users import NotionUserClient


class NotionClient:
    def __init__(self, notion_access_token, notion_api_host=DEFAULT_NOTION_API_HOST, notion_version=DEFAULT_NOTION_VERSION):
        self.__session = Request(
            notion_api_host,
            headers={
                'Notion-Version': notion_version,
                'Authorization': 'Bearer %s' % (notion_access_token),
            }
        )

        self.databases = NotionDatabaseClient(self.__session)
        self.pages = NotionPageClient(self.__session)
        self.blocks = NotionBlockClient(self.__session)
        self.search = NotionSearchClient(self.__session)
        self.users = NotionUserClient(self.__session)
