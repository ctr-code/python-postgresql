from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
# This is deprecated and moved to sqlalchemy.orm
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (sessionmaker, declarative_base)

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)


class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))


class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer)
    genre_id = Column(Integer)
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unit_price = Column(Float)


# Create a new session maker
Session = sessionmaker(db)

# Make the session
session = Session()

# Create the local metadata by analysing the database
base.metadata.create_all(db)

# select * from artist;
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" | ")

# select name from artist;
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)

# select name from artist where name='Queen';
# artist = session.query(Artist).filter_by(name="Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")

# select name from artist where artist_id=51;
# artist = session.query(Artist).filter_by(artist_id=51).first()
# print(artist.artist_id, artist.name, sep=" | ")

# select * from album where artist_id=51;
# albums = session.query(Album).filter_by(artist_id=51)
# for album in albums:
#     print(album.album_id, album.title, album.artist_id, sep=" | ")

# select * from track where composer='Queen';
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(
        track.track_id, track.name, track.album_id, track.media_type_id,
        track.genre_id, track.composer, track.milliseconds, track.bytes,
        track.unit_price, sep=" | ")
