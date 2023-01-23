def power_of_4(n):
    # para ver si la entrada es un entero positivo
    if type(n) != int or n <= 0:
        return False
    # dividir el número entre 4 hasta que  sea indivisible
    while n % 4 == 0:
        n = n / 4
    # si el numero es 1 al final, es una potencia de 4
    if n == 1:
        return True
    else:
        return False


print(power_of_4(1024)) 
print(power_of_4(55)) 
print(power_of_4("Four")) 
