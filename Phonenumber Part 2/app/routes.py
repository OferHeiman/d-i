from app import app, db, models
from flask import redirect, render_template, url_for, render_template_string
import random
from faker import Faker


@app.route('/')
def index():
    all_people = models.Person.query.all()
    all_phonenumbers = models.Phonenumber.query.all()
    all_nationalities = models.Nationality.query.all()
    return render_template('index.html', all_people=all_people, all_phonenumbers=all_phonenumbers, all_nationalities=all_nationalities)


@app.route('/fakeperson')
def fakeperson():
    print('add fake person')
    fake = Faker()
    name = fake.name()
    email = fake.email()
    address = fake.address()
    person = models.Person(name=name, email=email, address=address)
    db.session.add(person)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/fakephonenumber')
def fakephonenumber():
    print('add fake phone number')
    fake = Faker()
    number = fake.phone_number()
    random_person = random.choice(models.Person.query.all())
    phonenumber = models.Phonenumber(number=number, owner=random_person.id)
    db.session.add(phonenumber)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/addnationality')
def add_nationality():
    fake = Faker()
    nationality = models.Nationality(name=fake.country())
    db.session.add(nationality)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/addnationalitytorandomperson')
def add_nationality_to_random_person():
    random_person = random.choice(models.Person.query.all())
    random_nationality = random.choice(models.Nationality.query.all())
    random_person.nationalities.append(random_nationality)
    random_nationality.people.append(random_person)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/person/<phonenumber>')
def person_info_phonenumber(phonenumber):
    try:
        person_id_by_phonenumber = models.Phonenumber.query.filter_by(number=phonenumber)[0].owner
    except:
        return render_template_string('no results found for ' + phonenumber)
    person = models.Person.query.filter_by(id=person_id_by_phonenumber).first()
    person_phone_numbers = person.phonenumbers
    return render_template('personbyphonenumber.html', person=person, person_phone_numbers=person_phone_numbers)


@app.route('/person1/<name>')
def person_info_name(name):
    person = models.Person.query.filter_by(name=name).first()
    if person is None:
        return render_template_string('no results found for'+name)
    person_phone_numbers = person.phonenumbers
    return render_template('personbyname.html', person=person, person_phone_numbers=person_phone_numbers)


@app.route('/people/<nationality>')
def people_with_nationality(nationality):
    try:
        all_people_with_nationality = models.Nationality.query.filter_by(name=nationality).all()[0]
    except:
        return render_template_string('no results found for ' + nationality + ', maybe you missed an uppercase?')
    return render_template('peoplebynationality.html', all_people_with_nationality=all_people_with_nationality)
