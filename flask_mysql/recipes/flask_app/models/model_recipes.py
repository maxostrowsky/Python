# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
# model the class after the friend table from our database

DATABASE = 'recipes_schema'
bcrypt = Bcrypt(app)

class Recipe:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def create(cls, data:dict):
        print(data)
        query = 'INSERT INTO recipes (name, description, instructions, under_30, date_made, user_id) VALUE (%(name)s, %(description)s, %(instructions)s, %(under_30)s,%(date_made)s, %(user_id)s)'
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of recipes
        recipes = []
        # Iterate over the db results and create instances of recipes with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one(cls, data:dict):
        query = 'SELECT * FROM recipes WHERE id=%(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    #u
    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, date_made=%(date_made)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    #d
    @classmethod
    def delete_one(cls,data):
        query = 'DELETE FROM recipes WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def recipe_validation(recipe_data):
        is_valid = True

        if len(recipe_data["name"]) < 1:
            flash("There must be a Name!")
            is_valid = False

        if len(recipe_data["description"]) < 1:
            flash("There must be a Description!")
            is_valid = False

        if len(recipe_data['instructions']) < 1:
            flash("There must be Instructions!")
            is_valid = False

        if not 'under_30' in recipe_data:
            flash('Must select Yes or No!')
            is_valid=False

        if len(recipe_data['date_made']) < 2:
            flash('Must select a date!')
            is_valid = False

        return is_valid

        

    # @staticmethod
    # def login_validation(user_data, password):
    #     if not user_data:
    #         flash('This email is incorrect!')
    #         return False
    #     if not bcrypt.check_password_hash(user_data.password, password):
    #         flash('Invalid password!')
    #         return False
    #     return True

    @classmethod
    def get_user_email(cls, data):
        query = "SELECT * FROM recipes WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return User(results[0])
        else:
            return False

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(cls, data)
        if results:
            return User(results[0])
        else:
            return False