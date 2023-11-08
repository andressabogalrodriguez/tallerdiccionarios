# Lista de estudiantes
estudiantes =[
    {
        'nombre': 'Andrés ',
        'apellido': 'Sabogal',
        'promedio': 3.8,
        'nivel_prog': 2,
        'edad': 19,
        'estado_civil':'soltero'
    }
    ,
    {
        'nombre': 'Nicolas',
        'apellido': 'Rojas',
        'promedio': 4.2,
        'nivel_prog': 2,
        'edad': 26,
        'estado_civil':'soltero'
    }
    ,
    {
        'nombre': 'Alejandro',
        'apellido': 'Garcia',
        'promedio': 3.78,
        'nivel_prog': 2,
        'edad': 21,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Sandra',
        'apellido': 'Junco',
        'promedio': 4.39,
        'nivel_prog': 2,
        'edad': 23,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Brayan',
        'apellido': 'Ortiz',
        'promedio': 3.09,
        'nivel_prog': 2,
        'edad': 20,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Jhon',
        'apellido': 'Neva',
        'promedio': 3.5,
        'nivel_prog': 2,
        'edad': 20,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Luisa',
        'apellido': 'Betancourt',
        'promedio': 3.5,
        'nivel_prog': 3,
        'edad': 19,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Linda',
        'apellido': 'Ramos',
        'promedio': 3.61,
        'nivel_prog': 2,
        'edad': 25,
        'estado_civil': 'union'
    }
    ,
    {
        'nombre': 'Maria',
        'apellido': 'Pardo',
        'promedio': 3.8,
        'nivel_prog': 2,
        'edad': 23,
        'estado_civil': 'union'
    }
    ,
    {
        'nombre': 'Diana',
        'apellido': 'Soto',
        'promedio': 3.6,
        'nivel_prog': 2,
        'edad': 20,
        'estado_civil': 'union'
    }
    ,
    {
        'nombre': 'Johan',
        'apellido': 'Galindo',
        'promedio': 3.38,
        'nivel_prog': 2,
        'edad': 22,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Angel',
        'apellido': 'Molano',
        'promedio': 3.6,
        'nivel_prog': 3,
        'edad': 21,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Andres',
        'apellido': 'Segura',
        'promedio': 4.1,
        'nivel_prog': 3,
        'edad': 24,
        'estado_civil': 'comprometido'
    }
    ,
    {
        'nombre': 'Nikole',
        'apellido': 'Florez',
        'promedio': 4.19,
        'nivel_prog': 3,
        'edad': 21,
        'estado_civil': 'soltero'
    }
    ,
    {
        'nombre': 'Ruth',
        'apellido': 'Duran',
        'promedio': 4.0,
        'nivel_prog': 3,
        'edad': 22,
        'estado_civil': 'union'
}
    ]
# Inicializamos algunas variables para los cálculos
edadprom= 0
solteros = 0
promediomay = None
menornivelprogra = float('inf')
apellidoC= 0

# Recorremos la lista de estudiantes
for estudiante in estudiantes:
    edadprom += estudiante['edad']
    if estudiante['estado_civil'] == 'soltero':
        solteros += 1
    if promediomay is None or estudiante['promedio'] > promediomay['promedio']:
        promediomay = estudiante
    if estudiante['nivel_prog'] <menornivelprogra:
        menornivelprogra= estudiante['nivel_prog']
    if estudiante['apellido'][0].upper() == 'C':
        apellidoC += 1

# Calculamos el promedio de edad
edadprom /= len(estudiantes)

# Imprimimos los resultados
print(f"Promedio de edad de los estudiantes: {edadprom:.2f} años")
print(f"Número de estudiantes solteros: {solteros}")
print(f"Estudiante con el mayor promedio: {promediomay['nombre']} {promediomay['apellido']} (Promedio: {promediomay['promedio']})")
print(f"Estudiante con el menor nivel de programación: {menornivelprogra}")
print(f"Número de estudiantes cuyo apellido inicia con 'C': {apellidoC}")
