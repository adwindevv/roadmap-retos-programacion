#types of the operators
number1= 30
number2= 8
#arithmetical operators
print("Arithmetical operators")
print("Addition: ",number1+number2) #addition
print("Substraction: ",number1-number2) #substraction
print("Multiplication: ",number1*number2)# multiplication
print("Division: ",number1/number2)# division
print("Floor Division: ",number1//number2) # number integer division
print("Modulus: ",number1%number2) # modulus
print("Exponent: ",number1**number2) # exponentiation
#comparison operators
print("\nComparison Operators")
print("Equal: ",number1==number2) # equal
print("Not Equal: ",number1!=number2) # different
print("Greater than: ",number1>number2) # mayor que
print("Less than: ",number1<number2) # menor que 
#logical operators
a=True
b=True
print("\nLogical Operators")
print("AND: ",a and b)#return True if both are True
print("OR: ",a or b)#return true if one of the operands is true
print("NOT:",not b) #inverts the value of the operand
#assignment operators
print("\nAssignment operators")
number1=52
print(number1)
number1+=3
print(number1)
number1-=4
print(number1)
number1*=2
print(number1)
number1/=4
print(number1)
number1%=3
print(number1)
number1**=2
print(number1)
number1//=4
print(number1)
"""
Estructuras 
de 
Control
"""

#Condicionales
my_string = "AdwinDev"

if my_string == "Edwin Adair":
    print("Tu nombre es correcto")
elif my_string == "AdwinDev":
    print("Tu nombre de programador")
else:
    print("No contiene ningun nombre especificado")

#Iterativas

for i in range(11):
    print(i)

i=0
while i<=10:
    print(i)
    i+=1

#Manejo de excepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Vuelve a intentarlo")

print("\nEjercicio")
for numero in range (10,56):
    if numero %2 ==0:
        if numero != 16:
            if numero % 3==0:
                print(numero)
