import string

alfabeto = list(string.ascii_lowercase)
longitud_alfabeto = len(alfabeto);

print(alfabeto[0])
print(longitud_alfabeto)


def main():
    print("-------------------------------------")
    print("Algoritmo de encriptación - Cesar ")
    print("-------------------------------------\n")

    texto = input("Mensaje: ")
    clave = int(input("Clave (1-26): "))

    encriptado = cifrado_cesar(alfabeto, clave, texto)
    print("Texto encriptado: " + encriptado)

    desencriptado = decodificar_cesar(alfabeto, clave, encriptado)
    print("Texto desencriptado: " + desencriptado)


def cifrado_cesar(alfabeto, n, texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n

            if indice_cesar >= longitud_alfabeto:
                indice_cesar -= longitud_alfabeto

            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra
    return texto_cifrado


def decodificar_cesar(alfabeto, n, texto):
    texto_decodificado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra)
            indice_original = indice_cesar - n

            if indice_original < 0:
                indice_original += longitud_alfabeto

            texto_decodificado += alfabeto[indice_original]
        else:
            texto_decodificado += letra
    return texto_decodificado


if __name__ == '__main__':
    main()
