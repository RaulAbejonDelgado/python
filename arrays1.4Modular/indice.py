import intro
import logic
def indice(continuar,user):
    print "ACCIONES SOBRE LISTAS Y TUPLAS"
    print "CONTENIDO:comando a teclear"
    print "INDEX:continuar('i')"
    print "TUPLAS:continuar(0)"
    print "ACCESO A LOS ITEMS POR EL INDICE:continuar(1)"
    print "TUPLAS 1 DIMENSIONES RANGO POR EL INDICE :continuar(2)"
    print "TUPLAS 2 DIMENSIONES ACCESO ELEMENTOS POR INDICE:continuar(3)"
    print "AHORA CON LOS 3 ARGUMENTOS:continuar(4)"
    print "CREAR LISTAS/TUPLAS CON RANGE:continuar(5)"
    print "ENUMERAR EL INDICE[ENUMERATE]:continuar(6)"
    print "ENUMERAR UNA LISTA POR EL INDICE CON [ENUMERATE]:continuar(7)"
    print "OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]:continuar(8)"
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA [COUNT]:continuar(9)"
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA TUPLA [COUNT]:continuar(10)"
    print "SABER LA CANTIDAD DE ELEMENTOS DE UNA LISTA/TUPLA [LEN]:continuar(11)"
    print "CONVERSIONES ENTRE LISTAS TUPLAS Y VICIVERSA:continuar(12)"
    print "RESUMEN E INDICE:continuar(13)"
    print "LISTAS continuar:(14)"
    print "ORDENADAR LISTAS INT[SORT]:continuar(15)"
    print "ORDENADAR LISTAS DE STRING CON [SORT]:continuar(16)"
    print "INVERTIR LISTAS [REVERSER]:continuar(17)"
    print "ASIGNACION DE 1 ELEMENTO A LA DERECHA [APPEND]:continuar(18)"
    print "ASIGNACION DE VARIOS VALORES POR SU DERECHA [EXTEND]:continuar (19)"
    print "ASIGNACION DE ELEMENTOS EN UNA POSICION DETERMINADA:[INSERT] continuar(20)"
    print "ELIMINAR ITEMS POR SU PROPIO VALOR:[REMOVE]:continuar(21)"
    print "ELIMINAR ITEMS POR SU POSICION[DEL]:continuar(22"
    print "ELIMINAR ITEMS POR SU POSICION RETORNANDO EL ITEM ELIMINADO[POP]:continuar(23)"
    print "ELIMINAR TODOS LOS ELEMENTOS CON LA FUNCION [DEL]:continuar(24)"
    print "MODIFICAR ITEMS POR SU POSICION DE INDICE:continuar(25)"
    print "MODIFICAR ITEMS POR SU POSICION DE INDICE EN UN RANGO DE INDICES:continuar(26)"
    print "RESUMEN LISTAS continuar(27)"
    print "ASOCIAR OBJETOS A ELEMENTOS DE UNA LISTA/TUPLA continuar(28)"
    print "ASOCIAR OBJETOS A ELEMENTOS DE UNA LISTA/TUPLA POR INDICE DE RANGO continuar(29)"
    print "ZIP continuar(30)"
    print "SETS continuar(31)"
    print "ANADIR ELEMENTOS EN SET.ADDcontinuar (32)"
    print "ELIMINAR ELEMENTOS SET.REMOVE continuar(33)"
    print "BUSCAR ELEMENTOS EN SET continuar (34)"
    print "A que opcion quieres ir ??"
    continuar= raw_input()
    continuar = int(continuar)
    logic.continuar(continuar,user)