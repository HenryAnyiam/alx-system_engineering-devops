#!/usr/bin/python3
"""module to get employee information from REST API"""
from requests import get
from sys import argv


if __name__ == "__main__":
    details = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    tasks = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    data = tasks.json()
    info = details.json()
    total = len(data)
    completed = 0
    complete = []
    for i in data:
        if i.get('completed') is True:
            completed += 1
            complete.append(i)
    print(f"Employee {info.get('name')} is done with"
          f" tasks({completed}/{total})")
    for i in complete:
        print(f"     {i.get('title')}")
