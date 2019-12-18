def es_primo(num):
    # si es menos que 2 no es primo, por lo tanto devolvera Falso
    if num < 2:
        return False
    # un rango desde el dos hasta el numero que nosotros elijamos
    for i in range(2, num):
        # si el resto da 0 no es primo, por lo tanto devuelve Falso
        if num % i == 0:
            return False
    # de lo contrario devuelve Verdadero
    return True


def primos(num):  
    cont = 0
    for i in range( num):
        # Llamamos a la primera funcion para ahorrar trabajo ;)
        if es_primo(i) :
            # Que va a determinar si es primo o no
            cont += 1
            print(i)
    print("Hay ", cont, "numeros primos")  # Total de numeros primos
