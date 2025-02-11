#!/usr/bin/python3
"""
Script to export data in JSON format.
Gets employee tasks from REST API and exports to JSON file.
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports employee task data to JSON file.
    Args:
        employee_id: ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        return
    
    user_data = user_response.json()
    username = user_data.get('username')
    
    # Get employee's tasks
    todos_response = requests.get(f"{base_url}/todos",
                                params={'userId': employee_id})
    if todos_response.status_code != 200:
        return
    
    todos_data = todos_response.json()
    
    # Format tasks according to requirements
    tasks_list = []
    for todo in todos_data:
        task_dict = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        tasks_list.append(task_dict)
    
    # Create JSON object with required format
    json_data = {str(employee_id): tasks_list}
    
    # Export to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
