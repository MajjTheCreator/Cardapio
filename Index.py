cardapio = {}
nomeRestaurante = ""
porcentagemGarcom = 0

with open("Configuracoes.txt", "r") as texto:
    Data = texto.readlines()
    if len(Data) == 0:
        nomeRestaurante = input("Qual o nome do seu restaurante? ")
        porcentagemGarcom = int(input("Qual a porcentagem do garçom? "))
    else:
        nomeRestaurante = Data[0]
        nomeRestaurante = nomeRestaurante[:-1]
        porcentagemGarcom = int(Data[1])

with open("Cardapio.txt", "r") as texto:
    Data = texto.readlines()
    ultimaCategoria = ""
    ultimoItem = ""
    ultimoProduto = ""
    for i in range(len(Data)):
        Data[i] = Data[i][:-1]
        espacoBranco = 0
        for character in Data[i]:
            if character == "\t":
                espacoBranco += 1
        Data[i] = Data[i][espacoBranco:]
        if espacoBranco == 0:
            ultimaCategoria = Data[i]
            cardapio[Data[i]] = {}
        if espacoBranco == 1:
            ultimoItem = Data[i]
            cardapio[ultimaCategoria][Data[i]] = {}
        if espacoBranco == 2:
            ultimoProduto = Data[i]
        if espacoBranco == 3:
            cardapio[ultimaCategoria][ultimoItem][ultimoProduto] = Data[i]

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
        if objetivo == "Nome":
            nomeRestaurante = input("Qual vai ser o novo nome do restaurante? ")
        elif objetivo == "Porcentagem":
            porcentagemGarcom = int(input("Qual vai ser a nova porcentagem do garçom? "))
        else:
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
                print("O valor bruto R$", float(carrinho), " mais a porcentagem do garçom que é de: ", porcentagemGarcom, "%", " dando no total: R$", carrinho + (carrinho * (porcentagemGarcom / 100)), sep="")
                break
            else:
                categoria, item, produto, preco = procurar(objeto)
                carrinho += int(preco)

    elif entrada == "all":
        print("O nome do seu restaurante é: " + nomeRestaurante)
        print("A porcentagem do garçom é de: ", porcentagemGarcom, "%", sep="")
        print("O cardápio é:", cardapio)

    elif entrada == "stop":
        break 

with open("Cardapio.txt", "w") as texto:
    for categoria in cardapio:
        texto.write(categoria + "\n")
        for item in cardapio[categoria]:
            texto.write("\t" + item + "\n")
            for produto in cardapio[categoria][item]:
                texto.write("\t\t" + produto + "\n")
                texto.write("\t\t\t" + cardapio[categoria][item][produto] + "\n")

with open("Configuracoes.txt", "w") as texto:
    texto.write(nomeRestaurante + "\n" + str(porcentagemGarcom))
