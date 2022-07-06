print('EJECUTANDO CUATRO...')

array = []
array.append(dict(nombre='Juan', edad=20))
array.append(dict(nombre='Pedro', edad=30))

print(array[0]['nombre'])


diccionario = {}

diccionario['nombre'] = { 'nombreUno': 'Juan', 'nombreDos': 'Felipe' }
diccionario['edad'] = 20
diccionario['peso'] = '70'

print(diccionario['nombre'])

globals().update( { 'entorno': 'VALOR_ACTUALIZADO' } )

print(globals().get('entorno'))

work['final'].repartition(1).write.mode('overwrite').csv('/Users/andresbeltran/Documents/SALIDAS_PYSAPRK/salida.txt', header=True, sep=';') 

context.stop()
spark.stop()