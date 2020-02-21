#lists in python #arrays in javascript

songs_order = [
    "songs1 - Faded",
    "songs2 - Hakuna Matata",
    "songs3 - Alone"
    ]
print(songs_order)

#accessing a list using brackets.
print(songs_order[2])

#updating a list
songs_order[1] = "songs2 - World"
print(songs_order)

#len method - counts the number of items of the list
print(len(songs_order))

#append method - adding an item to the end of the list / using .dot notation /.append 
songs_order.append("songs4 - Alan walker")
print(songs_order)

#pop method - pop method removes the an item from the end of the list/ doesnt take any parameters
songs_order.pop()
print(songs_order)

#lists activity #1
fav_website = [
    "freecodecamp",
    "google",
    "youtube"
]
#adding another value to the web list
fav_website.append("instagram")
#using extend method with square brackets to add multiple values
fav_website.extend(["facebook","twitter"])
#print the web list to check
print(fav_website)
#removing the last item from the web list.
fav_website.pop()
#printing after removing the last item from the list
print(fav_website)

#lists activity #2
animals_list = [
    "cat",
    "dog",
    "tiger",
    "elephant"
]

# adding another item to end of the animal list
animals_list.append("lion")
print(animals_list)
# using extend method to add multiple items in the list or can put two lists together.
animals_list.extend(["hippo","monkey","jaguar"])
print(animals_list)
# remove() method removes the first occurance of specified element from the list
animals_list.remove("hippo")
print(animals_list)
# reverse method reverses the items in the list
animals_list.reverse()
print(animals_list)
# The sort() method sorts the elements of a given list in a specific order - numers firsts - alphabaticaly second Ascending or Descending.
animals_list.sort()
print(animals_list)
# count method returns how many times the element is repeated.
print(animals_list.count("dog"))
# Sorting list in descending  order
animals_list.sort(reverse=True)
print(animals_list)
      