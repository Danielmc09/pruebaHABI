def ordenar_bloques(arreglo):
    bloques = []  # Para almacenar los bloques de números
    bloque_actual = []  # Para construir el bloque actual

    for numero in arreglo:
        if numero == 0:  # Encuentra el fin de un bloque
            if bloque_actual:
                # Si hay números en el bloque actual, lo ordena y lo guarda
                bloques.append("".join(map(str, sorted(bloque_actual))))
                bloque_actual = []  # Reinicia el bloque actual para el siguiente
            else:
                # Si el bloque actual está vacío (dos ceros consecutivos)
                bloques.append("X")
        else:
            # Agrega el número al bloque actual
            bloque_actual.append(numero)

    # Asegura que el último bloque se procese (en caso de que el arreglo no termine en cero)
    if bloque_actual:
        bloques.append("".join(map(str, sorted(bloque_actual))))

    # Une los bloques ordenados en un string, separados por espacio
    return " ".join(bloques)
