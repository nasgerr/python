class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:
    def __init__(self):
        self.__rating = 0
    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, value):
        if value < 0 or value > 5:
            raise ValueError("Rating must be between 0 and 5")
        self.__rating = value
