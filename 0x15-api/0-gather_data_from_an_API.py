#!/usr/bin/python3

import requests
import sys

def gather_data_from_api(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    
    if response.status_code == 200:
        todos = response.json()
        
        if todos:
            employee_name = todos[0].get('username', 'Unknown')
            completed_tasks = [task for task in todos if task['completed']]
            total_tasks = len(todos)
            
            print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t{task['title']}")
        else:
            print("No tasks found for this employee.")
    else:
        print("Failed to retrieve data from the API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        gather_data_from_api(employee_id)
