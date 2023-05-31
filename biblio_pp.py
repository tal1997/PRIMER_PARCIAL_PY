import re
import json
import csv

#FUNCION LEER ARCHIVO JSON
def leer_archivo(archivo: str):
    with open(archivo, "r") as file:       # Abro el archivo data.json en modo escritura y lectura
        data = json.load(file)             # Cargo la variable data con el diccionario del archivo data.jso
        jugadores = data["jugadores"]      # Con esta variable, llevo toda la lista a diccionarios basicos y poder manejarlo mas facilmente
    return jugadores

#FUNCION MOSTRAR MENU    
def mostrar_menu():
    print("\nMENU DE OPCIONES")
    print("1. LISTAR JUGADOR Y POSICION")
    print("2. MOSTRAR ESTADISTICAS JUGADOR")
    print("3. GUARDAR ESTADISTICAS EN CSV")
    print("4. MOSTRAR LOGROS DE JUGADOR")
    print("5. CALCULAR Y MOSTRAR PROMEDIO ORDEN ASCENDENTE")
    print("6. ES MIEMBRO DEL SALON DE LA FAMA")
    print("7. BUSCAR MAXIMO REBOTERO")
    print("8. BUSCAR MAXIMO TIROS DE CAMPO")
    print("9. BUSCAR MAXIMO ASISTENTE")
    print("10. MOSTRAR JUGADORES CON MAS PUNTOS POR PARTIDO QUE VALOR INGRESADO")
    print("11. MOSTRAR JUGADORES CON MAS REBOTES POR PARTIDO QUE VALOR INGRESADO")
    print("12. MOSTRAR JUGADORES CON MAS ASISTENCIAS POR PARTIDO QUE VALOR INGRESADO")
    print("13. BUSCAR MAXIMO JUGADOR ROBADOR")
    print("14. BUSCAR MAXIMO JUGADOR BLOQUEADOR")
    print("15. MOSTRAR JUGADORES CON MAS TIROS LIBRES POR PARTIDO QUE VALOR INGRESADO")
    print("16. MOSTRAR PPP DEL EQUIPO EXCLUYENDO AL MENOR")
    print("17. MOSTRAR JUGADOR CON MAS LOGROS OBTENIDOS")
    print("18. MOSTRAR JUGADORES CON MAS PORCENTAJE TIROS TRIPLE POR PARTIDO QUE VALOR INGRESADO")
    print("19. BUSCAR JUGADOR CON MAS TEMPORADAS")
    print("20. MOSTRAR JUGADORES CON MAS PUNTOS POR PARTIDO QUE VALOR INGRESADO ORDENADOS POR POSICION")
    print("23. BONUS!!")
    print("0. SALIR")
        
#ELEGIR OPCION MENU
def opcion_menu():
    mostrar_menu()   #---> LLAMO A MOSTRAR EL MENU
    opcion = input("\nIngrese la opcion deseada\n: ")               
    patron = re.match(r'\b\d$|\b\d{2}$', opcion)                    # CON ESTA FUNCION LLAMO A MOSTRAR EL MENU MIENTRAS ELIJO
    while not patron:                                               # LA OPCION DESEADA Y LA VALIDO POR REGEX
        opcion = input("\nERROR, ingrese opcion correcta\n: ")      
        patron = re.match(r'\b\d$|\b\d{2}$', opcion)    
    opcion = int(opcion)                                            # SI PASA LA PRIMER VALIDACION CASTEO Y CONVIERTO LA OPCION A ENTERO
    while opcion > 23:                                              # PARA PODER PASAR A LA SIGUIENTE VALIDACION QUE SE FIJA SI EL NUM INGRESADO ES MENOR A 23(TOTAL DE OPCIONES)   
        opcion = input("\nERROR, ingrese opcion correcta\n: ")
        patron = re.match(r'\b\d$|\b\d{2}$', opcion)
    opcion = str(opcion)                                            # VUELVO A CONVERTIR LA OPCION A STRING
    return(opcion)

