import controli
import indice
import tuplas0
def intro(user):
    print "============================================================================================="
    print "============================================================================================="
    print "============================================================================================="
    print "============================================================================================="
    print "                    TUTORIAL PYTHON SOBRE TUPLAS LISTAS "
    print "============================================================================================="
    print "============================================================================================="
    print "============================================================================================="
    print "                               (TUPLAS) [LISTAS] "
    print "Bienvenido "+str(user)
    print "Las listas,tuplas son tipos de datos complejos en lo que otros lenguajes de programacion como c o java vendrian a ser los arrays o vectores pero con particularidades que iremos explicando de forma detallada."
    print "Los tipos de datos que pueden albergar pueden ser de cualquier tipo: int,boolean,string,objetos, listas,tuplas,diccionarios "
    print "Para empezar con el tutorial escribe el tipo de dato por el cual quieres investigar, las opciones son: tuplas,listas o diccionarios etc.."
    print "Mi recomendacion es que empieces por las tuplas, continues con las listas y termines con los diccionarios"
    print "Por donde vas a empezar ?? typea tuplas, listas o indice "
    nombre = raw_input()
    print (nombre)
    if nombre == 'tuplas' :
        tuplas0.tuplas()
    if nombre == 'listas' :
        arrays.accion_listas()
    if nombre == 'indice':
        indice.indice()
    
   
