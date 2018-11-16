class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    def printInformation(self):
        print(self.title)
        print(self.storyline)
        print(self.poster_image_url)
        print(self.trailer_youtube_url)
    
        