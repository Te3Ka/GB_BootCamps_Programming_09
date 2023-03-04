from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return '<h1>Hello, World!</h1>'

@app.route('/index')
def index():
	return "<h2>Это моя первая страница</h2>"

if __name__ == '__main__':
	app.run()