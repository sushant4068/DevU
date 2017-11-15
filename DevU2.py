# Example: Equilateral triangle
##sideA, sideB, sideC = -3,-3,-3
##if sideA == sideB == sideC and sideA>0:
##    print("It is equilateral")
##else:
##    print("Not an equilateral")
    
# Same code with ternary operatot
##print("It is equilateral") if sideA == sideB == sideC and sideA>0 else print("Not an equilateral")

##1.Write a program to find if a given number is Even or Odd.

##def odd_even(num):
##    if (num & 1):
##        print("Given number is odd")
##    else:
##        print("Given number is even")
##
##odd_even(10)

##2. Write a program to check if a given number is divisible by 7 or 11

##def seven_elev(num):
##    if((num %7==0) or (num %11==0)):
##        print("Given number is divisible by 7 or 11")
##    else:
##         print("Given number is NOT divisible by 7 or 11")
##
##num=eval(input("Enter a number:"))
##seven_elev(num)

##Write a program to find the largest of three numbers.

##def largest(a,b,c):
##    if(a>b and a>c):
##        print(a)
##    elif(b>a and b>c):
##        print(b)
##    else:
##        print(c)
##    print(a) if a>b & a>c  print(b) if (b>c & b>a)  else print(c)
##
##largest(10,12,20)

##Write a program to print numbers from 1 to 100,
##but replace the number with "fizz" if it is divisible by 3 and by "buzz"
##if it is divisible by 4 and "fizzbuzz" if it is divisible by both.
##list1=[]
##for i in range(1,101):
##    list1.append(i)
##print(list1)
##for i in range(0,100):    
##    if(list1[i]%3==0 and list1[i]%4==0):
##        list1[i]="FizzBuzz"
##    elif(list1[i]%3==0):
##        list1[i]="Fizz"
##    elif(list1[i]%5==0):
##        list1[i]="Buzz"
##print(list1)

##Write a program to find the count of vowels in a given country name.
##count=0
##def vowel_count(str1):
##    global count
##    for i in str1:
##        if i in "aeiouAEIOU":
##            count=count+1
##    print(count)
##str1=input("Enter name of the country:")
##vowel_count(str1)

##Write a program to delete vowels from a given string.
##def vowel_del(str1):
##    str2=""
##    for i in str1:
##        if i in "aeiouAEIOU":
##            continue
##        str2 +=i
##    print(str2)
##str1=input("Enter name of the country:")
##vowel_del(str1)

##Write a program to break the string on first vowel
##def vowel_del(str1):
##    str2=""
##    for i in str1:
##        if i in "aeiouAEIOU":
##            break
##        str2 +=i
##    print(str2)
##str1=input("Enter the string:")
##vowel_del(str1)

