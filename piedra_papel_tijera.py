# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:32:00 2022

@author: class
"""
import random

def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra 'pa' para papel o 'ti' para tijera.\n").lower()
    
    computadora = random.choice(['pi','pa','ti'])
    
    if usuario == computadora:
        return '!Empate¡'
    
    if gano_el_jugador (usuario, computadora):
        return '¡Ganaste!'
    
    return '!Perdiste¡'
    
def gano_el_jugador (jugador, oponente):
    
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    
print(jugar())