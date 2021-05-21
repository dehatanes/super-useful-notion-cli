from sunc.request import Request


# STILL MAKING TESTS
request = Request(headers={
    'Authorization': '<YOUR_API_KEY>',
})
"""
response = request.get('https://api.notion.com/v1/databases', params={'page_size': 10})
"""
response = request.post('https://api.notion.com/v1/pages', json={
    'parent': {
       'database_id': '642820bb-b4ae-4be4-a905-c99e2ad42e7d'
    },
    'properties': {
      'Name': {
        'title': [
          {
            'text': {
              'content': 'Tuscan Kale'
            },
          },
        ],
      },
    },
    'children': []
})
print(response.content)