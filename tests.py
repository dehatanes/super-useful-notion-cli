from sunc import NotionClient


client = NotionClient('')
print(client.users.list_all().json)