#FUNCIONES MENU, LLAMADAS   --> ESTA FUNCION LLAMO AL MAIN PARA QUE REALICE TODO EL RESTO, DE ACA NACE TODO EL PROGRAMA
def funciones_menu(dicci: dict):
    bandera_ejercicio_2 = False                 #UTILIZO ESTA BANDERA PARA AVISAR AL EJERCICIO 3 QUE EL 2 NO HA SIDO REALIZADO TODAVIA, ENTONCES NO ME DEJARA INGRESAR HASTA COMPLETAR EL 2
    while True:                                                         
        match opcion_menu():                            #CREO EL MATCH DE LA FUNCION OPCION MENU PARA COMPARAR CON CADA CASE QUE LLAMARA A LA FUNCION CORRESPONDIENTE
            case "1":
                lista_jugadores_posicion = listar_jugador_posicion(dicci)
                for jugador_posicion in lista_jugadores_posicion:
                    print(jugador_posicion)
            
            case "2":
                total_indices = (len(dicci)-1)                                                     #CONSULTO LA CANTIDAD DE ELEMENTOS DE LA LISTA Y LE RESTO UNO ASI PUEDO CONTAR DESDE EL INDICE 0
                indice = input("\nIngrese el indice que desea buscar: 0(incluido) a {0}(incluido) ".format((total_indices)))
                patron = re.match (r'\b[\d]$|\b[\d]{2}$',indice)       #VERIFICO SI ES VALIDA LA OPCION INGRESADA
                while not patron:
                    indice = input("\nERROR. Ingrese indice valido: 0(incluido) a {0}(incluido) ".format((total_indices)))
                    re.match (r'\b[\d]$|\b[\d]{2}$',indice)                         #SI NO HAY MATCH, QUE EL USUARIO REINGRESE EL NUMERO
                indice = int(indice)                                                #SI HUBO MATCH,CONVIERTO EL VALOR A ENTERO Y PASO A LA SIGUIENTE VALIDACION
                while indice < 0 or indice > total_indices:                         #VERIFICO SI EL NUMERO INGRESADO ES MENOR AL MAXIMO DE LA LISTA
                    indice = input("\nERROR. Ingrese indice valido: 0(incluido) a {0}(incluido) ".format((total_indices)))  #DE LO CONTRARIO QUE EL USUARIO REINGRESE UNA OPCION VALIDA
                    patron = re.match (r'\b[\d]$|\b[\d]{2}$',indice)                          
                indice = int(indice)
                
                jugador_datos = jugador_estadisticas_por_indice(dicci , indice)
                print(jugador_datos)                # IMPRIME EL RETORNO DE LA FUNCION CON EL DICCIONARIO NECESARIO 
                bandera_ejercicio_2 = True          #CONVIERTO LA BANDERA A TRUE PARA DAR AVISO AL EJERCICIO 3 QUE PUEDE CONTINUAR
                               
                
                
            case "3":
                while not bandera_ejercicio_2:                                  #PRIMERO VERIFICO QUE LA BANDERA EL EJERCICIO 2 SEA TRUE, SI ES FALSE, ME DE DEVEULVE AL MENU PRINCIPAL
                    print("Primero debe realizar el punto 2.")
                    input("Presione cualquier tecla para volver al menu.")
                    break  # Salir del bucle actual

                if bandera_ejercicio_2:
                    guardar_usuario = input("\nDesea guardar el ejercicio 2 en un archivo csv para ver más tarde?  Y/N: ")
                    patron = re.match(r'\b[yY]$|\b[nN]$', guardar_usuario)
                    while not patron:
                        guardar_usuario = input("\nERROR. Ingrese una respuesta válida: Y/N ")
                        patron = re.match(r'\b[yY]$|\b[nN]$', guardar_usuario)
                    guardar_csv = exporta_csv('est_jugador.csv', jugador_datos)
                    print(guardar_csv)
                    
            case "4":
                nombre_buscado = input("Ingrese nombre del jugador:")               #INGRESO EL NOMBRE BUSCADO
                verif_nombre_buscado = validar_nombre(nombre_buscado)               #VALIDO PARA VERIFICAR SI ESTA BIEN EL DATO
                while verif_nombre_buscado == -1:                                   #SI LA VERIF DEVUELVE -1, NO HIZO MATCH
                    nombre_buscado = input("ERROR. Ingrese un nombre valido:")
                    verif_nombre_buscado = validar_nombre(nombre_buscado)
                
                nombre_buscado = nombre_buscado.capitalize()                        #CAPITALIZO EL NOMBRE VERIFICADO ARRIBA
                buscar_nombre = se_encuentra_en(dicci, nombre_buscado)              #LLAMO A LA FUNCION SE_ENCUENTRA_EN PARA VERIFICAR SI EL NOMBRE SE ENCUENTRA EN LA LISTA DEL DREAMTEAM
                while buscar_nombre == -1:                                          
                    print("El nombre ingresado no se encuentra en el plantel\n")    #SI LA FUNCION DEVUELVE -1, NO ENCONTRO EL NOMBRE Y ME IMPRIME QUE EL NOMBRE NO SE ENCUENTRA EN EL PLANTEL
                    nombre_buscado = input("Error, ingrese un nombre valido: ").capitalize()  # SE VUELVE A SOLICITAR EL NOMBRE
                    buscar_nombre = se_encuentra_en(dicci, nombre_buscado)                 #RETORNA EL DICCIONARIO COMPLETO DEL JUGADOR ENCONTRADO

                logros_nombre_buscado = jugador_por_nombre_logros(buscar_nombre)        #UNA VEZ ENCONTRADO EL NOMBRE EN EL PLANTEL, SE LLAMA A LA FUNCION JUGADOR_POR_NOMBRE_LOGROS
                print(logros_nombre_buscado)                                            #QUE ME DEVOLVERA EL NOMBRE Y LOS LOGROS DEL JUGADOR BUSCADO
                
            case "5":
                promedio_puntos = promedio_punto_ordenado(dicci)            #CARGO LA VARIABLE CON EL DICCIONARIO PARA SABER EL PPP ORDENADO QUE REALIZARA LA FUNCION
                for datos in promedio_puntos:
                    print(datos)                                            #MUESTRO LOS DATOS ITERANDOLOS DE A UNO PARA QUE SALGA RENGLON A RENGLON EN ORDEN
            
            case "6":                                   
                es_fama = input("Que jugador queres saber: ")               #CONSULTO QUE JUGADOR DESEA AVERIGUAR SI ES SALON DE LA FAMA      
                verif_es_fama = validar_nombre(es_fama)                     #VERICO NOMBRE
                while verif_es_fama == -1:                      
                    es_fama = input("ERROR, ingresa un nombre valido: ")
                    verif_es_fama = validar_nombre(es_fama) 
                es_salon = es_salon_fama(dicci, es_fama.capitalize())       #LLAMO A FUNCION ES_SALON_FAMA, PASANDOLE EL DICCIONARIO Y EL NOMBRE CAPITALIZADO
                print(es_salon)                                             #IMPRIMO EL RESULTADO EN PANTALLA
                
            case "7":
                maximo_rebotero = buscar_maximo(dicci, "rebotes_totales")
                print(maximo_rebotero)
            case "8":
                mayor_porcentaje_tiros_campo = buscar_maximo(dicci, "porcentaje_tiros_de_campo")
                print(mayor_porcentaje_tiros_campo)
            case "9":
                asistencias_totales = buscar_maximo(dicci, "asistencias_totales")
                print(asistencias_totales)
            case "10":
                valor_ppp = input("Ingrese el ppp que desee: ")
                verif_valor = validar_numero_dos_digito(valor_ppp)
                while verif_valor == -1:
                    valor_ppp = input("Ingrese el ppp que desee: ")
                    verif_valor = validar_numero_dos_digito(valor_ppp)
                mayores = mayor_que_ingresado(dicci, float(valor_ppp) , "promedio_puntos_por_partido")
                print(mayores)
            
            case "11":
                valor_ppp = input("Ingrese el ppp que desee: ")
                verif_valor = validar_numero_dos_digito(valor_ppp)
                while verif_valor == -1:
                    valor_ppp = input("Ingrese el ppp que desee: ")
                    verif_valor = validar_numero_dos_digito(valor_ppp)
                mayores = mayor_que_ingresado(dicci, float(valor_ppp) , "promedio_rebotes_por_partido")
                print(mayores)
            case "12":
                valor_ppp = input("Ingrese el ppp que desee: ")
                verif_valor = validar_numero_dos_digito(valor_ppp)
                while verif_valor == -1:
                    valor_ppp = input("Ingrese el ppp que desee: ")
                    verif_valor = validar_numero_dos_digito(valor_ppp)
                mayores = mayor_que_ingresado(dicci, float(valor_ppp) , "promedio_asistencias_por_partido")
                print(mayores)
            case "13":
                mayor_robador = buscar_maximo(dicci, "robos_totales")
                print(mayor_robador)
            case "14":
                mayor_bloqueador = buscar_maximo(dicci, "bloqueos_totales")
                print(mayor_bloqueador)
            case "15":
                valor_ppp = input("Ingrese el ppp que desee: ")
                verif_valor = validar_numero_dos_digito(valor_ppp)
                while verif_valor == -1:
                    valor_ppp = input("Ingrese el ppp que desee: ")
                    verif_valor = validar_numero_dos_digito(valor_ppp)
                mayores = mayor_que_ingresado(dicci, float(valor_ppp) , "porcentaje_tiros_libres")
                print(mayores)
            case "16":
                ppp_equipo = promedio_pp_excluido(dicci)
                print(ppp_equipo)
            case "17":
                mayor_logros = mayor_cant_logros(dicci)
                print(mayor_logros)
                
            case "18":
                valor_ppp = input("Ingrese el porcentaje de tiros triples que desee: ")
                verif_valor = validar_numero_dos_digito(valor_ppp)
                while verif_valor == -1:
                    valor_ppp = input("Ingrese el porcentaje de tiros triples que desee: ")
                    verif_valor = validar_numero_dos_digito(valor_ppp)
                mayores = mayor_que_ingresado(dicci, float(valor_ppp) , "porcentaje_tiros_triples")
                print(mayores)
                
            case "19":
                mayor_temporadas_jugadas = buscar_maximo(dicci, "temporadas")
                print(mayor_temporadas_jugadas) 
            
            case "20":
                valor_ppp = input("Ingrese el porcentaje de tiros que campo que desee: ")
                verif_valor = validar_numero_dos_digito(valor_ppp)
                while verif_valor == -1:
                    valor_ppp = input("Ingrese el porcentaje de tiros que campo que desee: ")
                    verif_valor = validar_numero_dos_digito(valor_ppp)
                mayores = mayor_que_ingresado_posicion(dicci, float(valor_ppp) , "porcentaje_tiros_de_campo")
                print(mayores)
            case "23":
                bono = bonus()
                print(bono)
            
            case "24":
                jugadores_posic = jugadores_por_posicion(dicci)
                print(jugadores_posic)
                       
            case "25":
                cant_allstar = cantidad_allstar(dicci)
                for i in cant_allstar:
                    print(i)            
            
            case "26":
                jugadores_estadisticas_mayor = jugadores_por_max_estadistica(dicci)
                for i in jugadores_estadisticas_mayor:
                    print(i)
            
            case "27":
                maximo_estadistica = maximo_jugador_estadisticas(dicci)
                print("El jugador con mas estadisticas es: {0}".format(maximo_estadistica))
                
            case "0":
                exit()
            
