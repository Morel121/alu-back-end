#!/usr/bin/python3
"""
Script qui utilise une API REST pour un ID d'employé donné,
afin de renvoyer des informations sur la progression de sa TODO list.
"""
import requests
import sys

if __name__ == "__main__":
    # 1. Récupérer l'ID de l'employé depuis les arguments de la ligne de commande
    user_id = sys.argv[1]
    
    # URL de base de l'API
    url = "https://jsonplaceholder.typicode.com/"
    
    # 2. Requête pour obtenir les infos de l'utilisateur (le nom)
    user_response = requests.get(f"{url}users/{user_id}").json()
    employee_name = user_response.get("name")
    
    # 3. Requête pour obtenir toutes les tâches de cet utilisateur
    todos_response = requests.get(f"{url}todos", params={"userId": user_id}).json()
    
    # 4. Filtrer et compter les tâches
    total_tasks = len(todos_response)
    # Récupérer uniquement les titres des tâches terminées (completed == True)
    completed_tasks = [task.get("title") for task in todos_response if task.get("completed") is True]
    
    # 5. Afficher le résultat au format exact demandé
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    
    for title in completed_tasks:
        print(f"\t {title}")
