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
        name (str): The name of the album.
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

class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List(Album)): A list of the albums by this artist.
            The List includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        """
        Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (although this is yet to implemented).
        """
        self.album.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()
