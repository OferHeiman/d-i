import flask
import datetime
app = flask.Flask(__name__)

@app.route('/')
def display_type():
	future = datetime.datetime(2022, 1, 1, 0, 0, 0) - datetime.datetime.now()
	return f'''
		<html>
			<head>
				<title>Countdown</title>
			</head>
			<body>
		<h1>The 1st of January is in {future.days} days and {round((future.seconds/60)/60,2)} hours</h1>
			</body>
		</html>
	'''

app.run(debug=True, port=8080)

