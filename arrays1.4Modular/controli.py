import intro
import logic
import indice
def crearuser(user):
    txt=open(str(user)+'.txt','a')
    txt.close()
    saberpaso(user)
def saberpaso(user):
    txt=open(str(user)+'.txt','r')
    lineas=txt.readline()
    print "La ultima consulta realizada fue en la leccion :"+str(lineas)
    txt.close()
    if lineas == '' :
        intro.intro(user)
    else:
        continu(user)
    
def continu(user):
    print "quieres continuar desde el ultimo punto ?? s = si , n = no"
    con= raw_input()
    if con == 's' :
        ultimo=open(str(user)+'.txt','r')
        ulti=ultimo.readline()
        ultimo.close()
        logic.continuar(int(ulti),user)
    else:
        ultimo=open(str(user)+'.txt','r')
        ulti=ultimo.readline()
        ultimo.close()
        continuar= ulti
        indice.indice(continuar,user)
def grabartxt(user, continuar):
    txt=open(str(user)+'.txt','w')
    txt.write(str(continuar)+'\n')
