v = float(input('Qual a velocidade em que o carro passou?'))
m = 7 * (v - 80)
if v > 80:
    print('PARADO AÍ SEU FORA DA LEI! Você está a cima do limite de velocidade')
    print('Vocé foi multado e tem que pagar {} pela sua infração!'.format(m))
else:
    print('Tudo certo maus companheiro, siga boa viagem')