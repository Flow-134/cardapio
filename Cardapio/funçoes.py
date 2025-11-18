from tabulate import tabulate

def carregar_cardapio(cardapio):
    cardapio =[
        {"ID" : 1, "Pedido" : "Hamburguer" , "Preço" : 12.50},
        {"ID" : 2, "Pedido" : "Pizza" , "Preço" : 35},
        {"ID" : 3, "Pedido" : "Refrigerante" , "Preço" : 5}
    ]
    return cardapio

def exibir_cardapio(cardapio):
    cabeçalho = ["ID", "Pedido", "Preço"]
    print(tabulate(cardapio, headers=cabeçalho, tablefmt="grid"))

def adicionar_pedido(cardapio):
    return input("Digite o ID do seu item: ")
    return input("Digite a quantidade do ")

