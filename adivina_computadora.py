# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:09:05 2022

@author: class
"""
import random


def adivina_num_pc (x):
    print("-----------------------")
    print("----- Bienvenido -----")
    print("-----------------------")
    
    print(f"Selecciona un numero entre 1 y  {x} para que la computadora intente adivinarlo")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        #Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion=limite_inferior
        #Obtener una resputa del usuario
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta ingresa (C)").lower()
        
        if respuesta =="a":
            limite_superior = prediccion-1
        elif respuesta == "b":
            limite_inferior = prediccion+1
    print(f"La computadora adivino tu numero correctamente:{prediccion}")        
    
adivina_num_pc(10)    