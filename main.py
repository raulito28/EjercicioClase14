lista_numeros = []
while True:
    while True:
        try:
            e = int(input("Introducir elemento de lista a ordenar: "))
            break
        except:
            print("El dato introducido no es un número que sea válido")

    if (e == -9999):
        break
    lista_numeros.append(e)
    n = len(lista_numeros)
    for i in range(n-1):