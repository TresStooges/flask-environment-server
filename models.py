from app import db


class Property(db.Model):
    """docstring for Blog"""

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    temperature = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    image = db.Column(db.String)

    def __init__(self, location, temperature, timestamp, image):
        self.location = location
        self.temperature = temperature
        self.timestamp = timestamp
        self.image = image
