def accion_enumerar_listas():
    print "ENUMERAR UNA LISTA POR EL INDICE CON [ENUMERATE]"
    print "Vamos dominando las tuplas a si que el siguiente ejemplo sera una lista"
    print "las listas se recorren de la misma forma que las tuplas"       
    print "las listas se definen ejemplo mi_lista=['1',dos,'3',cuatro]"
    print "las diferencias entre las tuplas en deficion tupla=() vs lista=[]"
    print "las listas son dinamicas a diferencia de las tuplas y eso nos abre unas funcionalidades extra que iremos viendo mas adelante"
    print "las listas al ser dinamicas, podemos agregar,borrar,modificar elementos etc que no se pueden hacer con las tuplas"
    print "Ahora vamos a repetir el ejercicio pero tomando contacto con las listas asique puedes guiarte por el siguiente ejemplo y veras la similitud/diferencias con las tuplas"
    print "creo una lista con rango 20 con mi_liston = range(20)"
    mi_liston = range(20)
    print (mi_liston)
    mi_liston = list(enumerate(mi_liston))
    print "mi_liston = list(enumerate(mi_liston))"
    print (mi_liston)
    print "Como podras observar se comparta de la misma manera, y apreciaras que ya no va entre parentesis, si no entre corchetes y cuando usamos enumerate tambien le indicamos si es una tuple o una list"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(8)"
print ""
