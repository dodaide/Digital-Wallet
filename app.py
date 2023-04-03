from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from transaction import transact, getBalance
from config import USER_NAME, PASSWORD, SENDER_ADDRESS

app = Flask(__name__)
app.secret_key = '123456789'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = '123456789'
Session(app)

@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html', balance=getBalance(), senderAddress=SENDER_ADDRESS)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_NAME and password == PASSWORD:
            session['logged_in'] = True
            session['password'] = password
            return redirect(url_for('index'))
        else:
            error = 'Sai tài khoản hoặc mật khẩu'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/payment')
def payment():
    return render_template('payment.html', balance=getBalance())

@app.route('/verify', methods=['POST'])
def verify():
    session['receiver'] = request.form['receiver']
    session['amount'] = request.form['amount']
    return render_template('verify.html')

@app.route('/done', methods=['POST'])
def done():
    password = request.form['password']
    receiver = session.get('receiver')
    amount = session.get('amount')
    if password == session.get('password'):
        isSuccess = transact(receiver, amount)
        if isSuccess:
            return render_template('done.html', receiver=receiver, amount=amount)
        else:
            return render_template('done.html', error=True)
    else:
        return render_template('done.html', error=True)

if __name__ == '__main__':
    app.run(debug=True)

