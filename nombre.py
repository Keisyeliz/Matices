nombres = [['','','',''],['','','',''],['','','',''],['','','','']]
import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Keisy Murillo')
    print('Semestre: I')
    fnt_impresion_matriz()
    print('\n\n')

def fnt_impresion_matriz():
    for i in range(len(nombres)):
        for j in range(len(nombres[i])):
            print(nombres[i][j], end = ' ')
        print()

def fnt_agregar():# Ingreso secuencial
    for i in range(len(nombres)):
        for j in range(len(nombres[i])):
            nombres[i][j] = input(f'Ingrese un nombre {i},{j}: ')
    input('\nLos nombres se han registrado correctamente <ENTER>')
    fnt_impresion_matriz()

fnt_agregar()