# Daniel Villamar
# Ronald Gaibor

import os

def contar_algoritmos(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

def pedirNumeroTest():
    cantidadTest = contar_algoritmos('../testeos')
    numeroTest = input(f"De momento existen {cantidadTest} tests para su uso\nSeleccione cual desea probar: ")
    return numeroTest

def leer_archivo_go(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return ""
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return ""

'''
numeroTest=pedirNumeroTest()
algoritmo= "algoritmo"+numeroTest+".go"
ruta_archivo_go = "../testeos/"+algoritmo

codigo_go = leer_archivo_go(ruta_archivo_go)
'''
# current_dir = os.path.dirname(os.path.abspath(__file__))
# numeroTest=pedirNumeroTest()
# algoritmo= "algoritmo"+numeroTest+".go"
# ruta_archivo_go = os.path.join(current_dir, '..', 'testeos', algoritmo)

# codigo_go = leer_archivo_go(ruta_archivo_go)
