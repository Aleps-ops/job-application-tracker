import json 
from pathlib import Path
from application import Application

def save_applications(applications, filename):
    data = [application.to_dict() for application in applications]
    with open(filename, "w") as file:
        json.dump(data, file, indent = 4)

def load_applications(filename):
    if not Path(filename).exists():
        return []

    with open(filename, "r") as file:
        data = json.load(file)

    return [Application(**item) for item in data]