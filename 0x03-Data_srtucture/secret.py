def rot13(text):
    result = []
    for char in text:
        print(char)
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)
        



# Example usage
original_text = "Hello, World!"
encoded_text = rot13(original_text)
print("Original:", original_text)
print("Encoded:", encoded_text)
print("Decoded:", rot13(encoded_text))  # Applying ROT13 again decodes it
