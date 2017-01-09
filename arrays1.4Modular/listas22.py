"""ELIMINAR ELEMENTOS POR SU POSICION"""
def accion_elem2():
    print "ELIMINAR ITEMS POR SU POSICION DE INDICE[del]"
    print "creamos una lista para el ejemplo mi_listab = [1,2,3,5]"
    print "del mi_listab[3]  la posicion 3 se refiere al indice equilvaldria al elemento con valor 5 "
    mi_listab = [1,2,3,5]
    del mi_listab[3]
    print (mi_listab)
    print "podemos combinar el [del] con la forma de determinar los rangos mi_lista[0:2] del 0 hasta el 2"
    print "del mi_listab[0:2]"
    del mi_listab[0:2]
    print (mi_listab)
    print "EJERCICIO: Te animo a que crees una lista como mas te guste y pruebes  a eliminar primero items de uno en uno"
    print "Y despues repite el ejercicio eliminando items por rango de indice ,  saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(23)"
    print ""
