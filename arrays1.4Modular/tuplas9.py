"""SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA"""
def accion_howmany_list():
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA [COUNT]"
    print "Si necesitamos saber cuentos elementos con el mismo valor tenemos podemos usar variable.count('valor') "
    print "cosas=['raton','teclado','monitor','cpu','monitor','raton','raton']"
    print "print (cosas.count('raton'))"
    print "print (cosas.count('monitor'))"
    print "(cosas.acount('teclado'))"
    cosas=['raton','teclado','monitor','cpu','monitor','raton','raton']
    print "El raton aparece "+str(cosas.count('raton'))+" veces"
    print "El monitor aparece "+str(cosas.count('monitor'))+" veces"
    print "el teclado aparece "+str(cosas.count('teclado'))+" vez"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(10)"
    print ""
