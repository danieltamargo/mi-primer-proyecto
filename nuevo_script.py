lista = [1, 2, 3, 4, 5]

def suma_lista(lista):
    return sum(lista)

print(suma_lista(lista))

def resta_lista(lista):
    resultado = 0
    for i in lista:
        resultado -= i
    return resultado

print(resta_lista(lista))