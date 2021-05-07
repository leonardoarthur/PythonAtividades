d = float(input('Qual a distância da sua viagem em KM?'))
if d < 200:
    print('O valor da passagem custa R${}'.format(d * 0.50))
else:
    print('O valor da sua passagem vai custar R${}'.format(d * 0.45))