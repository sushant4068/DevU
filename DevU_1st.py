# 1. Write a program to find the area of square with given side

##def area(side):
##    return side*side
##
##a=input("Enter the value for square side: ")
##Ar=str(area(a))
##print(''.join((Ar," Sq.m")))

# 2. Write a program to find the square root of a given number.
##import math
##def sq_root(num):
##    return math.sqrt(num)
##
##num=int(input("Enter a number : "))
##
##sq=sq_root(num)
##print("Sqare root of given number:",sq)
    
# 3. Write a program to print the ascii number for a given character.
##char=input("Enter a character: ")
##num=ord(char)
##print(num)

# 4. Write a program to convert decimal values into hexadecimal values.

##num=input("Enter a decimal value: ")
##print(bin(num),"in binary.")
##print(oct(num),"in octal.")
##print(hex(num),"in hexadecimal.")

# 5. Write a program to convert temperature from degree celcius to degree fahrenheite.

##def temp(num):
##    return (num+32)
##
##T=input("Enter a temperature in degree Celcius: ")
##F=temp(T)
##print("Temp in fahrenheite:",F)

# 6. Write a program to calculate Body Mass Index(BMI).

##def bmi(weight,Height):
##    return (weight/(Height*Height))
##
##wt=input("Enter a weight in Kg: ")
##ht=input("Enter a height in Meters: ")
##
##S_BMI=bmi(wt,ht)
##print("Body Mass Index is: ",S_BMI)

# 7. Write a program to find the hypoteneous of a given right angled trianle using Pythagorous Theorem.
##import math
##side1=eval(input("Enter a side1: "))
##side2=eval(input("Enter a side2: "))
##Hp=math.sqrt((side1**2)+(side2**2))
##print("Hypoteneous of a given right angled trianle: ",Hp)

# 8. Write a program to find the velocity of train.

##def velocity(D,T):
##    return (float(D/T))
##Dist=input("Enter a distance in Km :")
##Time=input("Enter time in Hr: ")
##V=velocity(Dist,Time)
##print("Velocity of train in Km/Hr: ",V)


# 9. Write a program to calculate curent using ohm's law.
##Res=eval(input("Enter a value for Resistor :"))
##Volt=eval(input("Enter a value for Voltage :"))
##Current=Volt/Res
##print("Curent using ohm's law in Ampere:",Current)

# 10. Write a program to find the energy produced by a given object of mass m, using Eienstien Formula E=mc^2

##def energy(m,c):
##    return m*(c**2)
##
##mass=input("Enter object of mass : ")
##Light_Velocity=input("Enter a velocity of light:")
##E=energy(mass,Light_Velocity)
##print(E)

# 11. Brain Teaser: The redius of a type is 8 inch. How many rotations will the type make to cover 100 kilometers.
##conv_mtr= 0.0254 * 8
##print("Convert Inches into the meters: ",conv_mtr)
##circumference =2*3.14*conv_mtr
##print("circumference of a circle: ",circumference)
##rotations=(100*1000)/circumference
##print("NO of rotations to cover 100 kilometers: ",rotations)

# 12. Print the ascii order of all characters.
##str1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
##for i in str1:
##    print(ord(i))
##list1=[chr(i) for i in range(97,123)]
##print(list1)




