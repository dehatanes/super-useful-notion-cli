import os
import json
import tempfile
from subprocess import call

from PyInquirer import prompt
from .utils import get_formatted_date_for_today


def get_custom_prop_preference(prop_name: str, prop: dict):
    prop_type = prop['type']
    if prop_type == "title":
        resp = _ask_for_the_title(prop_name)
        return [{"text": {"content": resp}}]
    elif prop_type == "date":
        resp = _ask_for_date(prop_name)
        return {"start": resp}
    elif prop_type == "multi_select":
        resp = _ask_for_multi_select(prop_name, prop)
        return [{"name": chosen_tag} for chosen_tag in resp]
    elif prop_type == "select":
        resp = _ask_for_select(prop_name, prop)
        return {"name": resp}
    # todo -> add support to other types of props


def get_custom_page_content(raw_content: list) -> list:
    should_customize_page = _ask_if_should_customize_page_content()

    if not should_customize_page:
        return raw_content

    return _customize_content(raw_content)


def _ask_for_the_title(prop_name: str) -> str:
    date = get_formatted_date_for_today(formatter="%d.%m.%Y")
    default_title = f'[{date}] ATA'
    question = {
        'type': 'input',
        'name': 'title',
        'message': prop_name,
        'default': default_title,
    }
    answer = prompt(question)
    return answer['title']


def _ask_for_date(prop_name: str) -> str:
    today = get_formatted_date_for_today(formatter="%Y-%m-%d")
    question = {
        'type': 'input',
        'name': 'date',
        'message': prop_name,
        'default': today
    }
    answer = prompt(question)
    return answer['date']


def _ask_for_multi_select(prop_name: str, prop: dict) -> list:
    options = prop["multi_select"]["options"]
    question = {
        'type': 'checkbox',
        'name': 'multi_select',
        'message': prop_name,
        'choices': [{'name': choice['name']} for choice in options]
    }
    answer = prompt(question)
    return answer['multi_select']


def _ask_for_select(prop_name: str, prop: dict) -> str:
    options = prop["select"]["options"]
    question = {
        'type': 'list',
        'name': 'selector',
        'message': prop_name,
        'choices': [choice['name'] for choice in options]
    }
    answer = prompt(question)
    return answer['selector']


def _ask_if_should_customize_page_content() -> bool:
    positive_answer = 'Sim (abrirei um editor de texto padrão para você realizar a edição)'
    negative_answer = 'Não (segue o baile)'
    question = {
        'type': 'list',
        'name': "choice",
        'message': "Deseja editar o conteúdo padrão da ata?",
        'choices': [positive_answer, negative_answer]
    }
    answer = prompt(question).get("choice")
    return answer == positive_answer


def _customize_content(raw_content: list) -> list:
    default_content = _page_content_to_text(raw_content)

    editor_name = os.environ.get('EDITOR', 'vim')
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(str.encode(default_content))
        tf.flush()
        call([editor_name, tf.name])
        temp_file_name = tf.name
        edited_text = open(temp_file_name).read()
        return _text_to_page_content(edited_text)


def _page_content_to_text(page_content: list) -> str:
    return json.dumps(page_content, sort_keys=True, indent=4)


def _text_to_page_content(customized_content_text: str) -> list:
    return json.loads(customized_content_text)
