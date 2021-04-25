from infrastructure.json_store import json_store 


class JsonStoreModule:
    def __init__(self, **kwargs):
        if "path" in kwargs:
            self.configuration = json_store.load_config(kwargs["path"])
        