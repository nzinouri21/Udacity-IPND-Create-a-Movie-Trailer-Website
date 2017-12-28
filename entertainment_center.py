#In this file, we store details of movies to display them on a website.

import media
import fresh_tomatoes


#It is good practice to call your class definition in one file
#and to call/use your class in a different file.
#This file is to use clasa Movie from file media and to create multiple
#instances of Movie

toy_story = media.Movie("Toy Story",
                        "Joss Whedon, Joel Cohen, Andrew Stanton, and Alec Sokolow",
                        "November 22, 1995",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar",
                        "James Cameron",
                        "December 18, 2009",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")



inception = media.Movie("Inception",
                        "Christopher Nolan",
                        "July 13, 2010",
                        "A thief with the ability to enter people's dreams and steal their secrets.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")



ratatouille = media.Movie("Ratatouille",
                        "Brad Bird, Kathy Greenberg, Bob Peterson, and Emily Cook",
                        "June 29, 2007",
                        "A rat in Paris that wants to become a chef!",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")


the_big_sick = media.Movie("The big sick",
                        "Kumail Nanjiani, and Emily V. Gordon",
                        "June 23, 2017",
                        "A Pakistani comic who falls in love with an American graduate student.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg",
                        "https://www.youtube.com/watch?v=jcD0Daqc3Yw")


how_to_be_signle = media.Movie("How to be single",
                        "Marc Silverstein, Dana Fox, and Abby Kohn",
                        "February 12, 2016",
                        "A girl that breaks up with her long-term boyfriend and moves to New York for a fun, new life.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d1/How_To_Be_Single_Poster.jpg",
                        "https://www.youtube.com/watch?v=RrDI4-BSovs")

#Create a list or array of movies to pass to fresh_tomatoes open_movies_page function
movies = [toy_story, avatar, inception, ratatouille, the_big_sick, how_to_be_signle]

fresh_tomatoes.open_movies_page(movies)
