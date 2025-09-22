import json

with open('raw.json', 'r') as f:
    raw = json.load(f)

recipes: dict = raw['recipe']
technologies: dict = raw['technology']