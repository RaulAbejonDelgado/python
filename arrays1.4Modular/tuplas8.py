"""OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]"""
def accion_index():
    print "OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]"
    print "Si conocemos el valor especifico podemos consultar su numero de posicion dentro de la tupla/lista mediante variable.index('valor')"
    print "EJEMPLO EN LISTA:"
    print " creo lista nombres=['juan','pepe','kiko','jose']"
    print "typea nombres.index('pepe')"
    nombres=['juan','pepe','kiko','jose']
    print "esta en la posicion: "+str(nombres.index('pepe'))
    print "EJEMPLO EN TUPLA"
    print " creo tuplas nombres=('juan','pepe','kiko','jose')"
    print "typea nombres.index('kiko')"
    nombres=('juan','pepe','kiko','jose')
    print "esta en la posicion: "+str(nombres.index('kiko'))
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(9)"
print ""
