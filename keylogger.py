from pynput import keyboard

#def salvar_arquivo(texto,nome_arquivo="input.txt"):
#    with open(nome_arquivo, 'w') as arquivo:
#        arquivo.write(texto)

#texto=input("Digite um texto: ")

#salvar_arquivo(texto)
#print("Arquivo salvo com sucesso")

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()