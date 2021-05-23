from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
from cryptography.fernet import Fernet

def encryptData(str_key, str_data):
    ObjectKey = RSA.importKey(str_key)
    publicKey = PKCS1_OAEP.new(ObjectKey)
    encryptedData = publicKey.encrypt(str_data.encode('utf-8'))
    return encryptedData

def genKey():
	key = Fernet.generate_key()
	return key

def symEncrypt(key, str):
	f = Fernet(key)
	msg = f.encrypt(str)
	return msg

def symDecrypt(key, str):
	f = Fernet(key)
	msg = f.decrypt(str)
	return msg

