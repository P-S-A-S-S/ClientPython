from src.ServerCom.socketClass import MySocket
from src.ClientSide.getId import getId

def startClient():
    socketClient = MySocket()
    socketClient.connect("127.0.0.1", 1234)
    clientId = getId()
    if clientId == False:
        socketClient.mysend(b'{"head":{"id":0},"body":{"message":"Id Request"}}')
    else:
        hiQuery = '{"head":{"id":"%s"},"body":{"message":"NewClientConnection"}}' %(clientId)
        socketClient.mysend(hiQuery.encode(encoding='UTF-8'))
    socketClient.myreceive(clientId)