#FUNCION LISTAR JUGADORES POR POSICION
def listar_jugador_posicion(dicci):
    lista_dato = []                                         #UNA VEZ VALIDADO ARRIBA, CREO LA LISTA DONDE GUARDARE LOS DATOS BUSCADOS
    for i in dicci:                                         #RECORRO EL DICICONARIO
        nombre = i["nombre"]
        posicion = i["posicion"]                            #CREO UNA VARIABLE DONDE GUARDARE EL NOMBRE Y EL DATO DEL ITERADOR
        nueva_nombre_posicion = ("{0} - {1}".format(nombre,posicion))
        lista_dato.append(nueva_nombre_posicion)
        
    return lista_dato

#FUNCION ESTADISTICDAS POR INDICE
def jugador_estadisticas_por_indice(dicci, indice):
    lista_jugador = []
    for jugador in dicci:                                   #Recorro los diccionarios y los agrego a una lista para trabajar mas adelante el que preciso
        lista_jugador.append(jugador)
    
    datos_sin_logros = [                                    #CREO UN DICCIONARIO QUE NO CONTENGA LOS DATOS DE LOGROS
    {"nombre": lista_jugador[indice]["nombre"]},
    {"posicion": lista_jugador[indice]["posicion"]},
    {"estadisticas": lista_jugador[indice]["estadisticas"]}
    ]
    return (datos_sin_logros)                               #Devuelvo el jugador buscado sin logros

