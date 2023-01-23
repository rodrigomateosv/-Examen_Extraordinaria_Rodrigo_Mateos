def dots_and_boxes(links):
    # Creamos una matriz de 3x3 llena de ceros
    grid = [[0 for _ in range(3)] for _ in range(3)]
    # Inicializamos las puntuaciones de los jugadores en cero
    player1_score = 0
    player2_score = 0
    
    # Recorremos la lista de vínculos
    for link in links:
        x1, y1, x2, y2 = link # Desempaquetamos el vínculo en variables separadas
        
        # Si la línea es horizontal
        if x1 == x2:
            # Buscamos las cajas formadas por los puntos encima y debajo de la línea
            above_box = grid[x1][y1-1] if y1 > 0 else -1 # Valor de la caja de arriba, -1 si no existe
            below_box = grid[x1][y1] if y1 < 2 else -1 # Valor de la caja de abajo, -1 si no existe
            
            # Si ambas cajas están vacías, el jugador 1 gana un punto
            if above_box == below_box == 0:
                grid[x1][y1-1] = 1
                grid[x1][y1] = 1
                player1_score += 1
            # Si una de las cajas está vacía, el jugador 1 gana un punto sólo para esa caja
            elif above_box == 0:
                grid[x1][y1-1] = 1
                player1_score += 1
            elif below_box == 0:
                grid[x1][y1] = 1
                player1_score += 1
            # Si ambas cajas están completadas, no gana ningún punto
            else:
                pass
            # El jugador 2 toma el turno
            player2_score += 1
        # Si la línea es vertical
        else:
            # Buscamos las cajas formadas por los puntos a la derecha y a la izquierda de la línea
            left_box = grid[x1-1][y1] if x1 > 0 else -1 # Valor de la caja de la izquierda, -1 si no existe
            right_box = grid[x1][y1] if x1 < 2 else -1 # Valor de la caja de la derecha, -1 si no existe
            
            # Si ambas cajas están vacías, el jugador 2 gana un punto
            if left_box == right_box == 0:
                grid[x1-1][y1] = 2
                grid[x1][y1] = 2
                player2_score += 1
            # Si una de las cajas está vacía, el jugador 2 gana un punto sólo para esa caja
            elif left_box == 0:
