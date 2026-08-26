import json 
from pathlib import Path
from application import Application

def save_applications(applications, filename):
    data = [application.to_dict() for application in applications]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent = 4)

def load_applications(filename):
    if not Path(filename).exists():
        return []

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Application(**item) for item in data]