#FUNCION GUARDAR ARCHIVO CSV    
def exporta_csv(nombre_archivo, contenido):
    try:                                                                              # CON TRY --- EXCEPT LO QUE ME FIJO ES QUE AL CARGAR EL ARCHIVO, NO HAYA UN ERROR, DE LO CONTRARIO DEVUELVE FALSE E IMPRIME QUE NO SE PUDO CREAR EL ARCHIVO
        with open(nombre_archivo, 'w', encoding='utf-8', newline='') as archivo:      # ABRO EL ARCHIVO CON WITH(PARA QUE SE CIERRE AL FINALIZAR), ENCODING ME DA EL FORMATO UNIVERSAL, NEW LINE SE UTILIZA PARA QUE CADA SALTO DE LINEA SE ENCUENTRE VACIO 
            writer = csv.writer(archivo)                                              # UTILIZO LA FUNCION CSV.WRITER ARCHIVO PARA CARGAR A LA VARIABLE WRITER LO QEU DESEO CARGAR
            for diccionario in contenido:                                             # RECORRO LOS DICCIONARIOS DEL CONTENIDO(NOMBRE, POSICION, ESTADISTICAS)
                for clave, valor in diccionario.items():                              # POR CADA ITERACION, AGARRO LA CLAVE Y EL VALOR DEL DICCIONARIO CORRESPONDIENTE
                    if isinstance(valor, dict):                                       # CONSULTO SI ESE VALOR ES UN DICCIONARIO ENTONCES
                        valor = ",".join([f"{k}:{v}" for k, v in valor.items()])      # CONVIERTO EL DICCIONARIO A UNA CADENA DE  TEXTO SEPARADO POR COMAS
                    writer.writerow([clave, valor])                                   # ESCRIBO LA CLAVE,VALOR EN EL ARCHIVO. CONINUO CON EL SIGUIENTE DICCIONARIO
        return True, "Se creó el archivo: {0}".format(nombre_archivo)
    except:                                                                           # RETORNO TRUE O FALSE DEPENDE SI SE PUDO O NO CREAR EL ARCHIVO
        return False, "Error al crear el archivo: {0}".format(nombre_archivo)

#FUNCION BUSCAR JUGADOR POR NOMBRE Y MOSTRAR LOGROS
def jugador_por_nombre_logros(dato:dict):                  # TOMA EL VALOR DEL DICCIONARIO QUE SE PASE Y DEVUELVE
    retorno = {                                            # OTRO DICCIONARIO CON EL NOMBRE Y LOGROS
        "nombre": dato["nombre"],
        "logros": dato["logros"]
    }
    return retorno

#FUNCION PROMEDIO PUNTOS ORDENADO
def promedio_punto_ordenado(dicci):                 #RECIBE EL DICCIONARIO DE JUGADORES
    lista_promedio_jugador = []                     #CREO LA LISTA DONDE ALMACENARE LOS JUGADORES Y SU PROMEDIO
    for jugador in dicci:
        nombre = jugador["nombre"]
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]                            
        tupla = (nombre, promedio_puntos)  # Almacenar los datos en una tupla (nombre, promedio_puntos) #RECORRO LA LISTA Y AGARRO SOLO NOMBRE Y PPP DE CADA JUGADOR
        lista_promedio_jugador.append(tupla)        #AGREGO LA TUPLA A LA LISTA

    lista_ordenada = quicksort_basico(lista_promedio_jugador)         #LLAMO A LA FUNCION QUICKSORT
    return(lista_ordenada)                                      #DEVUELVO LA LISTA ORDENADA

#FUNCION VALIDAR NOMBRE
def validar_nombre(nombre):
    patron = re.match(r'\b[a-zA-Z]+\b',nombre)              #PATRON PARA VALIDAR QUE UN NOMBRE TENGA FORMATO ALFABETICO NOMAS
    if patron:
        return nombre                                       #SI HACE MATCH, DEVUELVE EL NOMBRE
    else:
        return -1                                           #DE LO CONTRARIO DEVUELVE -1
    
