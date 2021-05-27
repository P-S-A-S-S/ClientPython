from src.ServerCom.socketClass import MySocket
from src.ClientSide.getId import getId
from src.ServerCom.encryptData import encryptData

def startClient():
    socketClient = MySocket()
    socketClient.connect("129.159.207.221", 1234)
    print("Connected successfully!")
    clientId = getId()
    hiQuery = 'get public key'
    socketClient.mysend(hiQuery.encode(encoding='UTF-8'))
    socketClient.myreceive(clientId)
