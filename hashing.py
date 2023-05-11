
def encrypt(key, message):
    x =''
    for i in message:
        x += chr(ord(i) + key)
    return x

def decrypt(key, s_message):
    x =''
    for i in s_message:
        x += chr(ord(i) - key)
    return x

def verfiy(key, message, s_message):
    if message == decrypt(key, s_message):
        return True
    else:
        return False
