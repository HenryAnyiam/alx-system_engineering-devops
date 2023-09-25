#!/usr/bin/python3
"""module to get employee information from REST API"""
from requests import get
from sys import argv
import json


if __name__ == "__main__":
    details = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    tasks = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    data = tasks.json()
    info = details.json()
    name = info.get('username')
    full = []
    user_id = str(argv[1])
    for i in data:
        full.append({"task": i.get("title"),
                     "completed": str(i.get('completed')),
                     "username": name})
    user = {user_id: full}
    with open(f"{user_id}.json", 'w', encoding='UTF-8') as my_file:
        json.dump(user, my_file)
