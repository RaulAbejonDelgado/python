"""CONVERSIONES"""
def conversiones1():
    print "!!CONVERSIONES ENTRE LISTAS TUPLAS Y VICIVERSA !!"
    print "Si tenemos que modificar el contenido de una tupla sabemos que son estaticas y por ello no podemos, lo que si podemos es comvertir una tupla en lista "
    print "para manipularla como una lista y despues convertirla en una tupla"
    print "Pero como de momento solo sabemos consultar cualquier elemento y no manipular esta parte se vera al completo mas adelante:"
    print "***** convertir listas a tuplas *****"
    print "mi_lista=[1,'dos',3,'cuatro']" 
    print "mi_lista_tupla=tuple(mi_lista)"
    mi_lista=[1,'dos',3,'cuatro']
    print str(mi_lista)+" esto es una lista"
    mi_lista_tupla=tuple(mi_lista)
    print str(mi_lista_tupla)+" he volcado el contenido de mi_lista en mi_lista_tupla y tranformandolo en una tupla 'mi_lista_tupla=tuple(mi_lista)' "
    print "tranformo una tupla en una lista"
    print "mi_tupla_lista=list(mi_lista_tupla)"
    mi_tupla_lista=list(mi_lista_tupla)
    print str(mi_tupla_lista)+" he volcado el contenido de mi_lista_tupla(tupla) en mi_tupla_lista(lista) mi_tupla_lista=list(mi_lista_tupla)"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(13)"
    print ""
    print ""
