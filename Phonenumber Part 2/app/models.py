from app import db

nationality_table = db.Table('nationalities',
                    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                    db.Column('nationality_id', db.Integer, db.ForeignKey('nationality.id')))


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True)
    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')
    address = db.Column(db.String(200))
    nationalities = db.relationship("Nationality", secondary=nationality_table, back_populates="people")


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))


class Nationality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    people = db.relationship("Person", secondary=nationality_table, back_populates="nationalities")




