from notas_aula import *
from resumo import *

R_terra = 6400 * 1000
R_sat = 36000 * 1000

G_sat = 4 * pi * R_sat ** 2 / (pi * R_terra ** 2)

temperatura_ruido = 290#k
# A razão G/T do sistema fica...
GT = 10 * log10(G_sat) - 10 * log10(temperatura_ruido)
print('a razão G/T do ruído é : ', round(GT,2), 'dBK-1')
"""
Resposta:
a razão G/T do ruído é :  -3.6 dBK-1
"""
