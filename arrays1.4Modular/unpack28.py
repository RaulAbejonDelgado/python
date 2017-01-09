"""DESEMPAQUETAMIENTO O UNPACKING"""
def unpack():
    print "RELACIONAR OBJETOS CON ITEMS DE UNA LISTA / TUPLA"
    print "Podemos tener una serie de objetos(variables en este caso) y relacionar estos con los items de una lista"
    print "Ejemplo:"
    print "Creamos una tupla con 4 items mis_datos=('Raul','Abejon','30','soltero)"
    print "y creo 4 varibles y los inicializo con la lista de la siguiente manera "
    print "nombre, apellido, edad,estado=mis_datos"
    mis_datos=('Raul','Abejon','30','soltero')
    nombre, apellido, edad, estado=mis_datos
    print "Ahora al llamar al objeto me deberia mostrar el item asociado a la tupla"
    print (nombre)
    print (apellido)
    print (edad)
    print (estado)
    print "Para que sea efectivo el numero de valores ha de coincidir con el numero de objetos"
    print "Si la lista o tupla continue n numeros de items la cantidad de objetos a relacionar deben coincidir en n numero de objetos"
    print "Enumero los elementos de la tupla para comprobar que pese a estar asociado un item a un objeto sigue manteniendo la coherencia de sus indices:"
    mis_datos=tuple(enumerate(mis_datos))
    print (mis_datos)
    print ""
    for i in mis_datos:
        print (i)
    print "EJERCICIO:"
    print "Primero recrea este ejemplo para que veas el error que nos muestra por pantalla:"
    print "tupla=('pepe','coche','casa')"
    print "nombre,posesion1=tupla"
    print "Como puedes comprar si hacemos eso nos devuelve un error diciendo que no coinciden los argumentos con los objetos:"
    print "Ahora crea una tupla o lista y asociala unos objetos y depues typea el nombre de dichos objetos"
    print "haz la prueba guiandote en los ejemplos mostrados, para que saques tu propia conclusion"
    print "Cuando creas que has practicado los suficiente hazmelo saber escribiendo continuar(29)"
