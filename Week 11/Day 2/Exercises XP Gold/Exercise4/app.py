import flask
import datetime
app = flask.Flask(__name__)

@app.route('/')
def display_type():
	today = datetime.date.today()
	future = datetime.datetime(2021, 11, 28, 0, 0) - datetime.datetime.now()
	return f'''
		<html>
			<head>
				<title>Countdown</title>
			</head>
			<body>
		<h1>Today's date is: {today}</h1>
		<h1>Hanukkah is in: {future.days} days and {round((future.seconds/60)/60,2)} hours</h1>
			</body>
		</html>
	'''

app.run(debug=True, port=8080)

