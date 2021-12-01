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
print("Lista sin ordenadar\n", lista_numeros)
for i in range(n-1):
    for j in range(n-1-i):
        if lista_numeros[j] > lista_numeros[j+1]:
            aux = lista_numeros[j+1]
            lista_numeros[j+1] = lista_numeros[j]
            lista_numeros[j] = aux
print("Lista ordenada\n", lista_numeros)