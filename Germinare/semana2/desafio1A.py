segundos = int(input('Quantos segundos serão convertidos?'))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60
print('convertendos os segundos teremos {}Horas {}Minutos {}Segundos'.format(horas,minutos,segundos))