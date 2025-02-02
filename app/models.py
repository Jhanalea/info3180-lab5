from . import db


class Movie(db.Model):
  __tablename__ = 'movies'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150))
  description = db.Column(db.String(800))
  poster = db.Column(db.String(250))
  created_at = db.Column(db.DateTime)

  def __init__(self, title, description, poster, created_at):
    self.title = title
    self.description = description
    self.poster = poster
    self.created_at = created_at

  def __repr__(self):
    return f'<Movie {self.id}>'