#functions are a small program
#function syntax python
def press_grind_beanss():
    print("Grinding for 20 seconds")

press_grind_beanss()

#function - if coffee is grinding true or false
coffee_is_grinding = False

def press_grind_beans():
    if coffee_is_grinding:
        print("The Coffee is grinding")
    else:
        print("The coffee is not grinding")
    
#call function
press_grind_beans()

#function parameters
def cash_withdrawal(amount,accnum):
    print("withdrawing {} from account {}".format(amount,accnum))
    
#call function with values
cash_withdrawal(300,200)

#create a function that takes two parameteres for a coffee order size and type of drink
def cofee_order(size,type_of_drink):
    print("i would like a {} {} please".format(size,type_of_drink))

#call function with size and type of drink
cofee_order("large","cappuccino")
cofee_order("small","latte")

#adding function with two parameters - return 
def add_up(num1,num2):
    return num1+num2
add_up(7,3)
print(add_up(2,5))

#celsius to fahrenheit converter 
def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)
def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32
print("The temperature is {}F".format(get_fahrenheit(10)))

#function activity 1 - pizza challenge adding two parameters
def take_order(topping,size):
    print("Pizza with {} topping and {} size".format(topping,size))
#calling function with parameters
take_order("pineapple","medium")

