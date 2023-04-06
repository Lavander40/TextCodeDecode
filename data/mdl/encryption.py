def CodeText(text, key):
    encText = []
    keyList = []
    for i in range(0, len(key), 2):
        keyList.append(key[i:i+2])
    i = 0
    for litera in range(0, len(text)):
        encText.append(str(ord(text[litera]) + int(keyList[i])))
        if i == len(keyList) - 1:
            i = 0
        else:
            i += 1
    return ' '.join(encText)


def DecodeText(encText, key):
    text = []
    keyList = []
    encText = encText.split()
    for i in range(0, len(key), 2):
        keyList.append(key[i:i + 2])

    i = 0
    for litera in range(0, len(encText)):
        text.append(chr(int(encText[litera]) - int(key[i])))
        if i == len(key) - 1:
            i = 0
        else:
            i += 1
    return str(text)
