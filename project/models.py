from flask_login import UserMixin
from .extensions import db
import sqlite3 as sql

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))



class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(35))
   email = db.Column(db.String(50))
   message = db.Column(db.String(100))

   def __init__(self, name, email, message):
    self.name = name
    self.email = email
    self.message = message
       
class Contact(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String(40))
    message = db.Column(db.String(200))
    
    def __init__(self,name,email,message):
        self.name = name
        self.email = email
        self.message = message

class Product(db.Model):
    id = db.Column('id',db.Integer, primary_key = True)
    brand = db.Column(db.String(25))
    model = db.Column(db.String(40))
    price = db.Column(db.Integer())
    
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

# #connect to SQLite
# con = sql.connect('db_web.db')

# #Create a Connection
# cur = con.cursor()

# #Drop users table if already exsist.
# cur.execute("DROP TABLE IF EXISTS users")

# #Create users table  in db_web database
# sql ='''CREATE TABLE "Mobiles" (
# 	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	"BRAND"	TEXT,
# 	"MODEL"	TEXT,
#     "IMAGES" VARBINARY(),
#     "PRICE" TEXT )'''
    
# cur.execute(sql)

# #commit changes
# con.commit()

# #close the connection
# con.close()

