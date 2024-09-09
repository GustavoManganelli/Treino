h = int(input('Quantas horas serão convertidas?'))
m = int(input('Quantos minutos serão convertidos?'))
seg = int(input('Quantos segundos serão convertidos?'))
soma =3600*h + m*60 + seg
print('convertendo as horas, miuots e segundos informados teremos {}'.format(soma))