import os, sys

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(os.getcwd())

if not os.path.exists("./application/pylaunch.py"): 
    raise Exception("Invalid working directory. Exiting.")