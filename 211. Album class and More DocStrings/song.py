class Song:
    """
    Class to represent a song
    
    Attributes:
        title (str): The title of the song.
        artist (Artist): An artist object representing the song creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        album_name (str): The name of the album.
        year (int): The year was album released.
        artist (Artist): The artist responsible for the album. If not specified,
            the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs ig necessary.
                Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


# DocString representation:
# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)
# Song.__init__.__doc__ = """Song init method
#
#         Args:
#             title (str): Initialises the 'title' attribute
#             artist (Artist): At Artist object representing the song's creator.
#             duration (Optional[int]): Initial value for the 'duration' attribute.
#         """
# help(Song)
