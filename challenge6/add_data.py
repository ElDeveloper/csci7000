import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Newsboys")
new_artist.albums = [Album("Read All About It", 
                           'some genre',
                           "Refuge", "CD")]
 
# add more albums
more_albums = [Album("Hell Is for Wimps",
                     "some genre",
                     "Star Song", "CD"),
               Album("Love Liberty Disco", 
                     'and another genre',
                     "Sparrow", "CD"),
               Album("Thrive",
                     'so genre',
                     "Sparrow", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("Some awesome singer"),
    Artist("Such SQLAlchemy"),
    Artist("Very wooow")
    ])
session.commit()