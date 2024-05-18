
while True:
    exit = input("Sair? ")

    exit = exit.lower().startswith("s")

    if exit == False:
        try:
            number1 = input("Primeiro número: ")
            operator = input("Qual o operador? ")
            number2 = input("Segundo número: ")

            num1 = int(number1)
            num2 = int(number2)

            valid_operators = "+-*%/"

            if operator not in valid_operators:
                print("Digite um operador válido.")
                continue

            if len(operator) > 1:
                print("Digite apenas 1 operador.")
                continue

            if operator == "+":
                print(num1 + num2)
            elif operator == "-":
                print(num1 - num2)
            elif operator == "*":
                print(num1 * num2)
            elif operator == "/":
                print(num1 / num2)    
            elif operator == "%":
               print(num1 % num2)   
        except :
            print("Ocorreu algum erro ao calcular.")
    else:
        print("Você saiu.")        
        break 
