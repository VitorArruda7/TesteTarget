def resolver():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(f"Resultado do Problema 1: {SOMA}")

if __name__ == "__main__":
    resolver()
