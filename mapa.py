"""Arquivo que guarda a função que retorna o mapa da cidade 
com suas ruas, quadras e semáforos"""

def create_map(): 
    mapa = []
    for i in range(0, 28):
        row = []
        for j in range(0,37):
            row.append({})
        mapa.append(row)

    # Ruas horizontais
    for i in range(0, 28, 3):
        for j in range(0, 37):
            mapa[i][j] = {"type": "rua", "car": None}
    # Ruas verticais
    for j in range(0, 37, 4):
        for i in range(0, 28):
            mapa[i][j] = {"type": "rua", "car": None}
    # Quadras
    for i in range(0, 28):
        for j in range(0, 37):
            if mapa[i][j] == {}:
                mapa[i][j] = {"type": "quadra"}
    # Semáforos
    for i in [0, 27]:
        for j in range(4, 33, 4):
            mapa[i][j]["type"] = "sem"
    for i in range(3, 27, 3):
        for j in range(0, 37, 4):
            mapa[i][j]["type"] = "sem"

    return mapa