#conditionals if elif else statements
#logicial operator - == equal to
# != not equal to operator

music = "rock"

if music == "rock":
    print("oh no its rock n roll")
elif music == "no music":
    print("peace and quiet")
else: 
    print("what music is playing?")

#comparison operators - 
# > greater than
# >= greater than equal to
# < less than
# <= less than equal to

#age checker / conditional 
age = 18
country = "UK"

if age > 17 and country =="UK":
    print("yes you are old enough and you are from the UK")
else:
    print("you are not old enough and you are not from the UK ")
 
#weather checker comparison , #using (and - &&) both conditions have to be met.
place ="Manc"
weather ="Cloudy"

if place =="Manc" and weather == "Sunny":
    print("check again")
elif place =="Manc" and weather =="Rain":
    print("Obz")
else: 
    print("check weather again.")

#using (or - || operator ) one condition needs to be true.
day ="Saturday"

if day =="Saturday" or day=="Sunday":
    print(day)
else:
    print("its not" + day)
