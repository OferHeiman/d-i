import flask
app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template('homepage.html')

@app.route("/yellow")
def yellow():
    return flask.render_template('yellow.html')

@app.route("/red")
def red():
    return flask.render_template('red.html')

@app.route("/green")
def green():
    return flask.render_template('green.html')

@app.route("/blue")
def blue():
    return flask.render_template('blue.html')

app.run(debug=True, port=8080)