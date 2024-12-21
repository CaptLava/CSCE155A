# Simon Gomez
secret = input()
offset = int(input())
decoded_secret = ""
for char in secret:
    if 'a' <= char <= 'z':
        ascii_secret = ord(char) + offset
        if ascii_secret > 122:
            ascii_secret = 97 + (ascii_secret-123)
        elif ascii_secret < 97:
            ascii_secret = 122 - (97 - ascii_secret - 1)
        decoded_char = chr(ascii_secret)
    else:
        decoded_char = char
    decoded_secret = decoded_secret + decoded_char

print (decoded_secret)

