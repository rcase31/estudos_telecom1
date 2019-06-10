"""
Verificar livro Sistemas de Radioenlaces Digitais (capítulo 8).
Exemplo 8.4

     __________________________________
    /                 |R1               \
  Tx                  |                  Rx
  *-------------------*------------------*
   \                  |H                /
    \________________/\ _______________/
                    /  \
                   /    \
                  /      \
_________________/        \______________________

  |-------------------|------------------|
       D1                   D2

Imaginar aqui um volume em formato de bola de futebol americano
Também chamado de volume de Fresnnel.

====================================================

    Tx           __
    * __________/\_|+H_________
               /  \          |_ -H
              /    \        /\
_____________/      \______/  \


====================================================


                        v
                       ;##\
        (-            ;##  \                -)
       /\            ;###   \                /\
______/  \__________/#####   \______________/  \___
      Ponto A                              Ponto B



Perda por difração: ocorre um choque com um obstáculo.
Premissa: o obstáculo é agudo (sume de faca).


Atividade (enunciado): pegar no Google Maps um lugar que se enquadre nessas condições
e fazer suas contas.
"""

from math import *

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
    """
    """
    return h/r1

def Prx(Prt, Gant_tx, Gant_rx, Pesp_livre, P_difracao):

    return Prt + Gant_tx + Gant_rx - Pesp_livre - P_difracao

def EIRP(Pt, Gt):
    #Pt e Gt são Potência e Ganho de transmissão
    return Pt * Gt

def r1_f(d1, d2, f, d):
    return 17.3*((d1*d2/(f*d))**0.5)

def lambda_onda(f):
    return (3*10**8)/f

frequencia = 10**10
L_chuva = 2 #dB
_lambda = lambda_onda(frequencia)
L_espaco_livre = 20*log(4*pi*7500/_lambda)

