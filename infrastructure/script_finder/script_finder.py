from pathlib import Path
import os


def find(self, searchpath, scriptname):
        for path in Path(os.getcwd()).rglob(scriptname + ".py"):
            print(path)
    