def unpack2():
    print "RELACIONAR OBJETOS CON ITEMS DE UNA LISTA / TUPLA POR INDICE DE RANGO"
    print "tambien podemos relacionar un determinado numero de items con objetos por su rango de indice:"
    print "mis_datos2=('rul','tecnico','si','no')"
    print "estudia, trabaja =mis_datos2[2:] relaciono los objetos desde el elemento 2 siendo los 2 ultimos en el ejemplo"
    print "de esta manera podriamos saltar la restriccion del primer ejemplo donde teniamos que asignar n numeros de items y que coincidiera con un n nuemro de objetos"
    mis_datos2=('rul','tecnico','si','no')
    estudia, trabaja = mis_datos2[2:]
    print (mis_datos2)
    print "estudia, trabaja =mis_datos2[:2] relacion los objetos hasta el elemento 2 sin incluirlo siendo los 2 primeros en el ejemplo"
    nombre, titulo = mis_datos2[:2]
    print (mis_datos2)
    print "Ejercicio:"
    print "Prueba a crear una lista y a relacionar un par de objetos a un determinado rango de items por su indice, puedes recrear el ejemplo mostrado para expertimentarlo de propia mano"
    print "Cuando creas que has practicado los suficiente hazmelo saber escribiendo continuar(30)"
