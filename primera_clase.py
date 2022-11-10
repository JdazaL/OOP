##hacer una clase que cree fracciones mediante un constructor
##operaciones: suma-resta-multiplicacion-division

def mcd(a , b):
    if a == 0:
        return b
    else:
        return  mcd (b % a , a)

class fraction  :
    def __init__(self):
        x = int(input('Numerador: '))
        y = int(input('Denominador: '))
        self.num = x 
        self.den = y 

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __addi__(self,self2):
        if self.den == self2.den:
            self.new_num = self.num + self2.num
            self.new_den = self.den
            gcd = mcd(self.new_num,self.new_den)
            return str(self.new_num//gcd) + '/' + str(self.new_den//gcd)          
        else:
            self.new_num = self.num * self2.den + self.den * self2.num
            self.new_den = self.den * self2.den
            gcd = mcd(self.new_num,self.new_den)
            return str(self.new_num//gcd) + '/' + str(self.new_den//gcd)


    def __subs__(self,self2):
        if self.den == self2.den:
            self.new_num = self.num - self2.num
            self.new_den = self.den
            gcd = mcd(self.new_num,self.new_den)
            return str(self.new_num//gcd) + '/' + str(self.new_den//gcd)            
        else:    
            self.new_num = self.num * self2.den - self.den * self2.num
            self.new_den = self.den * self2.den
            gcd = mcd(self.new_num,self.new_den)
            return str(self.new_num//gcd) + '/' + str(self.new_den//gcd)
            ##si el nro restando es mayor el signo quedara en el denominador, no pude encontrar el porque.
    
    def __mult__(self,self2):
        self.new_num = self.num * self2.num
        self.new_den = self.den * self2.den
        return str(self.new_num) + '/' + str(self.new_den)   

    def __divs__(self,self2):
        self.new_num = self.num * self2.den
        self.new_den = self.den * self2.num
        return str(self.new_num) + '/' + str(self.new_den) 

frc1 = fraction()
print(frc1)
frc2 = fraction()
print(frc2)

print('La suma de las fracciones es: ' + frc1.__addi__(frc2))

print('La resta de las fracciones es: ' + frc1.__subs__(frc2))

print('La multiplicacion de las fracciones es: ' + frc1.__mult__(frc2))

print('La division de las fracciones es: ' + frc1.__divs__(frc2))
    