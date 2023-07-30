#!/usr/bin/python3
"""fun"""
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    user = requests.get(url + f"/users/{sys.argv[1]}").json()
    todos = requests.get(url + "/todos", params = {"userId": sys.argv[1]}).json()
    completed_tasks = [dict_.get("title") for dict_ in todos if dict_.get("completed") == True]
    print("Employee {} is done with tasks({}/{})".format(user.get("name"), 
            len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t{}".format(task))
