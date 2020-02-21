#challenge 1 - password check if its short then 8 character length
password = "kingkong"

if(len(password) <= 8):
    print("password is too short")
else:
    print(password)

#challenge 2 -check if the variable is divisble by 3 and 5
num = 15
if num % 3==0 or num % 5==0:
    print("this number is divisible by 3 or 5")
else: 
    print("number is not divisible by 3 or 5")

#challenge 3 - FizzBuzz
num2 = 15 
if num2 % 3==0 and num2 % 5==0: 
    print("FizzBuzz")
elif num2 % 3==0:
    print("Fizz")
elif num2 % 5==0:
    print("Buzz")
else:
    print(num2)

#challenge 4 - check if the number is a palindrome using slice operator
# str conversion

# num_int = 
# str(num_int)

check = "racecar"
if(check==check[::-1]):
    print("The string is a palindrome")
else:
    print("Not a palindrome")

#challenge 5 - check conditions with numbers
time = 7
place_of_work = "codenation"
town_home = "manchester"

if(time <= 7): 
    print("i am at home")
elif(time > 8):
    print("i am traveling from {} to {}".format(place_of_home,place_of_work))
else:
    print("i am at work")

#challenge 6 - check if the numbers are even.
num1 = 2
num2 = 4
#add variables together
num_even = 2 + 4

if(num1 % 2==0 and num2 % 2==0):
    print("{} and {} are even numbers".format(num1,num2))
else:
    print("{} and {} are not even numbers".format(num1,num2))

#challenge 7 - 

find_last_vowel = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"

last_vowel = 0
this_vowel = 0

this_vowel = find_last_vowel.rfind("a")
if this_vowel > last_vowel:
    last_vowel = this_vowel
this_vowel = find_last_vowel.rfind("e")
if this_vowel > last_vowel:
    last_vowel = this_vowel
this_vowel = find_last_vowel.rfind("i")
if this_vowel > last_vowel:
    last_vowel = this_vowel
this_vowel = find_last_vowel.rfind("o")
if this_vowel > last_vowel:
    last_vowel = this_vowel
this_vowel = find_last_vowel.rfind("u")
if this_vowel > last_vowel:
    last_vowel = this_vowel
print(last_vowel)

#challenge 8 - checks if the first letter is the same as the last letter.

word = "wow"
if(word[0] == word[-1]):
    print("true")
else:
    print("flase")




