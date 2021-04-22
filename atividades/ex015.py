#aluguel de carros
d = int(input('Quantos dias você está com o carro?'))
km = float(input('Quantos KM foram rodados?'))
pagar = (d * 60) + (km * 0.15)
print('Você precisa pagar R${:.2f} pelo uso do carro.'.format(pagar))
