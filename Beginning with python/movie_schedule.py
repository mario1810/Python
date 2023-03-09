current_movies={"Rudolph":"11:00am",
                "Frosty":"10:00am",
                "Christmas":"7:00am",}

current_movies["The Grinch"]="11:00"
for key in current_movies:
    print(key)
movie=input("What movie would you like to showtime for?\n")
showtime=current_movies.get(movie);
if(showtime== None)
