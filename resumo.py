from math import *

"""
Sistemas Modernos de Comunicação Wireless
2.2.1 Radiação Isotrópica
Fala de um modelo específico ideal de antena e fornece algumas medidas como perda (Lp)
"""
def perda_percurso(distancia, _lambda) -> float:
    """
    :param distancia: [R] distância entre antenas
    :param _lambda: [λ] comprimento de onda
    :return: [Lp] perda no percurso
    """
    return (4 * pi * distancia / _lambda) ** 2

def area_isotropica(_lambda) -> float:
    """
    :param _lambda: [λ] comprimento de onda
    :return: [Aiso] área da antena isotrópica
    """
    return (_lambda ** 2) / (4 * pi)


"""
Sistemas Modernos de Comunicação Wireless
2.2.3 A equação de Friis
Relaciona as potências recebida e trasmitida.
"""
def eq_friis(potencia_trasmitida, ganho_transmissor, ganho_receptor, perda_espaco_livre, modo_log=False) -> float:
    """
    Equação de Friis
    :param potencia_trasmitida: (Pt)
    :param ganho_transmissor: (Gt)
    :param ganho_receptor: (Gr)
    :param perda_espaco_livre: (Lp)
    :param modo_log: caso se queira fazer os cálculos em log, usar True aqui
    :return: potência recebida
    """
    if not modo_log:
        return potencia_trasmitida * ganho_receptor * ganho_transmissor / perda_espaco_livre
    else:
        return potencia_trasmitida + ganho_receptor + ganho_transmissor - perda_espaco_livre

"""
Sistemas Modernos de Comunicação Wireless
2.3.3 Perdas por difração
Considerando uma linha reta entra T e R, existem algumas situações:
    a) obstáculo abaixo da linha: não há perda
    b) obstáculo na linha: metade da intensidade do campo
    c) obstáculo acima da linha: regido pela equação de v
Assumimos aqui um obstáculo em forma de faca.
"""

def v(d_1, d_2, _lambda, h) -> float:
    """
    Função para quando há obstrução entre transmissor e receptor.
    :param d_1: distância do transmissor até o obstáculo
    :param d_2: distância do receptor até o obstáculo
    :param _lambda: largura da onda
    :param h: altura do obstáculo, em relação à linha TOR
    :return: parâmetro de Fresnel-Kirchhoff
    """
    numerador = 2 * (d_1 + d_2)
    divisor = _lambda * d_1 * d_2
    return h * (numerador/divisor) ** 2



"""
Sistemas Modernos de Comunicação Wireless
2.9 Cálculos de Enlace
2.9.1 Planejamento de enlace para propagação no espaço livre
Busca-se potência suficiente para ocorrer baixa SNR (relação sinal ruído). Como base fundamental para isso usa-se da eq.
de Friis como base fundamental.
Mas há um problema: a equação de Friis não leva em consideração o ruído. Assim adicionou-se um novo elemento na eq. de 
Friis: a densidade de ruído N0.
Observações:
    + EIRP = Pt * Gt

"""

def eq_planejamento_enlace(potencia_trasmitida, ganho_transmissor, ganho_receptor, perda_espaco_livre,
                           temperatura_ruido, modo_log=False) -> float:
    """
    Equação nos fornece a razão C/N0, que é uma forma de expressar SNR (relação sinal ruído).
    :param potencia_trasmitida: (Pt)
    :param ganho_transmissor: (Gt)
    :param ganho_receptor: (Gr)
    :param perda_espaco_livre: (Lp)
    :param temperatura_ruido: (Te)
    :param modo_log: caso se queira fazer os cálculos em log, usar True aqui
    :return: razão portadora-ruído
    """
    #constante de Boltzmann [dBW-sk^-1]
    k = -288.6
    potencia_recebida = eq_friis(potencia_trasmitida, ganho_transmissor, ganho_receptor / temperatura_ruido,
                                 perda_espaco_livre, modo_log)
    if modo_log:
        return potencia_recebida - k
    else:
        return potencia_recebida / k


