def zombie_time_para_penetrar(map, zombie_stats):
    """
    Esta función calcula la cantidad de tiempo que tardan los zombis en penetrar las defensas.
     El mapa del césped está representado por una matriz de cadenas, donde cada cadena representa una fila. 
    """
    moves = 0
    while True:
        # Mover zombies
        for zombie in zombie_stats:
            zombie[2][1] -= zombie[1]
        zombie_stats = [zombie for zombie in zombie_stats if zombie[2][1] > 0]
        
        # Comprueba si algún zombi ha llegado a las posiciones de los tiradores.
        for zombie in zombie_stats:
            if map[zombie[2][0]][zombie[2][1]] != " ":
                return moves
        
        # Dispara tiradores numerados
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j].isdigit():
                    shots = int(map[i][j])
                    while shots > 0:
                        for zombie in zombie_stats:
                            if zombie[2] == [i, j+shots]:
                                zombie[0] -= 1
                                if zombie[0] <= 0:
                                    zombie_stats.remove(zombie)
                        shots -= 1
                        
        
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "S":
                    for zombie in zombie_stats:
                        if zombie[2][0] == i and (zombie[2][1] == j-1 or zombie[2][1] == j+1):
                            zombie[0] -= 1
                            if zombie[0] <= 0:
                                zombie_stats.remove(zombie)
                        elif zombie[2][1] == j and (zombie[2][0] == i-1 or zombie[2][0] == i+1):
                            zombie[0] -= 1
                            if zombie[0] <= 0:
                                zombie_stats.remove(zombie)
        
        moves += 1
