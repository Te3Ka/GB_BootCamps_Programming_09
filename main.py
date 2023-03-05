from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return "<h1>Hello, World!</h1><a href='/index'>Перейти на 2-ую страницу</a>"

@app.route('/index/<x>/<y>')
def index(x, y):
	return f"<h2>Это моя первая страница</h2><br><h3>Реузльтат: {int(x) + int(y)}</h3>"

if __name__ == '__main__':
	app.run()