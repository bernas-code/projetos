##criptografar uma senha

import getpass

x = (int(input("Números inteiros: ")))
print("Digite até 4 números para a Key.")
chave = getpass.getpass("Key: ")
print("Key inserida com sucesso.")

str_x = str(x)
str_chave = str(chave)

if len(str_x) <= len(str_chave):
    print("erro")
else:
    cript=[]
    for i in range(len(str_x)):
            indice_str_chave = i % len(str_chave)
            soma = int(str_x[i]) + int(str_chave[indice_str_chave])
            cript.append(str(soma))
    
    criptografado = ''.join(cript)
    print("Criptografado.\n",criptografado)