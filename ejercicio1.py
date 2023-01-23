def dots_and_boxes(links):
    # Se inicializa una matriz de 3x3 con ceros, que representa la cuadrícula inicial del juego.
    grid = [[0 for i in range(3)] for j in range(3)]
    # Se inicializan las puntuaciones de ambos jugadores en cero.
    player1_score = 0
    player2_score = 0
 # Se itera sobre los vínculos proporcionados como entrada y se verifica si son horizontales o verticales.
    for link in links:
       
        if link[0] == link[2]:
           # Se verifica si las cajas formadas por los puntos encima, debajo, a la derecha o a la izquierda de la línea están vacías.
            if grid[link[0]-1][link[1]] == 0 and grid[link[0]+1][link[1]] == 0:
                player1_score += 1