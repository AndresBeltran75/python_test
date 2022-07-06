pesoAle = input('Ingrese el peso de Ale: ');
if pesoAle.isnumeric():
    pesoGi = int( int(pesoAle) * 2 ) + 4
    pesoDobleAle = int(pesoGi) - 4;
    pesoAleYGi = int(pesoAle) + int(pesoGi);
    pesoNico = int(pesoAleYGi) / 5;
    mensaje = "";

    if pesoNico >= 0 and pesoNico <= 20:
        mensaje = "Etapa 1";
    elif pesoNico >= 21 and pesoNico <= 40:
        mensaje = "Etapa 2";    
    elif pesoNico >= 41 and pesoNico <= 80:
        mensaje = "Etapa 3";
    else:
        mensaje = "Etapa 4";

    print( str(pesoAle) + " " +  str(pesoGi)  + " " +  str(pesoNico)  );
    print( 'Nico se encuentra en: ' + mensaje.upper() );
else:
    print('El valor ingresado para el peso de Ale, no es numérico.');