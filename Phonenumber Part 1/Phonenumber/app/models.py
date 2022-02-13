from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True)
    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')
    address = db.Column(db.String(200))


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))




