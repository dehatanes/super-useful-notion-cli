from .interactive_cmd import get_custom_prop_preference, get_custom_page_content
from .session import session_scope
from .notion_adapter import (
    get_database_properties,
    get_page_content,
    create_new_page_in_db,
    add_content_in_page,
)


def main():
    print()
    print("SUPER USEFUL NOTION CLI - ATA GENERATOR 2000")
    print("--------------------------------------------")
    properties_schema = get_properties_schema()
    new_page_properties = generate_page_properties(properties_schema)
    new_page_id = create_page(new_page_properties)

    print()
    print("Aguarde um instante... criando página...")
    print()

    template_content = get_template_page_content()
    if template_content:
        page_content = get_custom_page_content(template_content)

        print()
        print("Aguarde um instante... adicionando conteúdo na página...")
        print()

        add_content(new_page_id, page_content)

    print('--------------------------------------------')
    print('Página criada com sucesso!')
    print(f'Você pode visitá-la aqui: https://www.notion.so/debstests/{"".join(new_page_id.split("-"))}')


def get_properties_schema() -> dict:
    resp = get_database_properties(session_scope.database_id)
    return resp.get('properties')


def get_template_page_content() -> list:
    page_template_id = session_scope.page_template
    if not page_template_id:
        return []

    children = get_page_content(page_template_id)
    for child in children:
        child.pop('created_time')
        child.pop('id')
        child.pop('last_edited_time')
    return children


def create_page(properties: dict) -> str:
    resp = create_new_page_in_db(properties, session_scope.database_id)
    return resp.get('id')


def add_content(page_id: str, content: list) -> dict:
    resp = add_content_in_page(page_id, content)
    return resp


def generate_page_properties(properties_schema: dict) -> dict:
    properties = {
        prop['id']: {prop['type']: get_custom_prop_preference(name, prop)}
        for name, prop in properties_schema.items()
    }
    return properties


main()
