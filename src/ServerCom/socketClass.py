import socket, json
from src.ClientSide.saveId import saveId
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

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while True:
            chunk = self.sock.recv(min(1024 - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken get")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            try:
                str_data = chunk.decode('utf-8')
                print(str_data)
                Query = json.loads(str_data)
                print(Query)
                if Query["id"]:
                    saveId(str(Query["id"]))
            except Exception as e:
                print(e)
        return b''.join(chunks)