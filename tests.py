from sunc import NotionClient


client = NotionClient('secret_KkvznlgdwRX9tTItyvX83VtWOp4jp6LiSQV0W5pBYfO')
print(client.users.list_all().json)