matriz = [['-','-','-'],['-','-','-'],['-','-','-']]

def fnt_agregar(dato,x,y):
    if matriz[x][y] == '-':
        matriz[x][y] = dato.upper()
    elif matriz[x][y] == 'X':
        print('\nEste espacio ya se encuentra ocupado <Enter>')
def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = ' ')
        print()

sw = True
while sw == True:
    fnt_impresion_matriz()
    fnt_agregar(input('Dato: '),int(input('Fila: ')),int(input('Columna: ')))