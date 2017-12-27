import webbrowser
#Things we want the class movie to remember:
#   1.Title
#   2.Storyline
#   3.Poster image
#   4.YouTube trailer
class Video():
    def __init__(self, title):
        self.title = title
        #self.duration = duration
#Based on "Google Python Style Guide", when defining a class name,
#the first letter should be upper-case
class Movie(Video):
    """ This class provides a way to store movie related information. """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        #self.title = movie_title
        Video.__init__(self, title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, title, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self .season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
