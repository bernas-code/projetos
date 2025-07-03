import hashlib
import getpass

def criar_usuario(vetor_user,usuario):
    usuario = input("Digite seu nome de Usuario: ")
    vetor_user.append(usuario)
    print(f"Usuario salvo.")

def transformar_hash(senha,senha_2):
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(senha.encode('utf-8'))
    hash_sha256_2 = hashlib.sha256()
    hash_sha256_2.update(senha_2.encode('utf-8'))
    return hash_sha256.hexdigest()
    
def main():
    vetor_user = []
    criar_usuario(vetor_user,criar_usuario)
    usuarios = ''.join(vetor_user)
    senha = getpass.getpass("Senha: ")

    tentativa = 3
    while tentativa > 0:
        senha_2 = getpass.getpass("Digite sua senha novamente: ")
        hash_1 = transformar_hash(senha,senha_2)    
        hash_2 = transformar_hash(senha_2,senha)

        if hash_1 == hash_2:
            print(f"Seja bem vindo, {usuarios}!") 
            break
        else:
            tentativa -= 1
            print("Senha incorreta, tente novamente...")
            if tentativa == 0:
                print("Número de tentativas excedidas.")
                break

if __name__ == "__main__":
    main()