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


    return render_template('login.html')

@app.route('/doublelogin', methods=['GET', 'POST'])
def weakpage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            return '계정 정보 유출'
        else:
            return '계정 정보 유출'

    return render_template('doublelogin.html')


if __name__ == '__main__':
    app.run(debug=True, port=5414)

