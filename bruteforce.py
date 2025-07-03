## brute force por hash
import itertools
from multiprocessing import Pool, cpu_count
import hashlib 
import time

#adicionar multiprocessos paralelos para quebrar a hash mais facil

def quebrar_hash (hash_a,chars,comprimento_max):
    inicio = time.perf_counter()
    from itertools import product
    for length in range(1, comprimento_max+1):
            for tentativa in product(chars, repeat=length):
                tentativa = ''.join(tentativa)
                tentativa_hash = hashlib.md5(tentativa.encode()).hexdigest()
                if tentativa_hash == hash_a:
                    fim = time.perf_counter()
                    tempo_percorrido = fim - inicio 
                    print(f"O tempo decorrido:{tempo_percorrido:.4f} segundos.")
                    return tentativa
    fim = time.perf_counter()
    tempo_percorrido = fim - inicio 
    print(f"O tempo decorrido:{tempo_percorrido:.4f} segundos.")
    return None

hash_a = 'a62fe230fb661b05fc34925578f3e2c3'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
comprimento_max = 8

resultado = quebrar_hash(hash_a,chars,comprimento_max)
if resultado:
    print(f"Senha encontrada",resultado)
else:
    print("Senha não encontrada.")