"""ZIP"""
def zips():
    print "[ZIP]"
    print "Parecido a UNPACKING nos permite relacionar los items por indice entre listas Me explico"
    print "creo 2 listas cabecera y dtos"
    print "cabecera = ['name','email','login'] "
    print "dtos = ['raul','drohne@gmail.com','drohne@gmail.com']"
    print "Creo union y la defino de la siguiente manera con [ZIP] y las 2 listas creadas" 
    print "union = zip(cabecera,dtos)"
    cabecera = ['name','email','login']
    dtos = ['raul','drohne@gmail.com','drohne@gmail.com']
    union = zip(cabecera,dtos)
    print "y su resultado es tal cual te lo muestro:"
    print (union)
    print ""
    print "print 'printeo con un for' "
    print "for cabecera, dtos in union: "
    print "     print (str(cabecera)+' :'+str(dtos))"
    print "printeo con un for"
    for cabecera, dtos in union:
        print (str(cabecera)+" : "+str(dtos))
    print "Cuando creas que has practicado los suficiente hazmelo saber escribiendo continuar(31)"
print ""
