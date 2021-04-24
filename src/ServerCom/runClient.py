from socketClass import MySocket

def startClient():
    socketClient = MySocket()
    socketClient.connect("127.0.0.1", 1234)
    socketClient.mysend(b'{"head":{"id":0},"body":{"message":"hello Pauet"}}')
    socketClient.myreceive()

startClient()