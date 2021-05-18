from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from Crypto.Cipher import  PKCS1_OAEP

def encryptData(str_key, str_data):
    print("Key: ", str_key)
    ObjectKey = RSA.importKey(str_key)
    publicKey = PKCS1_OAEP.new(ObjectKey)
    encryptedData = publicKey.encrypt(str_data.encode('utf-8'))
    return encryptedData