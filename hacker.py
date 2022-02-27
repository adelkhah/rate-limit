import requests


url = "http://localhost:8080/login"
body = {"username" : "username",
        "password" : "password"}
res = requests.post(url=url, json=body)
print(res.status_code)
body["username"] = "mohammad"
res = requests.post(url=url, json=body)
print(res.status_code)
body["username"] = "ali1"
res = requests.post(url=url, json=body)
print(res.status_code)
body["username"] = "ali3"
res = requests.post(url=url, json=body)
print(res.status_code)
