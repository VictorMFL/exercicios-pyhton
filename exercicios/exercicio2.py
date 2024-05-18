# Tarefa 1
number = input("Digite um número inteiro: ")

try:
    if(int(number) % 2 == 0):
        print("Seu número é par.")
    else:
       print("Seu número é impar.")
except:
    print("Você não digitou um número inteiro.")


# Tarefa 2
what_hours = input("Que horas são? ")
hours = what_hours[0:2]

if " " in hours or ":" in hours:
    formated_hours = hours.replace(" ", "").replace(":", "")
    final_hour = int(formated_hours)
    if final_hour <= 11 and final_hour >= 5:
        print("Bom dia.")
    elif final_hour <= 17 and not final_hour <= 5:
        print("Boa tarde")
    elif final_hour > 17 or final_hour <= 4:
        print("Boa noite.")    
else: 
    final_hour = int(hours)
    if final_hour <= 11 and final_hour >= 5:
        print("Bom dia.")
    elif final_hour <= 17 and final_hour >= 5:
        print("Boa tarde")
    elif final_hour > 17 or final_hour <= 4:
        print("Boa noite.")     


# Tarefa 3
first_name = input("Dgite seu primeiro nome: ")

if len(first_name) <= 4:
    print("Seu nome é curto")
elif len(first_name) <= 6:
    print("Seu nome é normal")
elif len(first_name) > 6:
    print("Seu nome é muito grande")    