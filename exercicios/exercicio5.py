palavra_secreta = "bicicleta"
letras_acertadas = ""
numero_tentativas = 0

caracteries_proibidos = "1234567890/?!@#$%¨&*()_+="

while True:
    tentativa = input("Digite uma letra: ")
    numero_tentativas += 1

    if tentativa in caracteries_proibidos:
        print("Caractere inválido.")
    elif len(tentativa) > 1:
        print("Digite apenas 1 caractere por vez.")
        continue
    elif tentativa in palavra_secreta:
        letras_acertadas += tentativa
    
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print("Parabéns! Você ganhou.")
        print("A palavra era:" + palavra_secreta)
        print(f"Seu numero de tentativas foi {numero_tentativas}")
        numero_tentativas = 0
        palavra_formada = ""
        break
