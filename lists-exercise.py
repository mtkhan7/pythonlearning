#function for a sub sandwich order:5
#lit of toppings
topp = [
    "onions",
    "cucumber", 
    "cheese"
]

#insert method to add an item to the list at the first method
topp.insert(0,"extra cheese")

#print list topp
print(topp)

#function for a sub sandwich with 5 toppings
def sandwich_order(topp1,topp2,topp3,topp4,extra):
    print("order for a sub sandwich with 5 toppings {} {} {} {} {} enjoy your sandwich!".format(topp1,topp2,topp3,topp4,extra))
    
#call function
print(sandwich_order("onions","tomatoes","sweetcorn","cucumber","cheese"))
