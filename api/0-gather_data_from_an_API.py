#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])



    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

 
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    

    done_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

