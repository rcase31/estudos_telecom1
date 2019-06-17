from resumo import *
from notas_aula import *

# Ex 2.2 Sistemas Modernos de Comunicação Wireless

# Ele pede Pr e a tensão na antena receptora
# para isso usamos a equação de Friis

R = 40000
f = 4*10**9
Pt = 100 # mW
Ae = 0.5
X = 50

# Cálculos intermediários
_lambda = lambda_onda(f)
Aiso = area_isotropica(_lambda)
Lp = perda_percurso(R, _lambda)
ganho = Ae / Aiso

# Uso da eq. de Friis
Pr = eq_friis(Pt, ganho, ganho, Lp) # em mW
Pr_log = 10 * log10(Pr)
print('Potência recebida = ', round(Pr,2), ' mW')
print('Em dBm = ', round(Pr_log, 2), ' dBm')
Vr = sqrt((Pr * 10**-3) * X) * 10 ** 3 # em mW
print('Tensão recebida = ', round(Vr,2), ' mV')
"""
Resposta:
Potência recebida =  0.0  mW
Em dBm =  -55.56  dBm
Tensão recebida =  0.37  mV
"""