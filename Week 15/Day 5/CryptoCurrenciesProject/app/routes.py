import pprint

from app import app, db, models
from flask import redirect, render_template, url_for, flash, request
from sqlalchemy import or_, func
import random
from faker import Faker
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, login_user, current_user, UserMixin, login_required, logout_user
from requests import Request, Session
import json

# cryptocurrency's metrics from API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start': '1',
  'limit': '20',
  'convert': 'USD',
  'sort': 'market_cap',
  'sort_dir': 'desc'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ce6e8d4-0ac3-4434-b072-fd1ae1017454',
}
session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)
data = json.loads(response.text)

# global metrics from API
url2 = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

session2 = Session()
session2.headers.update(headers)
response2 = session.get(url2)
data2 = json.loads(response2.text)
pprint.pprint(data)


@app.context_processor  # pass variables information to templates
def inject_constants():
    return {'cryptodata': data2['data']}


@app.route('/')
def index():
    # our_ads = models.Ads.query.order_by(models.Ads.date_added)
    return render_template('index.html', cryptos=data)


@app.route('/fakeads')
def fakeads():
    print('add fake ad')
    fake = Faker()
    for _ in range(5):
        name = fake.word()
        photo = fake.image_url()
        price = str(random.randint(1, 5000)) + '$'
        choices = ['New', 'Used', 'Barely used']
        condition = random.choice(choices)
        category_choices = ['Vehicles', 'Real Estate', 'Apparel', 'Electronics', 'Home Goods',
                            'Musical Instruments', 'Office Supplies', 'Sporting Goods',
                            'Toys & Games', 'Hobbies', 'Family', 'Entertainment', 'Other']
        category = random.choice(category_choices)
        phonenumber = fake.phone_number()
        email = fake.email()
        description = fake.text()
        location = fake.address()
        ad = models.Ads(name=name, photo=photo, price=price, condition=condition, phonenumber=phonenumber, email=email,
                        category=category, description=description, location=location)
        db.session.add(ad)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete')
def deleteads():
    print('deleted all ads')
    models.Ads.query.delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/search')
def search():
    query = request.args['search']  # search=keyword from search bar
    # searches both name and description columns for search result
    nameresults = models.Ads.query.filter(or_(models.Ads.name.contains(query),
                                              models.Ads.description.contains(query),
                                              models.Ads.location.contains(query),
                                              ))
    return render_template('search.html', nameresults=nameresults)


@app.route('/item/<itemid>')
def item(itemid):
    ad = models.Ads.query.filter_by(id=itemid).first()
    return render_template('item.html', ad=ad)


@app.route('/category/<categoryname>')
def showcategory(categoryname):
    category_ads = models.Ads.query.filter(models.Ads.category.contains(categoryname))
    return render_template('specifics.html', category_ads=category_ads)


@app.route('/delete/<itemid>')
def delete(itemid):
    user_to_delete = models.Ads.query.get_or_404(itemid)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Listing Deleted Successfully")
        return redirect(url_for('index'))
    except:
        flash("Whoops! there was a problem deleting the listing, try again...")
        return redirect(url_for('index'))


@app.route('/signup', methods=("GET", "POST"))
def signup():
    form = models.UsersForm()
    if form.validate_on_submit():  # Check if the form has been filled
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = pbkdf2_sha256.hash(password)
        user = models.Users(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        form.username.data = ''
        form.email.data = ''
        form.password.data = ''
        form.confirmpassword.data = ''
        flash("You Have Successfully Signed Up!")
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)


@app.route('/login', methods=("GET", "POST"))
def login():
    form = models.LoginForm()
    if form.validate_on_submit():
        user_object = models.Users.query.filter_by(username=form.username.data).first()
        login_user(user_object)
        flash("You Have Successfully Logged in!")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile', methods=["GET"])
def profile():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('profile.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
