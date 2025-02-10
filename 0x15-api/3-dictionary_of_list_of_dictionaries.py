#!/usr/bin/python3
"""
Script to export employee's TODO list to JSON format.
"""
import json
import requests
import sys

def export_employee_tasks_to_json(employee_id):
    """
    Export tasks for a specific employee to JSON.
    
    Args:
        employee_id (int): ID of the employee
    """
    # API base URL
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch user details
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch user's TODO list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Prepare JSON data
    json_data = {
        str(employee_id): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            } for task in todos_data
        ]
    }
    
    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(json_data, jsonfile)

def export_all_employees_tasks_to_json():
    """
    Export tasks for all employees to a single JSON file.
    """
    # API base URL
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch all users
    users_url = f'{base_url}/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()
    
    # Prepare comprehensive JSON data
    all_tasks_json = {}
    
    for user in users_data:
        # Fetch user's TODO list
        todos_url = f'{base_url}/todos?userId={user["id"]}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        
        # Add user's tasks to comprehensive JSON
        all_tasks_json[str(user['id'])] = [
            {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            } for task in todos_data
        ]
    
    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(all_tasks_json, jsonfile)

def main():
    """Main function to handle script execution."""
    if len(sys.argv) == 2:
        try:
            employee_id = int(sys.argv[1])
            export_employee_tasks_to_json(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
            sys.exit(1)
    elif len(sys.argv) == 1:
        export_all_employees_tasks_to_json()
    else:
        print("Usage: python3 script.py [employee_id]")
        sys.exit(1)

if __name__ == "__main__":
    main()
