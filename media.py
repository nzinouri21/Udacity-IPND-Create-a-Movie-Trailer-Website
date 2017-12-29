import webbrowser

#Because we only have movies here, creating parent class Video might not be that useful.
#However, I wanted to implement the idea of inheritence.
#It also makes the code flexible if later on I decide to add tv shows or Netflix
#movies to my trailer website.

#Based on "Google Python Style Guide", when defining a class name,
#the first letter should be upper-case
class Video():
    """ This class provides a way to store movie related information."""


    def __init__(self, movie_title, screenwriter, release_date):
        """This is class Video's constructor function.
            Args:
                movie_title (str): A string that stores the movie title. This is inhereted from parent class Video.
                screenwriter (str): A string that stores movie screen writer or writers. This is inhereted from parent class Video.
                release_date (str): A string that stores movie release date. This is inhereted from parent class Video.
            Returns:
                None
        """
        self.title = movie_title
        self.screenwriter = screenwriter
        self.release_date = release_date


class Movie(Video):
    """ This class provides a way to store movie related information."""


    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, screenwriter, release_date, movie_storyline, poster_image, trailer_youtube):
        """This is class Movie's constructor function.

            Args:
                movie_title (str): A string that stores the movie title. This is inhereted from parent class Video.
                screenwriter (str): A string that stores movie screen writer or writers. This is inhereted from parent class Video.
                release_date (str): A string that stores movie release date. This is inhereted from parent class Video.
                movie_storyline (str): A string that stores the basic plot of the movie.
                poster_image (str): A string that stores the URL of the movie poster.
                trailer_youtube (str): A string that stores he URL of the movie trailer.
            Returns:
                None
        """

        #self.title = movie_title
        Video.__init__(self, movie_title, screenwriter, release_date)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Plays the movie trailer in the web browser.

            Args:
                None
            Returns:
                Opens web browser of YouTube trailer.

        """

        webbrowser.open(self.trailer_youtube_url)