#FUNCION VALIDAR JUGADOR EN PLANTEL
def se_encuentra_en(dicci, dato):                   # FUNCION PARA VALIDAR SI EL JUGADOR PERTENECE AL DREAMTEAM, PIDE DICCIONARIO Y DATO A BUSCAR
    encontrado = False                              # INICIO ESTA VARIABLE EN FALSE PORQUE DE NO ENCONTRAR EN TODO EL DICCIONARIO EL DATO BUSCADO, RETORNARA -1
    for jugador in dicci:                           # RECORRO LA LISTA DE LOS DICCIONARIOS
        if dato in jugador["nombre"]:               # SI ENCUENTRA EL DATO DENTO DE LOS VALORES DE LA CLAVE "NOMBRE"
           encontrado = True                        # CONVIERTE A ENCONTRADO EN TRUE 
           return jugador                           # Y RETORNA EL DICCIONARIO CORRESPONDIENTE
       
    if encontrado == False:
        return -1
    
#FUNCION ES SALON DE LA FAMA
def es_salon_fama(dicci, dato):                     # FUNCION PARA SABER SI EL JUGADOR PERTENECE AL SALON DE LA FAMA, INCORPORA DICCIONARIO Y DATO A BUSCAR
    encontrado = False                              # CARGO LA VARIABLE ENCONTRADO EN FALSE PARA SABER SI NO ENCUENTRA NINGUNA COINCIDENCIA DEVOLERA QUE EL JUGADOR NO PERTENECE AL DREAMTEAM
    for jugador in dicci:                           # RECORRO LA LISTA DE DICCIONARIOS
        if dato in jugador["nombre"]:               #CONSULTO SI EL DATO SE ENCUENTRA EN LOS VALORES DE LA CLAVE "NOMBRE"
            if "Miembro del Salon de la Fama del Baloncesto Universitario" not in jugador["logros"]:            #SI NO ENCUENTRA LO QUE ESTA ENTRE COMILLAS, EN EL DICCIONARIO DE LOGROS, ENTONCES ES TRUE, PORQUE LO QUE INDICA ES SI PERTENECE AL UNIVERSITARIO
                encontrado = True       #CONVIERTO ENCONTRADO A TRUE ASI YA NO HAY FORMA DE QUE EL JUGADOR NO PERTENEZCA AL DREAMTEAM
                return "El jugador {0} se encuentra en el salon de la fama del baloncesto".format(jugador["nombre"])    #SI ENCUENTRA LO MISMO PERO SIN UNIVERSITARIO, SIGNIFICA QUE PERTENECE AL SALON DE LA FAMA DE LA NBA Y DEVUELVE QUE SI, QUE PERTENECE
            else:   
                encontrado = True
                return "El jugador {0} no es miembro del salon de la fama del baloncesto.".format(jugador["nombre"])
    if encontrado == False:
            return("El jugador no es parte del DREAMTEAM")          #RETORNA QUE EL JUGADOR NO PERTENECE AL DREAMTEAM
        
#FUNCION QUICKSORT UNIVERSAL
def quicksort_basico(lista):                        #TRAIGO LA LISTA QUE DESEO ORDENAR
    if len(lista) <= 1:                             
        return lista

    pivote = lista[0]                               #UTILIZO COMO PIVOTE EL ELEMENTO 0 DE LA LISTA (PRIMER ELEMENTO)
    menores = []                                    #CREO LA LISTA DE MENORES Y MAYORES QUE CARGARE ABAJO
    mayores = []                                    # RECORRO LA LISTA DEL SEGUNDO ELEMENTO [1] CON EL ITERADOR X HASTA CUALQUIER OTRO ELEMENTO QUE HAYA

    for x in lista[1:]:                             # SI EL ELEMENTO[1] ES MENOR AL ELEMENTO[1] DEL PIVOTE, ENTONCES
        if x[1] < pivote[1]:                        # CARGO TODOS LOS VALORES DE X A LA LISTA DE MENORES
            menores.append(x)
        else:
            mayores.append(x)                       # DE LO CONTRARIO, SE CARGA A MAYORES

    menores_ordenados = quicksort_basico(menores)   # LE APLICO LA RECURSIVIDAD A LA LISTA DE MENORES Y VUELVO A APLICAR EL PROCESO DE ARRIBA CON UNA LISTA MAS CHICA
    mayores_ordenados = quicksort_basico(mayores)   # LO MISMO REALIZO CON LA LISTA DE MAYORES

    lista_ordenada = []                             # CREO LA LISTA DONDE ALMACENARE LOS DATOS FINALES
    lista_ordenada.extend(menores_ordenados)        # UTILIZO .append PARA AGREGAR LOS VALORES MENORES YA QUE DE ESTA FORMA ME IRA AGREGANDO ORDENADAMENTE LOS VALORES, SE LO CONTRARIO ENTRARIA EN UN BUCLE INFINITO PORQUE SE CARGARIAN COMO VIENE Y NUNCA TERMINARIA DE ORDENARSE
    lista_ordenada.append(pivote)                   # ELL PIVOTE LO AGREGO CON .APPEND PORQUE VA ENTRE MEDIO DE MENORES Y MAYORES
    lista_ordenada.extend(mayores_ordenados)        #TERMINO DE AGREGAR CON EXTEND LOS MAYORES PARA AGREGARLOS AL FINAL DE LA LISTA ORDENADAMENTE

    return lista_ordenada                           #RETORNO LA LISTA ORDENADA

