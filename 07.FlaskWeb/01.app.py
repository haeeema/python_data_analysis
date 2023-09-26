from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/hello')
def hello():
    return render_template('01.hello.html')


@app.route('/sub/hello')
def sub_hello():
    return render_template('sub/01.hello.html')


if __name__ == '__main__':
    app.run(debug=True)
