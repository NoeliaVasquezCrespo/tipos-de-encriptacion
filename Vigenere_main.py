alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    texto = input("Mensaje: ")
    llave = input("Llave:  ")

    encriptado = encriptar(llave, texto)
    print("Texto encriptado: " + encriptado)

    desencriptado = desencriptar(llave, encriptado)
    print("Texto desencriptado: " + desencriptado)


def encriptar(clave, txt):
    return vingenere(clave, txt, 'encriptar')


def desencriptar(clave, txt):
    return vingenere(clave, txt, 'desencriptar')


def vingenere(clave, txt, accion):
    cadena_vgn = []
    indice = 0
    clave = clave.upper()

    for i in txt:
        num = alfabeto.find(i.upper())
        if num != -1:
            if accion == 'encriptar':
                num += alfabeto.find(clave[indice])
            elif accion == 'desencriptar':
                num -= alfabeto.find(clave[indice])
            num %= len(alfabeto)
            if i.isupper():
                cadena_vgn.append(alfabeto[num])
            elif i.islower():
                cadena_vgn.append(alfabeto[num].lower())
            indice += 1
            if indice == len(clave):
                indice = 0

        else:
            cadena_vgn.append(i)
    return ''.join(cadena_vgn)


if __name__ == '__main__':
    main()
