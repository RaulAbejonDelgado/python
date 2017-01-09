"""INVERTIR LISTAS """
def accion_invertir():
    print "INVERTIR LISTAS [REVERSER]"
    print "Acabamos de ver sort que nos ordena las listas alfabeticamente con strings o de < las listas numericas"
    print "con variable.reverse consegimos alterar el estado original de la lista de forma inversa"
    print "ejemplo: lista=(2,1,3)"
    print "lista.reverse"
    print "esta accion nos invierte el contenido de la lista quedando de tal manera : (3,1,2)"
    print "EJERCICIO1: EJEMPLO"
    print "creamos una lista letras=['g','w','x','j','v','a'] "
    print "letras"
    print "letras.reverse()"
    print "letras"
    letras=['g','w','x','j','v','a']
    print (letras)
    letras.reverse()
    print (letras)
    print "EJERCICIO2:EJEMPLO"
    print "como ya conocemos el comando sort y el comando reverse podemos usarlo para ordenar una lista alfabeticamente y con reverse tener la lista ordenada inversamente"
    print "Comprobamos que altera inversamente el contenido del letras si probamos a ordenarlo primero y despues invertirlo"
    print "letras.sort()"
    print "letras.reverse()"
    print "letras"
    letras.sort()
    letras.reverse()
    print (letras)
    print ""
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(18)"
