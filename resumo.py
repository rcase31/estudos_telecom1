"""
Sistemas Modernos de Comunicação Wireless
2.3.3. Perdas por difração
Considerando uma linha reta entra T e R, existem algumas situações:
    a) obstáculo abaixo da linha: não há perda
    b) obstáculo na linha: metade da intensidade do campo
    c) obstáculo acima da linha: regido pela equação de v
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



