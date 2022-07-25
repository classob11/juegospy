# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:04:42 2022

@author: class
"""
import random

def adivina_el_numero (x):
    print("-----------------------")
    print("----- Bienvenido -----")
    print("-----------------------")
    print("El objetivo es adivinar el número generado por la computadora")
    
    numero_aleatorio = random.randint(1,x)
    
    prediction= 0
    
    while prediction!= numero_aleatorio:
        prediction = int(input(f"Adivina un numero entre 1 y {x}:"))
        
        if prediction < numero_aleatorio:
            print("Intent otra vez. Este numero es muy pequeño")
        elif prediction > numero_aleatorio:
            print("Intenta otra  vez. Este numero es muy grande")
            
    print(f"Felicitaciones.. Adivianste el numero {numero_aleatorio} correctamente")

adivina_el_numero(10)

