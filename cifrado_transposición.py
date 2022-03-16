import math


def main():
    print("------------------------------------------")
    print("Algoritmo de encriptación - transposición ")
    print("-----------------------------------------\n")

    texto = input("Mensaje: ")
    llave = int(input("Llave (2-%s): " % (len(texto) - 1)))

    encriptado = encriptar(llave, texto)
    print("Texto encriptado: " + encriptado)

    desencriptado = desencriptar(llave, encriptado)
    print("Texto desencriptado: " + desencriptado)


def encriptar(key, message):
    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)


def desencriptar(key, message):
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0;
    row = 0;

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return "".join(plainText)


if __name__ == '__main__':
    main()
