from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

db = create_engine("postgresql:///chinook")

meta = MetaData()
# meta.reflect(bind=db)

artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String,)
)

album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id")),
)

track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer),
    Column("genre_id", Integer),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

with db.connect() as connection:
    # select * from artist;
    # select_query = artist_table.select()

    # select name from artist;
    # select_query = artist_table.select().with_only_columns(artist_table.c.name)

    # select name from artist where name='Queen';
    # select_query = artist_table.select().where(artist_table.c.name == "Queen")

    # select name from artist where artist_id=51;
    # select_query = artist_table.select().where(artist_table.c.artist_id == 51)

    # select * from album where artist_id=51;
    # select_query = album_table.select().where(album_table.c.artist_id == 51)

    # select * from track where composer='Queen';
    select_query = track_table.select().where(track_table.c.composer == "Queen")

    results = connection.execute(select_query)

    for result in results:
        print(result)
