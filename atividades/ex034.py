s = float(input('Digite o salário: R$'))
if s <= 1250:
    novo = s + (s * 15 / 100)
    print('o novo salário é de R$ {}'.format(novo))
else:
    novo = s + (s * 10 / 100)
    print('o novo salário é de R$ {}'.format(novo))