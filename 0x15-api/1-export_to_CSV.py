#!/usr/bin/python3

import csv
import requests
import sys

def export_to_csv(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        file_name = f"{employee_id}.csv"

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos:
                user_id = task.get('userId', 'Unknown')
                username = task.get('username', 'Unknown')
                completed = task.get('completed', 'Unknown')
                title = task.get('title', 'Unknown')
                writer.writerow([user_id, username, completed, title])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
