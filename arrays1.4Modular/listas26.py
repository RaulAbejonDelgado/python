"""MODIFICAR VALORES EN CONJUNTO MEDIANTE SLICING"""
def acciones_mod_slic_listas():
    mi_listin = range(20)
    print "MODIFICAR VALORES POR SU RANGO DE INDICE LISTAS"
    print "Creo una lista con range para el ejemplo mi_listin = range(20)"
    print (mi_listin)
    print "Si le indicamos una serie de valores en un determinado rango de indice esta accion nos sobreescribira dichos elementos que coincidan con el indice parametrizado "
    print "EJEMPLO:"
    print "mi_listin[6:9]='seis','sieto','ocho' le estoy indicando que haga la modificacion desde el indice 6 hasta la posicion indice 9"
    print "Para que funcione como esperamos tiene que tener coherencia entre el rango de indices que le damos y la cantidad de datos que queremos modificar"
    mi_listin[6:9]="seis","siete","ocho"
    print (mi_listin)
    print "Aunque si lo que queremos es introducir un determinado patron de modificacion podemos hacer uso del tercer parametro como cuando accediamos a los indices por rango"
    print "ejemplo:"
    print "creo una lista con range por ejemplo. mi_prueba=range(20)"
    mi_prueba=range(20)
    print (mi_prueba)
    mi_prueba[0:21:2]="dato_nuevo1","dato_nuevo2","dato_nuevo3","dato_nuevo4","dato_nuevo5","dato_nuevo6","dato_nuevo7","dato_nuevo8","dato_nuevo9","dato_nuevo10"
    print (mi_prueba)
    print "mi_prueba[0:20:2] con esta sintaxis que ya la conocemos , le estaria diciendo que desde la posicion indice 0 hasta la posicion indice 20 , inserte modificaciones cada 2 indices con los valores que quieras pasarle"
    print "en este caso para que nos funcione correctamente y si en una lista de 20 elementos quiero modificar cada 2 indices nos da un total de 10 que seran los valores que pedira para su correcto funcionamiento"
    print "EJERCICIO: Crea una lista y modifica varios por su rango [desde:hasta] y despues prueba hacerlo con los 3 argumentos [desde:hasta:saltos], y saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(27)"
