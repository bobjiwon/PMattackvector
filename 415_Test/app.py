from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 사용자 정보를 저장할 간단한 데이터베이스 대신에 딕셔너리를 사용합니다.
users = {
    'user1': {'username': 'user1', 'password': 'pass1'},
    'user2': {'username': 'user2', 'password': 'pass2'}
}

@app.route('/')
def index():
    return '홈페이지'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            return f'로그인 성공, {username}님!'
        else:
            return '로그인 실패. 아이디 또는 비밀번호를 확인하세요.'

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return '이미 존재하는 사용자입니다. 다른 아이디를 사용하세요.'
        else:
            users[username] = {'username': username, 'password': password}
            return f'회원가입 성공, {username}님!'

    return render_template('signup.html')

@app.route('/weakpage', methods=['GET', 'POST'])
def weakpage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            return '계정 정보 유출'
        else:
            return '계정 정보 유출'

    return render_template('weakpage.html')

@app.route('/iframe', methods=['GET', 'POST'])
def iframe():
    return render_template('iframe.html')


if __name__ == '__main__':
    app.run(debug=True, port=5415)

