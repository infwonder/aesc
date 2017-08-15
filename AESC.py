import base64
import cStringIO
from binascii import hexlify, unhexlify
#from Crypto.Cipher import AES
#
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]
#
#class AESCipher:
#    def __init__(self):
#        pass
#
#    def encrypt(self, raw, key, iv):
#        raw = pad(raw)
#        cipher = AES.new(key, AES.MODE_CFB, iv)
#        return base64.b64encode(cipher.encrypt(raw)) 
#
#    def decrypt(self, enc, key, iv):
#        enc = base64.b64decode(enc)
#        cipher = AES.new(key, AES.MODE_CFB, iv)
#        return unpad(cipher.decrypt(enc))
from M2Crypto import EVP

class AESCipher:
	def __init__(self):
		pass

	def encrypt(self, raw, key, iv):
		raw = pad(raw)
		cipher = EVP.Cipher('aes_256_cfb', key, iv, 1)
		output = cStringIO.StringIO()
		output.write(cipher.update(raw))
		output.write(cipher.final())
		raw = base64.b64encode(output.getvalue())
		output.close()
		return raw

	def decrypt(self, enc, key, iv):
		enc = base64.b64decode(enc)
		cipher = EVP.Cipher('aes_256_cfb', key, iv, 0)
		output = cStringIO.StringIO()
		output.write(cipher.update(enc))
		output.write(cipher.final())
		enc = output.getvalue()
                output.close()
		return unpad(enc)
