"""printeo de un rango de direcciones"""
def acciones_tuplas2_1():
    print "TUPLAS 2 DIMENSIONES ACCESO ELEMENTOS"
    print "las tuplas/listas pueden tener varias dimensiones(mas de 1 tupla/lista/dic o combinacion de ellas) ejemplo mi_tupla2=(('uno', 2 ,'tres',4),('cinco',6,'siete',8))"
    mi_tupla2=('uno', 2 ,'tres',4),('cinco',6,'siete',8)
    print str(mi_tupla2)+"es una tupla bidimensional una tupla compuesta de 2 tuplas"
    print "Al tener 2 dimensiones este ejemplo, python trata la tupla/lista misma manera pero de forma conjunta,si antes hablabamos de una dimension trataba los elementos de ese conjunto, ahora al tener varios tuplas/listas se comportara de la misma manera para esos conjunto y si queremos tratar una dimension deberemos hacerlo de forma independiente"
    print "EJEMPLO1 :"
    print "mi_tupla2[0:0]= "+ str(mi_tupla2[0:0])+" desde indice de dimension 0 hasta indice de dimension 0 sin incluirla no encuentra nada pero sabemos si se trata de una lista o tupla en este caso es tupla"   
    print "mi_tupla2[0:1]= "+ str(mi_tupla2[0:1])+" selecionamos desde indice de dimension 0 hasta indice de dimension 1 sin ser incluido"
    print "mi_tupla2[1:0]= "+ str(mi_tupla2[1:0])+" esto no tendria sentido ya que le decimos que mire desde la 1 hasta la 0 sin incluir 0 "
    print "mi_tupla2[1:2]= "+ str(mi_tupla2[1:2])+" selecionamos desde indice de dimension 1 hasta el indice de dimension 2 sin ser incluido"
    print "mi_tupla2[0:2]= "+ str(mi_tupla2[0:2])+" selecionamos desde indice de dimension 0 hasta la indice de dimension 2"
    print "EJERCICIO_1=EJEMPLO1"
    print "EJEMPLO 2:"
    print "Entonces si queremos tratar cada elemento de una tupla/lista compuesta de otras listas tuplas deberemos hacerlo de forma individual"
    print "primero tendriamos que averiguar que elemento queremos tratar , con el ejemplo 1 hemos visto como hacerlo"
    print "una vez que tengamos claro cuales son las posiciones de los indices que queremos 'deslogsar' podemos guardarlo en una variable y tratarlos datos por elemento individual"
    print "primer_elemento=mi_tupla2[0:1]"
    print "segundo_elemento=mi_tupla2[1:2]"
    primer_elemento=mi_tupla2[0:1]
    segundo_elemento=mi_tupla2[1:2]
    print "El primer elemento de mi_tupla2 esta en el indice 0 lo he guardado en primer_elemento="+str(primer_elemento)
    print "El primer segundo elemento de mi_tupla2 esta en el indice 1 lo he guardado en segundo_elemento= "+str(segundo_elemento)
    print ""
    
    print "EJERCICIO_2=EJEMPLO2"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(4)"
