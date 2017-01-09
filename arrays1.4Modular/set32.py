def sets2():
    print "AnADIR ELEMENTOS en [set.add()]"
    print "para el ejemplo usamos el mismo ejemplo utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
    print "Eliminamos los items repetidos:"
    print "utensilios = set(utensilios) "
    utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
    print (utensilios)
    utensilios = set(utensilios)
    print "nos aseguramos de que utensilios es un set para poder usar .add"
    print " utensilios = set(utensilios)"
    print "utensilios.add('hola') "
    utensilios.add('hola')
    print (utensilios)
    print "utensilios.add(1) "
    utensilios.add(1)
    print (utensilios)
    print "utensilios.add('asd') "
    utensilios.add('asd')
    print (utensilios)
    print "comprobamos que al anadir un elemento lo deja sin orden aparante"
    print "Practica un poco emulando el ejemplo mostrado"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(33)"
    print " "
