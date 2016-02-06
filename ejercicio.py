#!/usr/bin/python
# -*- coding: utf-8 -*-

AuxFile = open ("/etc/passwd","r")  # Archivo -> auxiliar
lineas = AuxFile.readlines()        # Auxiliar -> lista[linea, caracter]

shells = {}             # Init diccionario
for linea in lineas:    # Recorro cada linea leida del fichero
    shells[linea.split(":")[0]] = linea.split(":")[-1][:-1] # Cargo el shell de
                                                            # cada root en el
                                                            # diccionario.
print "Numero de shells: " + str(len(shells))   # Imprimo la cantidad de shells
try:                                        
    print "shell de root:", shells["root"]
    print "shell de imaginario:", shells["imaginario"]
except: # Permite especificar el fallo concreto a capturar de los disponibles
    print "Usuario no encontrado en el diccionario."

AuxFile.close
