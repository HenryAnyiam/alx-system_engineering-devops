#!/usr/bin/python3
"""module to get employee information from REST API"""
from requests import get
from sys import argv
import json


if __name__ == "__main__":
    for num in range(1, 11):
        details = get(f"https://jsonplaceholder.typicode.com/users/{num}")
        tasks = get(f"https://jsonplaceholder.typicode.com/users/{num}/todos")
        data = tasks.json()
        info = details.json()
        name = info.get('username')
        full = []
        user_id = str(num)
        for i in data:
            full.append({"task": i.get("title"),
                         "completed": str(i.get('completed')),
                         "username": name})
        user = {user_id: full}
        with open("todo_all_employees.json", 'a+', encoding='UTF-8') as my_f:
            json.dump(user, my_f)
