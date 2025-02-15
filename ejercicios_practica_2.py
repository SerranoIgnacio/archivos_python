# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    v_stock = ''
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    with open('stock.csv') as csvfile:
        v_stock = list(csv.DictReader(csvfile))
    torni = 0
    for i in range(len(v_stock)):
        lista = v_stock[i]
        for k, v in lista.items():
            if k == "tornillos":
                cant_torni = v
                torni += int(cant_torni)
    print(f'Cantidad total es, {torni}')

def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    with open('propiedades.csv') as csvfile:
        v_prop = list(csv.DictReader(csvfile))

    cantidad_dpto = len(v_prop)
    DosAmbi = 0
    TresAmbi = 0
    for i in range(cantidad_dpto):
        row = v_prop[i]
        for k, v in row.items():
            if k == "ambientes":
                if "2" in v:
                    DosAmbi += 1
                elif "3" in v:
                    TresAmbi += 1
    print(f'El archivo contiene {DosAmbi} dpto con 2 ambientes y {TresAmbi} dpto con 3.')    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
