def sets3():
    print "ELIMINAR ELEMENTOS  en [set.remove()]"
    print "Seguimos con la misma lista de estos ejemplos con el mismo contenido :"
    print "utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
    utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
    print "Le pasamos el set para eliminar items duplicados"
    print "utensilios=set(utensilios)"
    utensilios=set(utensilios)
    print (utensilios)
    print "Ahora elimina un item por su propio valor cuchara en caso de que coincida"
    print "utensilios.remove('cuchara') "
    utensilios.remove('cuchara')
    print (utensilios)
    print "Ahora elimina un item por su propio valor cuchillo en caso de que coincida"
    print "utensilios.remove('cuchillo') "
    utensilios.remove('cuchillo')
    print (utensilios)
    print "Ahora elimina un item por su propio valor tenedor en caso de que coincida"
    print "utensilios.remove('tenedor') "
    utensilios.remove('tenedor')
    print (utensilios)
    print "Recrea el ejemplo por ti mismo para que lo experimentes de tu propia mano"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(34)"
