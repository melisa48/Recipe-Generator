import json

def load_recipes(filename):
    with open(filename, 'r') as file:
        return json.load(file)
