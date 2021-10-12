
from flask import Flask, render_template, request,redirect
from flask_wtf import form
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'dev fao football app'

@app.route('/CV', methods=["GET", "POST"])
def get_CV():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        age = request.form["age"]
        phone = request.form["phone"]
        email = request.form["email"]
        experience = request.form["experience"]
        education = request.form["education"]
        return render_template('CVPage.html',name=name,age=age,phone=phone,email=email,experience=experience,education=education)
    return render_template('CV.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
