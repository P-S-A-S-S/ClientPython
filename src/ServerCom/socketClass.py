import socket, json
from src.ServerCom.callManager import callManager
from src.ClientSide.getId import getId
from src.ServerCom.encryptData import encryptData, genKey, symDecrypt, symEncrypt

class MySocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < 1024:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
            #    raise RuntimeError("socket connection broken sent")
                break
            totalsent = totalsent + sent

    def myreceive(self, clientId):
        chunks = []
        bytes_recd = 0
        str_key = []
        sym_key = []
        while True:
            #chunk = self.sock.recv(min(1024 - bytes_recd, 2048))
            chunk = self.sock.recv(1024)
            if chunk == b'':
                print("Dead chunk: ",chunk)
                self.sock.close()
                raise RuntimeError("socket connection broken get")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            try:
                str_data = chunk.decode('utf-8')
                dataParsed = str_data.split("-----")
                try:
                    if dataParsed[1] == 'BEGIN PUBLIC KEY':
                        isKey = True
                except:
                    isKey = False

                if isKey:
                    str_key.append(str_data)
                    sym_key.append(genKey())
                    encryptedKey = encryptData(str_key[0], sym_key[0].decode('utf-8'))
                    self.mysend(encryptedKey)
                    if  clientId != False:
                        #str_key.append(str_data)
                        hiQuery = '{"head":{"id":"%s"},"body":{"message":"NewClientConnection"}}' %(clientId)
                        encryptedData = symEncrypt(sym_key[0], hiQuery.encode('utf-8'))
                        self.mysend(encryptedData)
                    elif clientId == False:
                        #str_key.append(str_data)
                        hiQuery = hiQuery = '{"head":{"id":0},"body":{"message":"Id Request"}}'
                        encryptedData = symEncrypt(sym_key[0], hiQuery.encode('utf-8'))
                        self.mysend(encryptedData)

                else:
                    decrypt = symDecrypt(sym_key[0], str_data.encode('utf-8'))
                    print("Encrpyed from server: ", str_data.encode('utf-8'))
                    Query = json.loads(decrypt)
                    response = callManager(Query, self, clientId, str_key[0], sym_key[0])
                    if response == "Id saved":
                        clientId = getId()
            except Exception as e:
                print(e)
        return b''.join(chunks)