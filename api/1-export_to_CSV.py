#!/usr/bin/python3
"""
Script that exports TODO list data for a given employee ID into a CSV file.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command-line arguments
    user_id = sys.argv[1]
    
    # Base URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user details (specifically targeting the 'username')
    user_response = requests.get(f"{url}users/{user_id}").json()
    username = user_response.get("username")
    
    # Fetch all tasks belonging to this user
    todos_response = requests.get(f"{url}todos", params={"userId": user_id}).json()
    
    # Define the output file name (e.g., 2.csv)
    filename = f"{user_id}.csv"
    
    # Write data to the CSV file with mandatory double quotes around all fields
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        # csv.QUOTE_ALL ensures every single field is enclosed in ""
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        for task in todos_response:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
