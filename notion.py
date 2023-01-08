import requests, json
#https://api.notion.com/v1/databases/{database_id}

token = '#'
databaseId = '#'
headers = {
    "Authorization":"Bearer " + token,
    "Notion-Version":"2022-06-28"
}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
    result = requests.request("POST", readUrl, headers=headers)
    print(result.status_code)
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(result.json(), f, ensure_ascii=False)
    pass

def createPage():
    pass

def updatePage():
    pass

readDatabase(databaseId, headers)