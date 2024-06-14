#cardapio
cardapio = {}

def procurar(objetivo):
    for categoria in cardapio:
            if categoria == objetivo:
                return categoria, "", "", ""
            for item in cardapio[categoria]:
                if item == objetivo:
                    return categoria, item, "", ""
                for produto in cardapio[categoria][item]:
                    if produto == objetivo:
                        return categoria, item, produto, cardapio[categoria][item][produto]
                    
while True:
    entrada = input("O que deseja fazer?\nadd: adiciona um item\nrmv: deleta um item\nedt: edita o preço de um produto\nsrc: procura o preço de um produto\ncar: começa a contagem do preço dos itens que você adicionar\nstop: para o programa salvando no arquivo de texto ou para de adicionar itens ao carrinho\nall: lista todos os itens\n")

    if entrada == "add":
        categoria = input("Qual a categoria? ")
        item = input("Qual o item? ")
        produto = input("Qual o produto? ")
        preco = input("Qual o preço? ")
        
        if categoria not in cardapio:
            cardapio[categoria] = {}
        if item not in cardapio[categoria]:
            cardapio[categoria][item] = {}
        cardapio[categoria][item][produto] = preco
        
    elif entrada == "rmv":
        objeto = input("O que você deseja deletar? ")
        categoria, item, produto, preco = procurar(objeto)
        if produto != "":
            del(cardapio[categoria][item][produto])
        elif item != "":
            del(cardapio[categoria][item])
        else:
            del(cardapio[categoria])

    elif entrada == "edt":
        objetivo = input("O que você deseja editar? ")
        categoria, item, produto, preco = procurar(objetivo)
        novoPreco = input("Qual o novo preço? ")
        cardapio[categoria][item][produto] = novoPreco

    elif entrada == "src":
        objetivo = input("Qual produto você deseja procurar? ")
        categoria, item, produto, preco = procurar(objetivo)
        print("Este produto está dentro da categoria ", categoria, ", dentro do item ", item, " e custa: R$", cardapio[categoria][item][produto], sep="")

    elif entrada == "car":
        carrinho = 0
        while True:
            objeto = input("Qual produto deseja adicionar ao carrinho?\nSe deseja finalizar o carrinho digite: stop\n")
            if objeto == "stop":
                print("O valor bruto R$", float(carrinho))
                break
            else:
                categoria, item, produto, preco = procurar(objeto)
                carrinho += int(preco)

    elif entrada == "all":
        print("O cardápio é:", cardapio)

    elif entrada == "stop":
        break 
