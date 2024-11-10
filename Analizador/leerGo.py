#Daniel Villamar
def pedirNumeroTest():
    cantidadTest=2
    print(f"De momento existen {cantidadTest} test para su uso\nSeleccione cual desea probar:")
    numeroTest=input()
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

numeroTest=pedirNumeroTest()
algoritmo= "algoritmo"+numeroTest+".go"
ruta_archivo_go = "../testeos/"+algoritmo

codigo_go = leer_archivo_go(ruta_archivo_go)
