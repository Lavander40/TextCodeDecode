def CodeText(text):
    encText = ""
    for i in range(len(text)):
        C = text[i]
        K = ord(C)
        K += 1
        CC = chr(K)
        encText = encText + CC
    return encText


def DecodeText(encText):
    text = ""
    for i in range(len(encText)):
        C = encText[i]
        K = ord(C)
        K -= 1
        CC = chr(K)
        text = text + CC
    return text
