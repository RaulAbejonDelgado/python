"""ENUMERAR EL INDICE"""
def accion_enumerar_tuplas():
    print "ENUMERAR UNA TUPPLA POR EL INDICE CON [ENUMERATE]"
    print "Si necesitamos saber el numero de indice en alguna ocasion podemos usar enumerate() para que nos muestra el numero de indice junto el valor"
    print "como observamos lo hace en una tupla y por cada indice crea una tupla con el numero de indice y el valor del elemento del indice"
    print "creo una tupla con rango 20 con mi_listin = range(20)"
    print "Por si acaso me aseguro de que lo que creo es una tupla y puedo hacerlo de la siguiente manera mi_listin = tuple(mi_listin) aunque tambien puedo decirle ya de paso que lo enumere de la siguiente manera mi_listin = tuple(enumerate(mi_listin)) "
    mi_listin = range(20)
    print (mi_listin)
    mi_listin = tuple(enumerate(mi_listin))
    print "'print' tuple(enumerate(mi_listin)) es una tupla" 
    print (mi_listin)
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(7)"
