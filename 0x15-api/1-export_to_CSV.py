#!/usr/bin/python3
"""fun"""
import csv
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    user = requests.get(url + f"/users/{sys.argv[1]}").json()
    todos = requests.get(url + "/todos", params = {"userId": sys.argv[1]}).json()
    
    with open(f"{sys.argv[1]}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for dict_ in todos:
            print(dict_)
            writer.writerow([sys.argv[1], user.get("username"), dict_.get('completed'), dict_.get("title")])
