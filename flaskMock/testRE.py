import requests

url = "http://127.0.0.1:5000/pay"

querystring = {"user_id":"4444","price":"12"}

payload = ""
headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "da4e1c9a-8794-45af-88d5-1d799c454b6a,5df7e366-1b4d-4f5b-b628-187d6dc0e583",
    'Host': "127.0.0.1:5000",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)