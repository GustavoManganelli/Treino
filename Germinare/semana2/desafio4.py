populacao_inicial = int(input('Digite a população inicial:'))
taxa_crescimento = float(input('Digite a taxa de crescimento anual:'))
anos = int(input('Digite o numeros de anos a serem simulados:'))

populacao_final = populacao_inicial * (1 + taxa_crescimento) ** anos
   
print ('A população após {} anos será de aproximadamente {}'.format(anos,populacao_final))