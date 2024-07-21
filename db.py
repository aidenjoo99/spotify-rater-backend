from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
  """
  Artist Model
  """

  __tablename__ = "artist"
  id = db.Column(db.String, primary_key=True, unique=True)
  rating = db.Column(db.Integer, nullable=True)
  albums = db.relationship("Album", cascade="all,delete", backref="artist")
  tracks = db.relationship("Track", cascade="all,delete", backref="artist")

class Album(db.Model):
  """
  Album Model
  """

  __tablename__ = "album"
  id = db.Column(db.String, primary_key=True, unique=True)
  rating = db.Column(db.Integer, nullable=True)
  artist_id = db.Column(db.String, db.ForeignKey("artist.id"), nullable=False)
  tracks = db.relationship("Track", cascade="all,delete", backref="album")

class Track(db.Model):
  """
  Track Model
  """

  __tablename__ = "track"
  id = db.Column(db.String, primary_key=True, unique=True)
  rating = db.Column(db.Integer, nullable=True)
  artist_id = db.Column(db.String, db.ForeignKey("artist.id"), nullable=False)
  album_id = db.Column(db.String, db.ForeignKey("album.id"), nullable=False)