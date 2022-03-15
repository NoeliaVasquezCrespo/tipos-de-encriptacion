import cifrado_vigenere


def main():
    print("----------------------------------------")
    print("| Algoritmo de encriptación 'Vigenere' |")
    print("----------------------------------------\n")

    vc = cifrado_vigenere.VigenereCipher()

    string = input("Ingrese un mensaje: ")
    keyword = input("Ingrese la palabra clave: ")

    print(f'Mensaje:  {string}')

    enciphered = vc.encipher(string, keyword)
    print(f'Texto Encriptado: {enciphered}')

    deciphered = vc.decipher(enciphered, keyword)
    print(f'Texto Desencriptado: {deciphered}')


main()
