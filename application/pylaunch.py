import eel
from interaction.json_store import json_store


def setupApp(config):
    eel.init(config["ui-path"])
    eel.start(config["index-file"])


if __name__ == '__main__':
    config = json_store.load_config("./configuration/app/app.config.json")
    setupApp(config)
