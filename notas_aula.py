"""
Equações das notas de aula.
"""
def r1(lamb, d1, d2):
    """
    Raio da Zona de Fresnel.
    """
    return (lamb*(d1*d2)/(d1+d2))**0.5

def A0(v1):
    """
    Valor da atenuação "sume de faca". Perda por difração.
    Esta atenuação está em dB.
    """
    ret = 6.9 + 20*log((v1-0.1)**0.5+1)+v1-0.1
    return ret

def v1(h, r1):
    return h/r1

def Prx(Prt, Gant_tx, Gant_rx, Pesp_livre, P_difracao):
    return Prt + Gant_tx + Gant_rx - Pesp_livre - P_difracao

def EIRP(Pt, Gt):
    """
    :param Pt:
    :param Gt:
    :return: portência radiada isotropicamente pelo transmissor
    """
    #Pt e Gt são Potência e Ganho de transmissão
    return Pt * Gt

def r1_f(d_1, d_2, frequencia, d):
    return 17.3*((d_1 * d_2 / (frequencia * d)) ** 0.5)

def lambda_onda(frequencia):
    """
    Calcula o comprimento de onda lambda
    :param frequencia: (f)
    :return: lambda em metros
    """
    return (3*10**8) / frequencia