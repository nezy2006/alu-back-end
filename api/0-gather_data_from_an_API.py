#!/usr/bin/python3
import requests
import sys

def gather_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        print(f"Error fetching user {employee_id}")
        return
    user_data = user_resp.json()
    employee_name = user_data.get("name")
    todos_resp = requests.get(todos_url)
    if todos_resp.status_code != 200:
        print(f"Error fetching TODOs for user {employee_id}")
        return
    todos = todos_resp.json()

    completed_tasks = [task for task in todos if task.get("completed") is True]
    total_tasks = len(todos)
    num_done = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    gather_data(emp_id)

