

class Student:
    ###campos definidos y finitos van separados

    names=""
    middle_surname=""
    last_surname=""
    ID=0
    run=0
    dv=""
    alternative_id=""

    def __init__(self,name,surname1,surname2,rut,ID,dv,a_id):
        self.names=name
        self.middle_surname=surname1
        self.last_surname=surname2
        self.run=rut
        self.ID=ID
        self.dv=dv
        self.alternative_id=a_id
    
rut=int(input("Ingrese su rut sin digito verificador, si no posee escribir 0: "))
if rut == 0:
    a_id=input("¿Cual es su identificación alternativa? ")
else:
    a_id=("no usa")
    dv=int(input("¿Cual es su digito verificador?, si no posee rut escribir 0: "))
ID=input("¿Cual es su ID? ")
names=input("¿cuales son sus nombres? ")
surname1=input("¿Cual es su primer apellido? ")
surname2=input("¿Cual es su segundo apellido? ")

std1=Student(names,surname1,surname2,rut,dv,ID,a_id)
print(vars(std1))
