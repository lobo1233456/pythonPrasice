import requests

url = "http://localhost:12306/login"

payload = "{\"username\":\"admin\",\"password\":\"admin\",\"roleID\":22}"
headers = {
    'content-length': "63",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "cfa68e15-2ef9-4b21-8f2f-3455c38836d9"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
