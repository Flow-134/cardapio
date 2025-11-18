from funçoes import *
from tabulate import tabulate
cardapio =[
        {"ID" : 1, "Pedido" : "Hamburguer" , "Preço" : 12.50},
        {"ID" : 2, "Pedido" : "Pizza" , "Preço" : 35},
        {"ID" : 3, "Pedido" : "Refrigerante" , "Preço" : 5}
]
while True:
    print("MENU: ")
    print("1 -- Ver cardapio")
    print("2 -- Adicionar item ao pedido")
    print("3 -- Ver pedido")
    print("4 -- remover pedido")
    print("0 -- finalizar")
    op = input("Digite a opção que você deseja: ")


    if op == "1":
        mostrar = cardapio
        cabeçalho = ["ID" , "Pedido" , "Preço"]
        print("\n Cardapio")
        print(tabulate(mostrar, headers="keys", tablefmt="fancy_grid"))
    elif op == "0":
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida!")

    if op =="2":
        pedido=input("Digite o ID do seu item: ")
        qtd=int(input("Digite a quantidade do seu pedido"))
        for i in cardapio:
                total = qtd*i["Preço"]
        