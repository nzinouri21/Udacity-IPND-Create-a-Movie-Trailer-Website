import webbrowser

#Because we only have movies here, creating parent class Video might not be that useful.
#However, I wanted to implement the idea of inheritence.
#It also makes the code flexible if later on I decide to add tv shows or Netflix
#movies to my trailer website.


class Video():
    """ This class provides a way to store movie related information. """

    def __init__(self, movie_title, screenwriter, release_date):
        self.movie_title = movie_title
        self.screenwriter = screenwriter
        self.release_date = release_date

#Based on "Google Python Style Guide", when defining a class name,
#the first letter should be upper-case
class Movie(Video):
    """ This class provides a way to store movie related information. """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, screenwriter, release_date, movie_storyline, poster_image, trailer_youtube):
        #self.title = movie_title
        Video.__init__(self, movie_title, screenwriter, release_date)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
