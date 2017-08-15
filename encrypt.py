from AESC import AESCipher
Aesc1 = AESCipher()

with open('./file.raw', 'rb') as DAT:
    data = DAT.read();
    print "data from node 1: " + data
    vector1 = '0123456789abcedf'
    encryptkey = ''
    data_encrypted = Aesc1.encrypt(data, encryptkey, vector1)

    with open('./file.enc', 'wb') as DOUT:
        DOUT.write(data_encrypted);

