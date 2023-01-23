def versos_enorden(versos):
    # Crear una lista de diccionarios con los versos y su número de orden correcto
    correct_order = [
        {'verso': '12 bateristas tocando el tambor,', 'order': 1},
        {'verso': '11 gaiteros tocando la tubería,', 'order': 2},
        {'verso': '10 señores un salto,', 'order': 3},
        {'verso': '9 damas bailando,', 'order': 4},
        {'verso': '8 criadas un ordeño,', 'order': 5},
        {'verso': '7 cisnes nadando,', 'order': 6},
        {'verso': '6 gansos una puesta,', 'order': 7},
        {'verso': '5 anillos de oro,', 'order': 8},
        {'verso': '4 pájaros cantando,', 'order': 9},
        {'verso': '3 gallinas francesas,', 'order': 10},
        {'verso': '2 tórtolas y', 'order': 11},
        {'verso': '1 perdiz en un peral.', 'order': 12}
    ]

    # Ordenar la lista de versos según el orden correcto
    sort_versos = sorted(versos, key=lambda x: next(item for item in correct_order if item["verso"] == x)['order'])

    # Agregar "El día 12 de Navidad mi verdadero amor me dio" al principio del listado
    sort_versos.insert(0, "El día 12 de Navidad mi verdadero amor me dio")

    # Retornar la lista de versos ordenada
    return sort_versoss

# Ejemplo :
versos = ["5 anillos de oro,", "9 damas bailando,", "1 perdiz en un peral.", "12 bateristas tocando el tambor,"]
print(versos_enorden(versos))
