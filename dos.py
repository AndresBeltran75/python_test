cantidadEmpleados = int(input('Cantidad de empleados: '))

empleados = []
nombres   = []

for cantidad in range( cantidadEmpleados ):
    nombre = input('Nombre empleado {index}: '.format(index = cantidad + 1))
    edad   = input('Edad empleado {index}: '.format(index = cantidad + 1))
    dato = dict(nombre = nombre, edad = edad)
    empleados.append( dato )
    
for empleado in empleados:
    print(empleado)

    