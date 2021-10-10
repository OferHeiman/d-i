import flask
import datetime
app = flask.Flask(__name__)

@app.route('/')
def display_type():
	return f'''
		<html>
			<head>
				<title>By type</title>
			</head>
			<body>
		<h1>The current date is: {datetime.date.today()}</h1>
			</body>
		</html>
	'''

app.run(debug=True, port=8080)
