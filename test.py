import hashlib
import time
from itertools import product
#a

def crack_hash(target_hash, charset, max_length):
    inicio = time.perf_counter()  # Captura o tempo inicial
    for length in range(1, max_length + 1):
        for attempt in product(charset, repeat=length):
            attempt = ''.join(attempt)
            hashed_attempt = hashlib.md5(attempt.encode()).hexdigest()
            if hashed_attempt == target_hash:
                fim = time.perf_counter()  # Captura o tempo final
                tempo_decorrido = fim - inicio  # Calcula o tempo decorrido
                print(f"Tempo decorrido: {tempo_decorrido:.4f} segundos")
                return attempt
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio
    print(f"Tempo decorrido: {tempo_decorrido:.4f} segundos")
    return None

# Exemplo de uso
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # Hash MD5 de "password"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
max_length = 8

result = crack_hash(target_hash, charset, max_length)
if result:
    print(f"Senha encontrada: {result}")
else:
    print("Senha não encontrada.")