import json

def load_config(path) -> dict:
    with open(path, "r") as f:
        return json.loads(f.read())


def save_config(path):
    with open(path, "w") as f:
        pass


store = lambda path: load_config(path)