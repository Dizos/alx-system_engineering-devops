#!/usr/bin/python3
"""
Script to export employee's TODO list to CSV format.
"""
import csv
import requests
import sys

def export_employee_tasks_to_csv(employee_id):
    """
    Export all tasks for a given employee to CSV.
    
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
    
    # Prepare CSV filename
    filename = f"{employee_id}.csv"
    
    # Write tasks to CSV
    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write all tasks
        for task in todos_data:
            csv_writer.writerow([
                user_data['id'], 
                user_data['username'], 
                task['completed'], 
                task['title']
            ])

def main():
    """Main function to handle script execution."""
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_employee_tasks_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

if __name__ == "__main__":
    main()
