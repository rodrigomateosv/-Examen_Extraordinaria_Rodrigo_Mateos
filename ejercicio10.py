def potencia(base, exponente):
    # Verificamos si el exponente es negativo
    if exponente < 0:
        
        return None
    else:
        # Inicializamos la variable resultado en 1
        resultado = 1
        # Utilizamos un ciclo for para multiplicar la base por sí misma
        
        for i in range(exponente):
            resultado *= base
        
        return resultado

print(potencia(2, 3)) 
print(potencia(10, 0)) 
print(potencia(-5, 3)) 
print(potencia(-4, 2))
