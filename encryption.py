import random
import string
chars=" "+string.punctuation + string.ascii_letters + string.digits
chars=list(chars)
key=chars.copy()
random.shuffle(key)
text=input("Enter a message to encrypt: ")
text_change=""
for letters in text:
    index=chars.index(letters)
    text_change += key[index]
print(f"Entered text : {text}")
print(f"Encrypted text : {text_change}")
text=input("Enter a message to decrypt: ")
text_change=""
for letters in text:
    index=key.index(letters)
    text_change += chars[index]
print(f"Entered text : {text}")
print(f"Decrypted text : {text_change}")