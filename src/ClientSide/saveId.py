def saveId(id):
    pathToIdFile = 'idPass.txt'
    try:
        with open(pathToIdFile, 'w') as writer:
            writer.write(id)
    except OSError as e:
        print(e)