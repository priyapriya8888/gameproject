from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)

# Simple mock login system
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with open('users.json') as f:
            users = json.load(f)
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect('/')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.json') as f:
            users = json.load(f)
        users[username] = password
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return redirect('/login')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
