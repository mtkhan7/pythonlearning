#activity 1 : prints out name,age and favourite color
name = "Muhammad Khan"
age = "32"
favourite_color = "white"

print("My name is {} , i am {} years old and my favourite color is {} ".format(name,age,favourite_color))

#activity 2 : stores what i had for breakfast today, lunch and dinner and 
# what i will have tomorrow and print the output
breakfast = "weetabix"
lunch = "sandwich"
dinner = "roast chicken"
print("Today I had for breakfast is {}, for lunch I had a {}, and for dinner I will have {}".format(breakfast,lunch,dinner))

#update variables and print
breakfast ="tea and toast"
lunch = "sushi"
dinner = "lentils and bread"
print("Tomrrow I will have for breakfast is {}, for lunch will be {}, and for dinner I will have {}".format(breakfast,lunch,dinner))

#activity 3: Create a program that calculate the number of days from today to your birth date and print this out.

#print the number of days from today to your birthday
#check this code and see
# todays_date = datetime.date.today()
# my_birthday = datetime.date(20, 10, 20)
# days_to_birthday = my_birthday - todays_date
# print(days_to_birthday)

from datetime import date
birth_date = date(1987, 10, 2)
today_date = date(2020, 2, 4)
days_old = today_date - birth_date
print ("You are {} days old.".format(days_old.days))



#activity 4: