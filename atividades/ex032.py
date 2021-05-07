a = int(input('Digite um ano para saber se ele é bissexto:'))

if a % 4 == 0 and a % 100 != 0 or a % 400:
    print('Esse ano é bissexto!')
else:
    print('O ano não é bissexto :( ')