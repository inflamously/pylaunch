import eel


@eel.expose
def debug_hello():
    return "Hello World, from Python by EEL."


@eel.expose
def debug_sum(testA, testB):
    return testA + testB


@eel.expose
def debug_void():
    pass

def init():
    pass