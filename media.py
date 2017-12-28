import webbrowser

#Because we only have movies here, creating parent class Video might not be that useful.
#However, I wanted to implement the idea of inheritence.
#It also makes the code flexible if later on I decide to add tv shows or Netflix
#movies to my trailer website.

#Based on "Google Python Style Guide", when defining a class name,
#the first letter should be upper-case
class Video():
    """ This class provides a way to store movie related information.
    Attributes:
        movie_title: A string that stores the movie title. This is inhereted from parent class Video.
        screenwriter: A string that stores movie screen writer or writers. This is inhereted from parent class Video.
        release_date: A string that stores movie release date. This is inhereted from parent class Video.
    """

    def __init__(self, movie_title, screenwriter, release_date):
        self.title = movie_title
        self.screenwriter = screenwriter
        self.release_date = release_date


class Movie(Video):
    """ This class provides a way to store movie related information.
    Attributes:
        movie_title: A string that stores the movie title. This is inhereted from parent class Video.
        screenwriter: A string that stores movie screen writer or writers. This is inhereted from parent class Video.
        release_date: A string that stores movie release date. This is inhereted from parent class Video.
        movie_storyline: A string that stores the basic plot of the movie.
        poster_image: A string that stores the URL of the movie poster.
        trailer_youtube: A string that stores he URL of the movie trailer.

    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, screenwriter, release_date, movie_storyline, poster_image, trailer_youtube):
        #self.title = movie_title
        Video.__init__(self, movie_title, screenwriter, release_date)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""

        webbrowser.open(self.trailer_youtube_url)
