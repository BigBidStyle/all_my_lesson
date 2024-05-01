import sys
def decrypt(cipher):
    print(cipher)
    return cipher

if __name__ == "__main__":
    data = sys.stdin.readlines() # <-- Получаем входные данные в виде списка строк.
    transcript = decrypt(data)
    print(transcript)