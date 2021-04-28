import math
n1 = float(input('Digite o ângulo que você deseja:'))
se = math.sin(math.radians(n1))
co = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O ângulo {} tem as seguintes informações:\n SENO = {:.2f}\n COSSENO = {:.2f}\n TANGENTE = {:.2f}'.format(n1, se, co, tan))
