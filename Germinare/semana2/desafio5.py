t = float(input('Digite o tamnho do seu arquivo em MB:'))
v = float(input('Digite a velocidade da conexão em Mbps:'))
te = (t // v) *8
dr = te <= 60 
print(f'O tempo estimado de donwload é de {te:.2f} segundos.')
print('Download rápido?', dr)