#!/usr/bin/python3
"""Gets employee details"""

from csv import DictWriter, QUOTE_ALL
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    site_url = "https://jsonplaceholder.typicode.com"
    # get user's todos
    todos_url = site_url + "/user/{}/todos".format(argv[1])
    user_todo = get(todos_url).json()
    # get user's info such as name
    user_url = site_url + "/users/{}".format(argv[1])
    user_dits = get(user_url).json()

    todos = []
    todo_list = []
    hdr_name = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    for todo in user_todo:
        # === writing list of dicts to csv ===
        todo_dict = {}
        todo_dict['USER_ID'] = argv[1]
        todo_dict['USERNAME'] = user_dits.get("name")
        todo_dict['TASK_COMPLETED_STATUS'] = todo.get("completed")
        todo_dict['TASK_TITLE'] = todo.get("title")
        todos.append(todo_dict)

        # === writing nested lists to csv ===
        # tudus = []
        # tudus.append(argv[1])
        # tudus.append(user_dits.get("name"))
        # tudus.append(todo.get("completed"))
        # tudus.append(todo.get("title"))
        # todo_list.append(tudus)

    file = "{}.csv".format(argv[1])
    with open(file, mode="w", newline='') as f:  # open csv file
        # === writing list of dicts to csv ===
        writer = DictWriter(f, fieldnames=hdr_name, quoting=QUOTE_ALL)
        writer.writerows(todos)

        # === writing nested lists to csv ===
        # writer = csv.writer(f, delimiter=',', quoting=QUOTE_ALL)
        # writer.writerows(todo_list)
