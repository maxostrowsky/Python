from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user

@app.route('/')
@app.route('/user')
def index():
    all_users = model_user.User.get_all()
    return render_template('all_users.html',all_users = all_users)

@app.route('/user/new')
def new_user():
    
    return render_template('add_user.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    id = model_user.User.create(request.form)
    return redirect('/')

@app.route('/user/<int:id>')
def show_user():
    pass

@app.route('/user/<int:id>/edit')
def edit_user():
    pass

@app.route('/user/<int:id>/update')
def update_user():
    pass

@app.route('/user/<int:id>/delete')
def delete_user():
    pass

