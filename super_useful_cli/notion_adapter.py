import os
import requests

NOTION_API_TOKEN = os.environ.get("NOTION_API_KEY")
notion_api_base_path = 'https://api.notion.com/v1'
notion_api_version = '2021-05-13'


def get_database_properties(database_id: str) -> dict:
    endpoint = f"{notion_api_base_path}/databases/{database_id}"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
    }
    resp = requests.get(endpoint, headers=headers)
    # todo -> handle request errors
    return resp.json()


def get_page_content(page_id: str) -> list:
    endpoint = f"{notion_api_base_path}/blocks/{page_id}/children"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    resp = requests.get(endpoint, headers=headers)
    children = resp.json().get("results")
    # todo -> handle request errors
    return children


def create_new_page_in_db(page_properties: dict, database_id: str) -> dict:
    endpoint = f"{notion_api_base_path}/pages"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    body = {
        "parent": {"database_id": database_id},
        "properties": page_properties
    }
    resp = requests.post(endpoint, json=body, headers=headers)
    # todo -> handle request errors
    return resp.json()


def add_content_in_page(page_id: str, content: list) -> dict:
    endpoint = f"{notion_api_base_path}/blocks/{page_id}/children"
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Notion-Version': notion_api_version,
        'Content-Type': 'application/json',
    }
    body = {
        "children": content
    }
    resp = requests.patch(endpoint, json=body, headers=headers)
    # todo -> handle request errors
    return resp.json()


if __name__ == '__main__':
    # Just used to test requests in dev env
    from .utils import beauty_print
    from .session import session_scope
    response = get_database_properties(session_scope.database_id)
    beauty_print(response)
