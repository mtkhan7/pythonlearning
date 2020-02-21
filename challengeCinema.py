#check age of cinema goers and print out ticket price

age = int(input('how old are you: '))

if(age < 18):
    print("child ticket £8")
elif(age >= 60):
    print("senior ticket £7.50")
else:
    print("Adult ticket £10.95")

