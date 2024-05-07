matriz = [[0,5,2],[0,3,0],[1,2,4]] 
list_repetir = []
dato = 2
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if dato == matriz[i][j]:
            contador += 1
            posicion = 'Fila = ',i,'Columna = ',j,
            list_repetir.append(posicion)
print(f'\nEl {dato} se encuentra {contador} veces.')
print(f'{dato} se encuentra en las posiciones: ',list_repetir)