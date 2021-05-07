n = str(input('Digite seu nome completo: ')).strip().upper()
print('O nome tem {} letra A'.format(n.count('A')))
print('A primeira letra A foi encontrada na posisão {}'.format(n.find('A')+1))
print('A útima letra A foi vista na posição {]'.format(n.rfind('A')+1))
