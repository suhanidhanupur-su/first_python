#print
print("Suhani kumari" ,  "Hello Everyone")
print("Age 18")
print("35+23")
print(35+23)

#variable=value
name = "Suhani kumari"
age = 18
price = 50.99
print(name, age, price)
print("My Name Is =" , name)
print("my Age Is =",age)
print("price =",price)

#"""print sum""" artmatic opration
a = 2
b = 4
sum = a+b
sum1 = a*b
sum3 = a**b #a^b
sum4 = a % b #reminders
print(sum , sum1 , sum3 , sum4)

#relational opration

a = 50 
b = 20

print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#assignment oprator

a = 30
b = 20
c = 30
d = 40

a += 10
b -= 20
c /= 3
d *= 2

print(a , b , c , d)

#logical oprators

print(not False)
print(not True)

val1 = True
val2 = False

print("and oprator :" , val1 and val2)

print("or oprator :" , val1 or val2)

#type conversion

a = 400
b = 300.44

sum = a+b #400.00 + 300.44 a + b

#type casssting

a,b = 200,"200"
c = int(b)

print(a+c)

#input

name = input("enter your name:", )
age = int(input("enter your age",))
No = int (input("Enter Mobile No",))
print("WELCOME ", name , age , No)
#string

str1 = 'Suhani kumari'
str2 = "Suhani kumari"
str3 = """Suhani kumari"""

print(str1 + " " + str2)
print(len(str1 + str2 + str3)) #length

print(str1[0 :len (str1)]) #slicing

print(str1.endswith("ma")) #checking

print(str2.capitalize()) #capitalize

print(str3.replace("Suhani" , "Isha")) #Replacing

print(str1.find('v')) 

print(str2.count('a'))

#conditional Statment

a = int(input("First Number "))
b = int(input("Second No "))

s = (input("Choose Simble "))

if(s == "*"):
    print(a*b)

elif(s == "+"):
    print(a+b)

elif(s == "-"):
    print(a-b)

elif(s == "/"):
    print(a/b)

elif(s == "%"):
    print((a/b)*100)

else:
    print("Unknown Simble")

mark =  int(input("Marks --> ",  )) 

if(mark >= 90):
    Mark = "A"
elif(mark >= 80 and mark < 90 ):
    mark = "B"
elif(mark >= 70 and mark <= 80):
    mark = "C"
elif(mark <= 69):
    mark = "D"

print(mark)