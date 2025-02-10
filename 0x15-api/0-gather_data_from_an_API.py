#!/usr/bin/python3
"""
Script to retrieve and display an employee's TODO list progress from an API.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetch and display employee's TODO list progress.
    
    Args:
        employee_id (int): ID of the employee
    """
    # API base URL
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch user details
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch user's todo list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Calculate completed tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    
    # Print progress summary
    print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    
    # Print completed task titles
    for task in completed_tasks:
        print(f"\t {task['title']}")

def main():
    """Main function to handle script execution."""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

if __name__ == "__main__":
    main()
