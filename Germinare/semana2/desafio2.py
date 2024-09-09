largura = int(input('Seu terreno tem quantos metros de largura?'))
comprimento = int(input('Seu terreno tem quantos metros de comprimento?'))
metro = int(largura * comprimento)
litro = int(metro / 3)
quant = float(litro/5)
preco = int(30)
multiplicacao = quant * preco
print('Serão necessárias {} latas de tinta custando'.format(quant),multiplicacao)