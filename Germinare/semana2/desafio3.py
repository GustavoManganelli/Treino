print('Qual o nome do funcionário?')
nome = input()
print('Quantas horas por semana {} trabalha?'.format(nome))
horas = int(input())
print('quantos dependentes {} tem?'.format(nome))
dependentes = int(input())
calculo_horas = horas * 4 * 25
calculo_dependentes = dependentes * 500
soma = calculo_horas + calculo_dependentes
print(nome,'terá um salário mesnal de R${}.00'.format(soma))