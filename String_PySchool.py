##Write the function countA(word) that takes in a word as argument and returns the number of 'a' in that word.
##def counter(str1):
##    count1=str1.count('a')
##    print(count1)
##counter("aaple")

#Write the function countLetter(word, letter) that takes in a word and a letter as arguments and returns the number of occurrence of that letter in the word
##def countletter(word,letter):
##    count1=word.count(letter)
##    print(count1)
##countletter("Analog Devices","n")

##Write a function removeLetter(word, letter) that takes in a word and a letter as arguments and
##remove all the occurrence of that particular letter from the word. The function will returns the remaining leters in the word.
##def removeletter(word,letter):
##    remove1=word.replace(letter,'')
##    print(remove1)
##removeletter("sushant",'s')


##Write the function changeCase(word) that changes the case of all the letters in a word and returns the new word.
##def Swapcase(str1):
##    print(str1.swapcase())
##Swapcase("Analog DEVicEs")

##Write the function search(word, substring) that takes in a word and a substring as arguments and
##returns the position (0 indexed) of the substring if it is found in the word. The function returns -1 if the substring is not found.
##def substring(word,substring):
##    V=word.find(substring)
##    print(V)
##substring("google",'a')

##A string contains a sequence of characters. Elements within a string can be accessed using index that starts from 0.
##Write the function getChar(word, pos) that takes in a word and a number as argument and returns the character at that position.
##def substring(word,pos):
##    print(word[pos])
##substring("google",5)

##Write a function countVowels(word) that takes in a word as an argument
##and returns the number of vowels ('a', 'e', 'i', 'o', 'u') in the word.
##def Vowels(word):
##    count=0
##    for i in word:
##        if i in "aeiouAEIOU":
##            print(i)
##            count+=1
##    print(count)
##Vowels("India")

##Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized.

##def CapitaliseVowels(word):
##    for i in word:
##        if i in "aeiou":
##            pos=word.index(i.upper())
##            print(pos)
##            
##            
##    print(word)
##CapitaliseVowels("india")

##Write the function startEndVowels(word) that returns True if the word starts and ends with vowels.
##def startEndVowels(word):
##    len1=len(word)
##    len2=len1-1
##    if(word[0] in "aeiouAEIOU" and
##       word[len2] in "aeiouAEIOU"):
##        print("TRUE")
##    else:
##        print("FALSE")
##
##    print(word[::-1])
##startEndVowels("InDia")

##Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u')
##in a word and returns the remaining letters in the word.
##def removeVowels(word):
##    str1=""
##    for i in word:
##        if i in "aeiouAEIOU":
##            continue
##        str1+=i
##    print(str1)                
##removeVowels("India")

##Write the function startWithVowel(word) that takes in a word as argument and
##returns a substring that starts with the first vowel found in the word.
##
##def startWithVowel(word):
##    pos=0
##    for i in word:
##        if i in "aeiouAEIOU":
##            pos=word.find(i)
##            break
##        else:
##            print("NO VOWELS")
##            break
##    print(word[pos:])
##startWithVowel("appleIphone")

##Write the function getCommonLetters(word1, word2) that takes in two words as arguments and returns a new string that contains
##letters found in both string. Ignore repeated letters and sort the result in alphabetical order.
##def getCommonLetters(word1, word2):
##    list1=[]
##    for i in word1:
##        if i in word2:
##            list1.append(i)
##    print(''.join(sorted(list1)))
##    
##getCommonLetters("microsoft","delsft")

##Write a function mirrorText(word1, word2) that takes in 2 words as
##arguments and returns a new word in the following order: word1word2word2word1.
##def mirrorText(word1, word2):
##    str2=""
##    str2=word1+word2+word2+word1
##    print(str2)
##mirrorText("Ray","Ban")

##Write a function echoWord(word) that takes in a word as arguments
##and returns a word that repeats itself based on the number of letter in the word.
##def echoWord(word):
##    len1=len(word)
##    print(word*len1)
##echoWord("Analog")

##Write a function rightJustify(word) that takes in a word as argument and
##return a word with leading spaces so that the last letter of the word is in column 50 of the display.
##def rightJustify(word):
##    print(word.rjust(50))
##rightJustify("Virat")

##A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either direction.
##Write a function that determines whether the given word or number is a palindrome.

##def palindrome(word):
##    if(word==word[::-1]):
##        print("Palindrome")
##    else:
##        print("Not Palindrome")
##palindrome("101")

##Write a function isInAlphabeticalOrder(word) that takes in a word as argument and returns True if the word contains letters that are arranged in alphabetical order.
##For example, the letter 'c' should not appear before the letter 'a'.
##def isInAlphabeticalOrder(word): 
##    str2="".join(sorted(word))
##    if str2 == word:
##	    print("True")
##    else:
##	    print("False")
##isInAlphabeticalOrder("app")

##Write a function isAllLettersUsed(word, required) that takes in a word as the first argument
##and returns True if the word contains all the letters found in the second argument.
##def isAllLettersUsed(word, required):
##    for i in word:
##        if i in required:
##            return True
##        else:
##            return False
##T=isAllLettersUsed('learning python', 'google')
##print(T)

##Write a function splitWord(word, numOfChar) that takes in a word and a number as arguments. The function will split the word into smaller segments with
##each segment containing the number of letter specified in the numOfChar argument.
##These segments are stored and returned in a list.

