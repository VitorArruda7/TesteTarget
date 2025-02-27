def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

def resolver():
    texto = input("Digite uma string para inverter: ")
    print(f"String invertida: {inverter_string(texto)}")

if __name__ == "__main__":
    resolver()
