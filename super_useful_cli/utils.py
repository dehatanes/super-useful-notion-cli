from datetime import date
import json


def get_formatted_date_for_today(formatter):
    today = date.today()
    return today.strftime(formatter)


def beauty_print(content):
    print(json.dumps(content, sort_keys=True, indent=4))
