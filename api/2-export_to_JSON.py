#!/usr/bin/python3
"""
Script that exports TODO list data for a given employee ID into a JSON file.
"""
import json
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
    
    # Structure the data according to the required format
    tasks_list = []
    for task in todos_response:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    
    # Final dictionary containing the user_id as the primary key
    json_data = {user_id: tasks_list}
    
    # Define the output file name (e.g., 2.json)
    filename = f"{user_id}.json"
    
    # Write the formatted data into the JSON file
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)
