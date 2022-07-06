import random

armasEquipoUno = input('Ingrese las letras de las armas del equipo uno: ');
vulnerabilidadesEquipoUno = input('Ingrese las vulneravilidades del equipo uno: ');

armasEquipoDos = input('Ingrese las letras de las armas del equipo dos: ');
vulnerabilidadesEquipoDos = input('Ingrese las vulneravilidades del equipo dos: ');

tiposArmas = ['.','-','+','*','T','Y','|','W','X','M'];
nombreEquipos = ['VIGBIANA','FIOTA'];
nombreEquiposAux = ['VIGBIANA','FIOTA'];

armaAleatoriaEquipoUno = random.choice(armasEquipoUno);
armaAleatoriaEquipoDos = random.choice(armasEquipoDos);
nombreEquipoUno = random.choice(nombreEquipos);
nombreEquipos.remove(nombreEquipoUno);
nombreEquipoDos = nombreEquipos[0];
tipoAleatorio = '';
salida = '';

datosEquipos = {
    nombreEquipoUno: {
        'nombre': nombreEquipoUno,
        'armas': armasEquipoUno,
        'vulneravilidades': vulnerabilidadesEquipoUno
    },
    nombreEquipoDos: {
        'nombre': nombreEquipoDos,
        'armas': armasEquipoDos,
        'vulneravilidades': vulnerabilidadesEquipoDos
    }
}

for vulneravilidades in datosEquipos['VIGBIANA']['vulneravilidades']:
    if vulneravilidades in datosEquipos['FIOTA']['armas']:
        datosEquipos['FIOTA']['armas'] = datosEquipos['FIOTA']['armas'].replace(vulneravilidades,'')
        
for vulneravilidades in datosEquipos['FIOTA']['vulneravilidades']:
    if vulneravilidades in datosEquipos['VIGBIANA']['armas']:
        datosEquipos['VIGBIANA']['armas'] = datosEquipos['VIGBIANA']['armas'].replace(vulneravilidades,'')

for equipo in nombreEquiposAux:
    for datos in datosEquipos[equipo]['armas']:
        tipoAleatorio = random.choice(tiposArmas);
        if datos == tipoAleatorio:
            salida += datosEquipos[equipo]['nombre'][:1];
        else:
            salida += '≈';
        """if datos in tiposArmas:
            salida += datosEquipos[equipo]['nombre'][:1];
        else:
            salida += '≈';"""

print(salida);
    