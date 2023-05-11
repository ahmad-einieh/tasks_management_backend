
def encrypt(message):
    key = get_sum(message)
    x =''
    for i in message:
        x += chr(ord(i) + key)
    x += chr(key)
    return x

def decrypt(s_message):
    key = get_last_char(s_message)
    s_message = s_message[:-1]
    x =''
    for i in s_message:
        x += chr(ord(i) - key)
    return x

def verfiy(message, s_message):
    if message == decrypt(s_message):
        return True
    else:
        return False

def get_sum(string):
    letter_sum = 0

    for char in string:
        letter_sum += ord(char)

    return letter_sum

def get_last_char(string):
    key = string[-1]
    key = ord(key)
    return key
