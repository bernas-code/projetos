import socket
import time
from concurrent.futures import ProcessPoolExecutor #usar processos
#from concurrent.futures import ThreadPoolExecutor #usar threads

def verificar_porta(ip,porta,resultados):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        resultado = sock.connect_ex((ip,porta))
        if resultado == 0:
            resultados.append(resultado)
            print(f"IP: {ip} ------------- Porta: {porta} / Open \nRunning: ...")
        sock.close()
    except Exception as e:
        print(f"Erro ao verificar porta {porta}: {e}")

def ajuda_scan(ip,portas):
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.map(lambda p: verificar_porta(ip, p ), portas)
    #with ThreadsPoolExecutor(max.worker=100) as executor:
    #   executor.map(lambda p: verificar_porta(ip, p), portas)

def main():
    resultados = []
    ip = input("ip: ")
    print("Buscando...")
    portas = range(1, 1024)
    for porta in portas:
        verificar_porta(ip,porta,resultados)

if __name__ == "__main__":
    main()