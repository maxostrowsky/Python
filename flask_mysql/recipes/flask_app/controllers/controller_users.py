from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_users
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not model_users.User.registration_validation(request.form):
        return redirect('/')

    hash_browns = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password":hash_browns
    }
    id = model_users.User.create(data)
    session['uuid'] = id

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user = model_users.User.get_user_email({'email':request.form['email']})
    if not model_users.User.login_validation(user, request.form['password']):
        print('see anything')
        return redirect('/')
    session['uuid'] = user.id
    return redirect ('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')