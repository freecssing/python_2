# . Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. 

def crea_dicc(nom, n1, n2):

    """
        *Recibe una cadena con nombres y dos listas de notas y retorna un diccionario con cada nombre como clave y
        una lista de las dos notas correspondientes al alumno
    """

    nombres_cortada = nom.replace("'", "").replace(",", "")
    
    nombres_cortada = nombres_cortada.split()

    notas = list(zip(n1, n2))

    nombres = list(zip(nombres_cortada, notas))

    dicc_nombres = {item[0]: item[1] for item in nombres}

    return dicc_nombres


def calc_promedio(x):

    result = sum(x) / len(x)

    return result


def promedio_alumnos(dicc):
    
    prom = dict(map(lambda x: (x[0], calc_promedio(x[1])), dicc_nombres.items()))

    return prom


def promedio_total(dicci):
    
    dic_aux = promedio_alumnos(dicci)

    tot = sum(dic_aux.values()) / len(dic_aux)

    return tot


def calc_alto(un_diccionario):

    dicci_aux = promedio_alumnos(un_diccionario)

    mas_alto = max(dicci_aux, key=lambda n: dicci_aux[n])

    return mas_alto


def calc_nota_baja(un_diccionario):

    dic_bajo = dict({key: min(coleccion) for key, coleccion in un_diccionario.items()})

    bajo = min(dic_bajo, key = lambda n: dic_bajo[n])

    return bajo


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francisca', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos',  'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


dicc_nombres = crea_dicc(nombres, notas_1, notas_2)

print('Notas por alumno: ', dicc_nombres)


prom_alumnos = promedio_alumnos(dicc_nombres)

print('Promedio de cada alumno: ', prom_alumnos)


prom_general = promedio_total(dicc_nombres)

print('Promedio general: ', prom_general)


mas_alto = calc_alto(dicc_nombres)

print('Promedio mas alto: ', mas_alto)


nota_baja = calc_nota_baja(dicc_nombres)
print('Nota mas baja: ', nota_baja)