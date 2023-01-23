import string

def cifrado_vigenere(ciphertexto, longitud_clave):
    # Crear una lista para almacenar las posibles claves
    possibles_claves = []
        for i in range(longitud_clave):
        block = ""
        # Creo el bloque tomando cada carácter enésimo, donde n es la longitud de la clave
        for j in range(i, len(ciphertext), longitud_clave):
            block += ciphertexto[j]
        # Calcular el índice de coincidencia para el bloque.
  índice_de_coincidencia = calcula_índice_de_coincidencia(block)
        # Determine el cambio necesario para alinear el bloque con la letra inglesa más común, E
        shift = (ord('E') - ord(índice_de_coincidencia[0]))
% 26
        # Crear una clave basada en el turno
        key = chr((shift + ord('A')) % 26)
        possibles_claves.append(key)
    # Return the possible keys
    return "".join(possibles_claves)

def calcula_índice_de_coincidencia(texto):
    """Calcula el índice de coincidencia para el texto dado.
    """
    n = len(text)
    # Crea un diccionario para almacenar la frecuencia de cada letra
    letter_frecuencia = {letter: 0 for letter in string.ascii_uppercase}
    
    for letter in text:
        letter_frecuencia[letter] += 1
    # Calcular el índice de coincidencia
    índice_de_coincidencia = 0
    for letter, frecuencia in letter_frecuenciauencia.items():
        índice_de_coincidencia += (frecuencia * (frecuencia - 1)) / (n * (n - 1))
    
    return índice_de_coincidencia

ciphertext = "HELLOWORLD"
key_length = 5
key = cifrado_vigenere(ciphertexto, longitud_clave)
print(key)
