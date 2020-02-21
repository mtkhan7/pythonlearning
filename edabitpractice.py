#beginner challenges edabit.

#returns first value of an array
def listnum(array):
 return array[0]
#Return the Remainder from Two Numbers
def rem(num1,num2):
    return num1 % num2
#maximum range of a triangle's third edge , the side lengths are all integers
def next_edge(side1, side2):
    return (side1 + side2) - 1
#return square of an integer
def squared(b):
	return b*b
#Return the Sum of Two Numbers
def twosum(x,y):
    return x+y 
#Convert Minutes into Seconds
def convert(minutes):
    return minutes*60

#count the legs of farmers animals
def animals(chickens,cows,pigs):
    chicken = chickens * 2
    cow = cows * 4
    pig = pigs * 4
    result = chicken + cow + pig              
    return result

#finding an area of a Triangle 
def tri_area(base, height):
    result = (base*height) / 2
    return result
print(tri_area(3,2))

#function to covert a string to number
def to_int(txt):
    result = int(txt)
    return result
print(to_int("55"))
    

#function to convert a number to string
def to_txt(num):
    result = str(num)
    return result
print(to_txt(66))   

#Find the Smallest Number in a List
def find_smallest_num(num):
    result = min(num)
    return result
print(find_smallest_num([7,7,7]))

# Source description
# The first for loop is used to display six lines of row stars.
# Then, the second for loop performs to display some columns in the heart shape.
# The "if-else" condition is performed to do an actual determination of heart shape.
# The first and second statements inside of the IF parameter can display stars as a horizontal line of the top two lines (four-star and three-star) of heart shape.
# Next, the remaining two parameters of IF expression can be displayed stars as the right to left and left to right of the heart shape.
for row in range(6):
    for col in range(7): 
       if (row==0 and col % 2 !=0)or(row==1 and col % 3==0) or(row-col==2) or(row+col==8):  
            print("*",end=" ")  
       else:  
           print(end=" ")  
    print()


#Fizz Buzz  - Loop   
for i in range(1,25):
    if(i % 3==0 and i % 5==0):
        print("FizzBuzz")
    elif(i % 3 ==0):
        print("Fizz")
    elif(i % 5==0):
        print("Buzz")