class item_carrinho:
    def __init__(self, id: str, name: str, b5kg: float, a5kg: float, in_debt: bool=False, total: float=0.0, totalDiscount:float=0.0) -> None:
        self.id = id
        self.name = name
        self.b5kg = b5kg
        self.a5kg = a5kg
        self.in_debt: bool = in_debt
        self.total: float = total
        self.totalDiscount: float = totalDiscount

def calculate_final_price(item: item_carrinho, kg: int, in_debt: bool):
    productValue:float = 0
    productValueDiscount:float = 0

    if(kg < 5):
        productValue = item.b5kg
    else:
        productValue = item.a5kg

    productValue = productValue * kg

    if(in_debt):
        productValueDiscount = productValue - (productValue * 0.05)

    return item_carrinho(item.id, item.name, item.b5kg, item.a5kg, in_debt, productValue, productValueDiscount)

if __name__ == '__main__':
    products_db = [
        item_carrinho("1", "Filé Duplo", 4.90, 5.80),
        item_carrinho("2", "Alcatra", 5.90, 6.80),
        item_carrinho("3", "Picanha", 6.90, 7.80)
    ]

    print("Mercado J&F - Promoção FRI")
    for i in products_db:
        print(f"{i.id}- {i.name}")
    
    id = input("Digite o tipo que deseja levar: ")
    kg = int(input("Digite a quantidade comprada (em kg): "))

    print("A compra será realizada com cartão de débto?")
    print("1- SIM")
    print("2- NÃO")
    in_debt_str = input("")
    in_debt = False

    if(in_debt_str == "1"):
        in_debt = True

    product:item_carrinho = None

    for i in products_db:
        if(i.id == id):
            product = calculate_final_price(i, kg, in_debt)
            break
    
    print("*********************CUPOM FISCAL**********************")
    print(f"* Carne: {product.name}")
    print(f"* Quantidade: {kg}")
    print(f"* Preço: {product.total}")
    print(f"* Cartão de Debto: {"SIM" if product.in_debt else "NÃO"}")
    print(f"* Total com desconto: {product.totalDiscount}")
    print("********************************************************")
    