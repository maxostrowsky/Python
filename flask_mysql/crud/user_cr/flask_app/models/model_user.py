# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = 'users_schema'

class User:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #c
    @classmethod
    def create(cls, data:dict):
        query = 'INSERT INTO users (first_name, last_name, email, created_at) VALUE (%(first_name)s, %(last_name)s, %(email)s,%(created_at)s)'
        return connectToMySQL(DATABASE).query_db(query, data)
        
    #r
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    #u
    
    #d
