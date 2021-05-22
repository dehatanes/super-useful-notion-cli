from collections import namedtuple
import os

SessionScope = namedtuple('NotionScope', ['database_id', 'page_template'])
session_scope = SessionScope(
    database_id=os.environ.get("NOTION_DATABASE_ID"),
    page_template=os.environ.get("NOTION_TEMPLATE_PAGE_ID"),
)
