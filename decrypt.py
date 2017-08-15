from AESC import AESCipher
Aesc2 = AESCipher()

with open('./file.enc', 'rb') as DIN:
    data_encrypted = DIN.read()
    vector2 = '0123456789abcedf'
    decryptkey = ''
    data_decoded = Aesc2.decrypt(data_encrypted, decryptkey, vector2)

    with open('./file', 'wb') as DUMP:
        DUMP.write(data_decoded)

    print "data decoded by node 2: " + data_decoded

