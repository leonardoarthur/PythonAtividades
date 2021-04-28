'''cat1 = float(input('Digite o cateto oposto:'))
cat2 = float(input('Digite o cateto adjacente:'))
hip = (cat1**2 + cat2**2)**1/2
print('a hipotenuza do triângulo vale:', hip)'''

import math
co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
