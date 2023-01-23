import time

def permutar(datos, i, length, perms):
    if i==length:
        perms.append("".join(data))
    else:
        for j in range(i,length):
            datos[i], datos[j] = datos[j], datos[i]
            permutar(datos, i+1, length, perms)
            datos[i], datos[j] = datos[j], datos[i]

def numero_palabra(word):
    inicio_tiempo = time.time()
    
    #genera todas las permutaciones de la palabra
    perms = []
    permutar(list(word), 0, len(word), perms)
    
    #ordena las permutaciones alfabéticamente
    perms.sort()
    
    #encontrar la posición de la palabra original en la lista ordenada
    position = perms.index(word)+1
    
    final_time = time.time()
    execution_time = final_time - inicio_tiempo
    print("tiempo de ejecuccion: ", execution_time)
    
    return position


print(numero_palabra("ABAB")) 
print(numero_palabra("AAAA")) 
print(numero_palabra("BAAA"))
print(numero_palabra("PREGUNTA"))
print(numero_palabra("CONTADOR")) 
