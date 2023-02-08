#!/usr/bin/python3
"""Gets all employees todo details"""

import json
from requests import get
from sys import argv


if __name__ == "__main__":
    site_url = "https://jsonplaceholder.typicode.com"
    # get user's info such as name
    users_url = site_url + "/users"
    user_dits = get(users_url).json()
    # print(user_dits)
    todos = []
    json_dict = {}
    for user in user_dits:
        user_id = user.get('id')
        # get user's todos
        todos_url = site_url + "/user/{}/todos".format(user_id)
        user_todo = get(todos_url).json()
        for todo in user_todo:
            # === writing list of dicts to csv ===
            user_dict = {}
            user_dict['username'] = user.get("username")
            user_dict['task'] = todo.get("title")
            user_dict['completed'] = todo.get("completed")
            todos.append(user_dict)
        json_dict[user_id] = todos

    file = "todo_all_employees.json"
    with open(file, mode="w", newline='') as f:  # open json file
        # === writing to json ===
        json.dump(json_dict, f)
