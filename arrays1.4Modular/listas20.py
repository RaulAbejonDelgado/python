"""INSERTAR ELEMENTOS EN LA POSICION DETERMINADA"""
def accion_insert1():
    print "INSERTAR ELEMENTOS POR SU INDICE CON EL METODO [insert]:"
    print "Creamos una lista para el ejemplo : mi_listab=['a','b','c']"
    mi_listab=['a','b','c']
    print "Le digo que quiero agregar la palabra letras en el indice 0 "
    print "mi_listab.insert(0,'letras')"
    mi_listab.insert(0,'letras')
    print (mi_listab)
    print "Ahora repito el ejercicio pero con numeros defino la misma lista con numeros:"
    print "mi_listab=[1,2,3,5]"
    print "mi_listab.insert(3,'4') coloco el elmento numero 4 en la posicion de indice numero 3 ya que empienza en 0"
    mi_listab = [1,2,3,5]
    mi_listab.insert(3,'4')
    print (mi_listab)
    print "EJERCICIO: crea una lista numerica, de texto o mixta e intenta insertar items en la posicion que quieras para comprobarlo, saca tus propias conclusiones"
    print ""
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(21)"
