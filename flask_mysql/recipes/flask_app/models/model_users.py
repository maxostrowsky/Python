# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
# model the class after the friend table from our database

DATABASE = 'recipes_schema'
bcrypt = Bcrypt(app)

class User:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def create(cls, data:dict):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s, %(last_name)s, %(email)s,%(password)s)'
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data:dict):
        query = 'SELECT * FROM users WHERE id=%(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    #u
    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, created_at=%(created_at)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    #d
    @classmethod
    def delete_one(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def registration_validation(user_data):
        is_valid = True

        if len(user_data["first_name"]) < 2:
            flash("First name must be at least two characters!")
            is_valid = False

        if len(user_data["last_name"]) < 2:
            flash("Last name must be at least two characters!")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email address")
            is_valid = False
        else:
            user = User.get_user_email({"email":user_data['email']})
            if user:
                flash('Email is already in use!')
                is_valid = False

        if len(user_data['password']) < 8:
            flash("password must be at least eight(8) characters")
            is_valid = False
        
        if user_data['password'] != user_data['confirm_password']:
            flash("Passwords do not match!")
            is_valid = False

        return is_valid

        

    @staticmethod
    def login_validation(user_data, password):
        if not user_data:
            flash('This email is incorrect!')
            return False
        if not bcrypt.check_password_hash(user_data.password, password):
            flash('Invalid password!')
            return False
        return True

    @classmethod
    def get_user_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return User(results[0])
        else:
            return False

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(cls, data)
        if results:
            return User(results[0])
        else:
            return False


