import flask
import random
app = flask.Flask(__name__)

@app.route('/<number>')
def display_type(number:int):
	random_num = random.randrange(1,101)
	if int(number) == random_num:
		return f'''
			<html>
				<head>
					<title>Random</title>
				</head>
				<body>
			<h1>Success</h1>
				</body>
			</html>
			'''
	else:
		return f'''
			<html>
				<head>
					<title>Random</title>
				</head>
				<body>
				</body>
			</html>
			'''

app.run(debug=True, port=8080)
