import random
pc = random.randint(0, 5)
u = int(input('Adivinhe no número que eu estou pensando de 0 a 5:'))
if pc == u:
    print('Parabéns desafiante, fui derrotado!')
else:
    print('Você foi derrotado por mim HA HA HA, pensei no numero {}'.format(pc))