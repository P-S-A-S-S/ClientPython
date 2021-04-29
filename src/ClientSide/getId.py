def getId():
    pathToIdFile = 'idPass.txt'
    try:
        with open(pathToIdFile, 'r') as reader:
            return reader.read()
    except OSError as e:
        print("Error getting Id: ",e)
        return False