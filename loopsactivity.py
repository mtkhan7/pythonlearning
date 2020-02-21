#activity #1 - create an array that lists favourite films up to 5 elements
fav_movies = [
    "harry potter",
    "james bond",
    "the hobbit",
    "irishmen",
    "lion king"
    ]
#adding 2 more movies using the extend method
addfav_movies = [
       "the martian",
       "ET"
       ]
fav_movies.extend(addfav_movies)
fav_movies.insert(1,"batman")
#loop to print through movies
for i in fav_movies:
    print(i)
    
#loop activity #2

#list of 4 movies
movies_fav = [
    "james bond",
    "the hobbit",
    "irishmen",
    "ghostbusters"
]


#loop to show each film in the array
for indexmovie in movies_fav:
    print(indexmovie)
    
    
#function to check if the 3rd movie is ghostbusters
def check_movie(film):
    if(movies_fav[3] == "ghostbusters"):
        print("yes you can watch ghostbusters its at #3")
    else:
        print("boohooo, we want ghostbusters")

#call movie checker    
check_movie("film")