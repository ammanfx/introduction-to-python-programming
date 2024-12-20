
def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) + 13) - ord('a')) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) + 13) - ord('A')) % 26 + ord('A')))
        else:
            result.append(char)
    return'' .join(result)


message = "HELLO WORLD"

secret_message = rot13(message)
print(secret_message)

