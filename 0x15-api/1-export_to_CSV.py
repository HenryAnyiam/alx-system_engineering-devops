#!/usr/bin/python3
"""module to get employee information from REST API"""
from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    details = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    tasks = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    data = tasks.json()
    info = details.json()
    name = info.get('username')
    full = []
    user_id = str(argv[1])
    for i in data:
        full.append([user_id, name, str(i.get('completed')), i.get('title')])
    with open(f"{user_id}.csv", 'w', encoding='UTF-8') as my_file:
        obj = csv.writer(my_file)
        obj.writerows(full)
