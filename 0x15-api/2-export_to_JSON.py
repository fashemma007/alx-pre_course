#!/usr/bin/python3
"""Gets employee details"""

import json
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
    json_dict = {}

    for todo in user_todo:
        # === writing list of dicts to csv ===
        user_dict = {}
        user_dict['task'] = todo.get("title")
        user_dict['completed'] = todo.get("completed")
        user_dict['username'] = user_dits.get("username")
        todos.append(user_dict)
    json_dict[argv[1]] = todos

    file = "{}.json".format(argv[1])
    with open(file, mode="w", newline='') as f:  # open json file
        # === writing to json ===
        json.dump(json_dict, f)
