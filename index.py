from src.ServerCom.runClient import startClient
import time

def tryToConnect():
    try:
        startClient()
    except Exception as e:
        print("Error: ", e)
        print("Trying to reconnect in 5 seconds...")
        time.sleep(5)
        tryToConnect()

tryToConnect()