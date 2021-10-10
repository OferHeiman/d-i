import flask
app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template('CV.html')

app.run(debug=True, port=8080)