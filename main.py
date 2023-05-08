from claseRegistro import Registro
from claseMenu import Menu
import csv
import os

print('hola')
def test () :
    pass

if __name__ == '__main__':
    dias = 30
    horas = 24
    Lista = []

    for i in range(horas):
        Lista.append([0] * dias)

    archivo = open('mes.csv')
    reader = csv.reader(archivo, delimiter = ' ')
    bandera=True
    for linea in reader:
        if bandera:
            bandera=False
        else:
            dias = int(linea[0])
            horas = int(linea[1])
            Temperatura = linea[2]
            Humedad = linea[3]
            Presion = linea[4]
            Lista[horas-1][dias-1] = Registro(Temperatura, Humedad, Presion)

    for i in range(horas):
        print('hora {}'.format(i))
        for j in range(dias):
            print('Dia{}'.format(j+1))
            Lista[i][j].mostrarDatos()

    #op=int (input('Desea ejecutar el test? \n 1 - SI \n 2 - NO\n'))
    #if op==1:
        #test()
    xmenu = Menu()

    b = False
    while not b:
            print('----------- MENU ------------')
            op = int(input('Ingrese la opcion:\n1- Mostrar para cada variable el día y hora de menor y mayor valor\n2- Indicar la temperatura promedio mensual por cada hora\n3- Dado un número de día listar los valores de las tres variables para cada hora del día dado.\n4- Salir\n'))
            if op != 4:
                xmenu.manejoMenu(op,Lista,dias,horas)

            else:
                b = True