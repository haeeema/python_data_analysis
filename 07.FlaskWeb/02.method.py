from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>method 확인</h2><h2>/login으로 확인해 보세요</h2>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        return render_template('02.login_result.html', userid=userid, userpw=userpw)


@app.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'GET':
        return render_template('03.sample.html')
    else:
        a = request.form['a']
        b = request.form['b']
        return render_template('03.sample_result.html', a=a, b=b)


if __name__ == '__main__':
    app.run(debug=True)