#FUNCION BUSCAR MAXIMO REBOTES, TIROS CAMPO, ASISTENCIA TOTAL, ESTADISTICAS
def buscar_maximo(dicci, dato_buscar):                          # FUNCIION PARA BUSCAR EL MAXIMO DE UN DICC, RECIE DICCIONARIO Y LO BUSCADO
    lista_buscados = []                                         # LISTA DONDE GUARDARE LOS DATOS BUSCADOS
    for jugador in dicci:                                       # RECORRO LA LISTA DE DICCIONARIOS
        if dato_buscar in jugador["estadisticas"]:              # SI EL DATO A BUSCAR SE ENCUENTRA EN LA CLAVE DE ESTADISTICAS ENTONCES:
            nombre = jugador["nombre"]                          # AGARRO EL NOMBRE Y EL VALOR BUSCADO
            valor = jugador["estadisticas"][dato_buscar]
            tupla = nombre, valor                               # LOS CONVIERTO EN UNA TUPLA 
            lista_buscados.append(tupla)                        # AGREGO LA TUPLA A LA LISTA_BUSCADOS
    datos_ordenados = quicksort_basico(lista_buscados)          # APLICO QUICKSORT A LOS ELEMENTOS DE LA LISTA DE TUPLAS
    return ("El jugador con mayor {0} es: {1}".format(dato_buscar, datos_ordenados[-1]))    #RETORNO EL MAYOR JUGADOR, UTILIZ [-1] PARA ACCEDER AL ULTIMO ELEMENTO DE LA LISTA QUE YA ORDENADO SERA EL MAS GRANDE

#FUNCION VALIDAR NUMERO
def validar_numero_dos_digito(numero):                      # FUNCION PARA VALIDAR NUMERO DE 1 O DOS DIGITOS
    patron = re.match(r'\b[\d]{1,2}$',numero)               # EL PATRON BUSCA UN STR QUE COMIENCE Y TERMINE CON 1 O 2 DIGITOS
    if patron:
        return numero                                       # SI HACE MATCH, DEVUELVE EL NUMERO STR
    else:
        return -1                                           # DE LO CONTRARIO DEVUELVE -1 PARA INDICAR QUE NO HUBO MATCH
    
#FUNCION MAYORES PROMEDIOS QUE EL INGRESADO
def mayor_que_ingresado(dicci, dato_ingresado, estadist_ingresada):     # FUNCION PARA SABER LOS MAYORES AL INGRESADO, RECIBE DICCIONARIO, EL VALOR INGRESADO CON EL QUE COMPARARA, Y LA ESTADISTICA A LA QUE PERTENECE
    encontrado = False                                                  # CREO LA BANDERA ENCONTRADO EN FALSE PARA IDENTIFICAR SI ENCUENTRA O NO LO QUE ESTE BUSCANDO
    lista_mayores = []                                                  # CREO LA LISTA DE MAYORES PARA AGREGAR EL NOMBRE Y ESTADISTICA BUSCADA SI ES MAYOR
    for jugador in dicci:                                               # RECORRO LA LISTA DE DICCIONARIOS
        if dato_ingresado < jugador["estadisticas"][estadist_ingresada]:     # SI EL DATO INGRESADO ES MENOR AL VALOR DE LA ESTADISTICA ITERADO ENTONCES
            nombre = jugador["nombre"]                                          
            dato_filtrado = jugador["estadisticas"][estadist_ingresada]      # CARGO EL NOMBRE Y LA ESTADISTICA A LAS VARIABLE, NOMBRE Y DATO_FILTRADO
            tupla = nombre , dato_filtrado                                   # LOS TRANSFORMO EN UNA TUPLA Y AGREGO A LA LISTA
            lista_mayores.append(tupla)
            encontrado = True                                                #MODIFICO LA BANDERA A ENCONTRADO
    if encontrado == False:
        return("NO EXISTE NINGUN DATO MAYOR AL INGRESADO")                  # SI EN NINGUN MOMENTO DEL FOR SE CAMBIA LA BANDERA ENCONTRADO A TRUE, SIGNIFICA QUE NO ENCONTRO NADA EN LA LISTA Y ENTONCES RETORNA QUE NO EXISTE NINGUN DATO MAYOR AL INGRESADO
    lista_mayores = quicksort_basico(lista_mayores)                         # EN EL CASO DE HABER LISTA, SE ORDENARA POR METODO QUICKSORT
    return ("Los jugadores que el {0} es mayor al ingresado son: {1}".format(estadist_ingresada,lista_mayores))   #RETORNO LA LISTA ORDENADA

