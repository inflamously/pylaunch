import eel

from infrastructure.json_store import json_store


@eel.expose
def get_app_config():
    return json_store.load_config("./configuration/app/app.config.json")


def init():
    pass
