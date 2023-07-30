#!/usr/bin/python3
"""fun"""
import csv
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    user = requests.get(url + f"/users/{sys.argv[1]}").json()
    todos = requests.get(url + "/todos", params = {"userId": sys.argv[1]}).json()
    store = [] 
    with open(f"{sys.argv[1]}.json", "w") as file:
        for dict_ in todos:
            store.append({"task": dict_.get("title"), "completed": dict_.get("completed"), "username": user.get("username")})
        json.dump({sys.argv[1] : store}, file)
