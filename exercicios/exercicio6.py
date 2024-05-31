import os

lista = []

while True:
    funcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")

    if funcao == "i":
        os.system('cls')
        dado = input("Digite o que você deseja adicionar à lista: ")
        lista.append(dado)

    elif funcao == "a":
        os.system('cls')
        delete = input("Digite o indice do item que vai ser excluido: ")  
        try:
            del lista[int(delete)]
            print("Item excluido com sucesso!")
        except ValueError:
            print("Digite um número inteiro como indice.")
        except IndexError:
            print("Indice inexistente.") 
        except Exception:
            print("Erro desconhecido.")       
            
    elif funcao == "l":
        os.system('cls')
        if len(lista) > 0:
            for indice, dado in enumerate(lista):
                print(indice, dado)
        else:
            print("Não tem nada na lista. \n")        

    else:
        os.system('cls')
        print("Digite uma letra correspondente a ação.")    