#FUNCION PPP EXCLUYENDO EL MENOR
def promedio_pp_excluido(dicci):                                #FUNCION PARA AVERIGUAR EL PROMEDIO PUNTOS POR PARTIDO EXCLUYENDO AL MENOR, LA CUAL RECIBE UN DICCIONARIO
    lista_devolver = promedio_punto_ordenado(dicci)             # BASICAMENTE SE REUTILIZA LA FUNCION PROMEDIO_PUNTO_ORDENADO, PASANDOLE EL DICCIONARIO, LA CUAL ME DEVOLVERA LA LISTA ORDENADA
    return lista_devolver[1:]                                   # IMPRIMO LA LISTA EVITANDO A PARTIR DEL ELEMENTO [1], YA QUE EL [0] SERA EL MINIMO
    
#FUNCION MOSTRAR JUGADOR MAYOR CANTIDAD DE LOGROS
def mayor_cant_logros(dicci):                           # FUNCION PARA AVERIGUAR EL JUGADOR CON MAYOR CANTIDAD DE LOGROS
    lista_jugadores_logros = []                         # CREO LA LISTA DE LOGROS JUGADORES
    mayor_logros = 0                                    # INICIALIZO LA VARIABLE MAYOR_LOGROS EN 0 PARA UTILIZARLA COMO CONTADOR MAS ADELANTE
    jugador_mayor_logro_retorno = None                  # ACA CARGARE EL JUGADOR QUE TENGA MAYOR CANTIDAD DE LOGROS, DE BASE LA ARRANCO EN NONE 
    for jugador in dicci:                               # RECORRO LA LISTA DE DICCIONARIOS
        nombre = jugador["nombre"]                      # AGARRO EL NOMBRE DE CADA JUGADOR Y
        contador_logros = (len(jugador["logros"]))      # CARGO LA VARIABLE CONTADOR_LOGROS UTILIZANDO UN LEN(JUGADOR["LOGROS"]) PARA CONTARLE LA CANTIDAD DE LINEAS DE LOGRO QUE TENGA CADA ITERADOR(JUGADOR)
        tupla = nombre , contador_logros                # CREO UNA TUPLA CON LOS VALORES NOMBRE Y CONTADOR_LOGROS
        lista_jugadores_logros.append(tupla)            # CARGO LA TUPLA A LA LISTA DE LOGROS
    
    for i in lista_jugadores_logros:                    # ENTONCES RECORRO LA LISTA DE LOGROS Y CONSULTO EN CADA ITERACION
        if i[1] > mayor_logros:                         # SI EL CONTADOR DE LOGROS(ELEMENTO[1] DE LA TUPLA) ES MAYOR A MAYOR_LOGROS(POR DEFECTO 0)
            mayor_logros = i[1]                         # MODIFICO LA VARIABLE MAYO LOGRO CON EL NUMERO MAYOR CONSULTADO ARRIBA
            tupla = i[0] , i[1]                         # CREO UNA TUPLA CON EL NOMBRE Y EL CONTADOR
            jugador_mayor_logro_retorno = tupla         # AGREGO LA TUPLA A LA VARIABLE PARA RETORNARLA DESPUES
                        
    return("{0} es el jugador con mayor cantidad de logros, con {1}".format(jugador_mayor_logro_retorno[0], jugador_mayor_logro_retorno[1]))  #RETORNO EL JUGADOR CON LA MAYOR CANTIDAD DE LOGROS

#MOSTRAR PPP ORDENADO POR POSICION
def mayor_que_ingresado_posicion(dicci, dato_ingresado, estadist_ingresada): #FUNCION PARA SABER EL PPP ORDENADO POR POSICON, RECIBE DICCIONARIO, EL DATO INGRESADO Y LA ESTADISTICA BUSCADA(EN ESTE CASO PPP)
    encontrado = False                                                          # CREO LA FAMOSA BANDERA ENCONTRADO QUE ME ACOMPAÑO TODO EL PROCESO :_) EN FALSE PARA SABER SI ENCUENTRA LO QUE BUSCCO LA FUNCION
    lista_mayores = []                                                          # CREO LA LISTA DONDE ALMACENARE LOS MAYORES AL DATO INGRESADO
    for jugador in dicci:                                                       # RECORRO LA LISTA DE DICCIONARIOS
        if dato_ingresado < jugador["estadisticas"][estadist_ingresada]:        # CONSULTO SI EL DATO INGRESADO ES MENOR AL DATO DE LA ESTADISTICA DEL JUGADORE ITERADO:
            nombre = jugador["nombre"]                                          # ENTONCES CARGO LA VARIABLE NOMBRE CON EL NOMBRE DEL JUGADOR
            dato_filtrado = (" PPP: {0}".format(jugador["estadisticas"][estadist_ingresada]))    #LA VARIABLE DATO FILTRADO, CON EL DATO DE LA ESTADISTICA BUSCADA
            posicion_jugador = jugador["posicion"]                                 #Y CARGO LA POSICION DEL JUGADOR EN OTRA VARIABLE 
            if posicion_jugador == "Base":
                posicion_jugador = ("{0}.Base".format(1))               
            elif posicion_jugador == "Escolta":
                posicion_jugador = ("{0}.Escolta".format(2))                        # DADAS LAS 5 POSICIONES, ME FIJO POR IF A CUAL PERTENECE Y LE AGREGO UN NUMERO PARA IDENTIFICAR EN EL QUICKSORT PROXIMAMENTE SIENDO:
            elif posicion_jugador == "Alero":                                                          #  "1.BASE" - "2.ESCOLTA" - "3.ALERO" - "4.ALA-PIVOT" - "5.PIVOT"
                posicion_jugador =  ("{0}.Alero".format(3))
            elif posicion_jugador == "Ala-Pivot":
                posicion_jugador = ("{0}.Ala-Pivot".format(4))
            else:
                posicion_jugador = ("{0}.Pivot".format(5))
            
            datos_a_lista = nombre , posicion_jugador , dato_filtrado              #CREO LA VARIABLE DATOS_A_LISTA DONDE VOY A CARGAR NOMBRE, POSICION(YA MODIFICADA) Y EL DATO 
            lista_mayores.append(datos_a_lista)                                    # AGREGO LA VARIABLE A LA LISTA DE MAYORES
            encontrado = True                                                      # CONVIERTO LA BANDERA ENCONTRADO A TRUE
    if encontrado == False:                                             #SI LA BANDERA NUNCA SE ACTUALIZA, NO EXISTE NINGUN DATO MAYOR AL INGRESADO Y LO RETORNO
        return("NO EXISTE NINGUN DATO MAYOR AL INGRESADO")
    lista_mayores = quicksort_basico(lista_mayores)                     #DE LO CONTRARIO, CARGO LA LISTA DE JUGADORES MAYORES AL QUICKSORT PARA ORDENARLA, EN ESTE CASO POR POSICION!!
                                                                                #LOGRO ORDENARLA POR POSICION, PORQUE CARGO LA POSICION COMO SEGUNDO ELEMENTO, Y MI FUNCION QUICKSORT UNIVERSAL, ORDENA POR EL SEGUNDO ELEMENTO DE LOS DATOS INGRESADOS
    return ("Los jugadores que el {0} es mayor al ingresado son: {1}".format(estadist_ingresada,lista_mayores)) #RETORNO LOS DATOS OBTENIDOS

