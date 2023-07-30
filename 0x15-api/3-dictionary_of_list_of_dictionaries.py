#!/usr/bin/python3
"""fun"""
import csv
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    users = requests.get(url + "/users").json()
    store_json={}
    with open("todo_all_employees.json", "w") as file:
        for user in users:
            store = []
            todos = requests.get(url + "/todos", params = {"userId": user.get("id")}).json()
            for dict_ in todos:
                store.append({"username": user.get("username"), "task": dict_.get("title"), "completed": dict_.get("completed")})
            store_json[user.get("id")] = store
        json.dump(store_json, file)
