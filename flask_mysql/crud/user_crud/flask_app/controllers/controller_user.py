from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user

@app.route('/')
@app.route('/user')
def index():
    context = {
        'all_users' : model_user.User.get_all()
    }
    return render_template('all_users.html',**context)


#display route
@app.route('/user/new')
def new_user():
    
    return render_template('add_user.html')


@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    id = model_user.User.create(request.form)
    return redirect('/')


#display route
@app.route('/user/<int:id>')
def show_user(id):
    context = {
        'users': model_user.User.get_one({'id':id})
    }
    return render_template('one_user.html', **context)


#display route
@app.route('/user/<int:id>/edit')
def edit_user(id):
    context = {
        'users': model_user.User.get_one({'id':id})
    }
    return render_template('edit_user.html', **context)

@app.route('/user/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id': id
    }
    model_user.User.update_one(data)
    return redirect(f'/user/{id}')

@app.route('/user/<int:id>/delete', methods=['get'])
def delete_user(id):
    model_user.User.delete_one({'id':id})
    return redirect('/')