#FUNCION BONUS
def bonus():
    psiquis_en_corto = ("VALE POR UN BONITO CODIGO DE BONUS... SI TAN SOLO TUVIERA UNO!!!1!1!! :')")
    return psiquis_en_corto

#####################################################


#EXTRA JUGADOR POR POSICION
def jugadores_por_posicion(dicci):
    contador_base = 0
    contador_escolta = 0
    contador_alero = 0
    contador_ala_pivot = 0
    contador_pivot = 0
  
    for jugador in dicci:
        if jugador["posicion"] == "Base":
            contador_base +=1
        elif jugador["posicion"] == "Escolta":
            contador_escolta +=1
        elif jugador["posicion"] == "Alero":
            contador_alero +=1
        elif jugador["posicion"] == "Ala-Pivot":
            contador_ala_pivot +=1
        elif jugador["posicion"] == "Pivot":
            contador_pivot +=1
            
    return("BASES: {0}\nESCOLTAS: {1}\nALEROS: {2}\nALA-PIVOT {3}\nPIVOT: {4}".format(contador_base , contador_escolta , contador_alero , contador_ala_pivot , contador_pivot))

#EXTRA ALL STAR DESCENDENTE
def cantidad_allstar(dicci):
    logros_jugadores = []
    
    for jugador in dicci:
            for logros in jugador["logros"]:
                    if "All-Star" in logros:
                        nombre = jugador["nombre"]
                        allstar = logros
                        tupla = (nombre,allstar)
                        logros_jugadores.append(tupla)
                        
    lista_alls_comparativa = []
               
    for jugador in logros_jugadores:
        veces_allstar = int(jugador[1][0:2])
        nombre = jugador[0]
        allst = veces_allstar
        tupla = (nombre, allst) 
        lista_alls_comparativa.append(tupla)
        
    lista_ordenada = quicksort(lista_alls_comparativa)
    lista_ordenada.reverse()
    return lista_ordenada
    
def quicksort(lista):
        pivote = lista[0]                               
        menores = []                                    
        mayores = []                                    

        for x in lista[1:]:                             
            if x[1] < pivote[1]:                        
                menores.append(x)
            else:
                mayores.append(x)                       

        menores_ordenados = quicksort_basico(menores)   
        mayores_ordenados = quicksort_basico(mayores)   

        lista_ordenada = []                             
        lista_ordenada.extend(menores_ordenados)        
        lista_ordenada.append(pivote)                   
        lista_ordenada.extend(mayores_ordenados)        

        return lista_ordenada
        
def jugadores_por_max_estadistica(dicci):
    lista_estadisticas = []
    for jugador in dicci:
        for estadistica in jugador["estadisticas"]:
            lista_estadisticas.append(estadistica)
    
    lista_estadisticas_filtradas = set(lista_estadisticas)
    
    lista_maximos = []
    for estadistica in lista_estadisticas_filtradas:
        maximo = buscar_maximo(dicci , estadistica)
        lista_maximos.append(maximo)
    
    return lista_maximos

def maximo_jugador_estadisticas(dicci):
    max_jugador_estadisticas = None
    max_estadisticas = 0
    
    for jugador in dicci:
        total_estadist = 0
        for estadistica in jugador["estadisticas"].values():
            total_estadist += estadistica
        if total_estadist > max_estadisticas:
            max_jugador_estadisticas = jugador["nombre"]
        
    return (max_jugador_estadisticas)
        
    
        
    
            
        
    