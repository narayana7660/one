# import random

# start = int(input("enter the starting value of the range: "))
# end= int(input("enter the ending value of the range: "))

# while start >= end:
#     print("starting value must be less than ending value, please enter the values correctly")
#     start = int(input("enter the starting value of the range: "))
#     end= int(input("enter the ending value of the range: "))

# generaterandom = random.randint(start,end)

# print(f"guess the number between {start} and {end}.you have 5 tries left")

# attempts = 5

# while attempts > 0:
#     guess = int(input("enter your guess: "))
#     attempts -=1

#     if guess < generaterandom:
#         print(f"your guessed value is less than generated value.{attempts} tries left")
#     elif guess > generaterandom:
#         print(f"your guessed value is more than generated value.{attempts} tries left")
#     else:
#         print("congratulations! your guessed number is correct")
#         break

# else:
#     print(f"sorry,you have ran out of your attempts,the genarated value is - {generaterandom:}.better luck next time!")

# import psycopg2
# connection = psycopg2.connect(
#     host = "localhost",
#     user = "postgres",
#     password = "9509",
#     dbname = "postgres",
#     port = 5432
#  )

# mycursor = connection.cursor()
# mycursor.execute("update profile set name = 'krish', email = 'krish@gmail.com' where id = 3")
# # myresult = mycursor.fetchall()

# # for x in myresult:
# #     print(x)
# # mycursor.close()
# connection.commit()
# print("program is executed")
# connection.close()

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def fun():
#     return"hello"
# @app.route("/home/<name>")
# def myfunc(name):
#     return"welcome %s to the python class" % name

# if __name__ =="__main__":
#     app.run()


# from flask import Flask,redirect,url_for,render_template,jsonify,request
# import psycopg2
# from psycopg2 import Error,extras
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# def con():
#     connection=None
#     try:
#         connection = psycopg2.connect(
#     host="localhost",
#     user="postgres",
#     password="9509",
#     dbname="postgres",
#     port=5432  
#         )
#     except Error as e:
#         print(f"the error is '{e}")
#     return connection

# @app.route('/item/<int:id>',methods=["GET"])
# def fun(id):
#   connection= con()
# cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cursor.execute('select * from profile where id = %s',(id,))
# items = cursor.fetchone()
# cursor.close()
# connection.close()
# if items:
#     return jsonify(dict(items))
# else:
#     return jsonify({"error":"item not found"})

# from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def fun():
#     return"hello Narayana"

# if __name__=="__main__":
#     app.run()

# from flask import *
# app = Flask(__name__)
# @app.route('/user/<name>')
# def fun(name):
#     return render_template("base.html",name=name)
# if __name__=="__main__":
#     app.run()

# from flask import Flask,redirect,url_for,render_template,jsonify,request
# import psycopg2
# from psycopg2 import Error,extras
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# def con():
#     connection=None
#     try:
#         connection = psycopg2.connect(
#     host="localhost",
#     user="postgres",
#     password="9509",
#     dbname="postgres",
#     port=5432  
#         )
#     except Error as e:
#         print(f"the error is '{e}")
#     return connection

#     @app.route('/item/<int:id>',methods=["GET"])
#     def fun(id):
#         connection= con()
#         cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         cursor.execute('select * from profile where id = %s',(id,))
#         items = cursor.fetchone()
#         cursor.close()
#         connection.close()
      
#     if items:
#         return jsonify(dict(items))
#     else:
#         return jsonify({"error":"item not found"})

from flask import Flask,redirect,url_for,render_template,jsonify,request
import psycopg2
from psycopg2 import Error,extras
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def con():
    connection=None
    try:
        connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="9509",
    dbname="postgres",
    port=5432  
        )
    except Error as e:
        print(f"the error is '{e}")
    return connection



@app.route('/item/<int:id>',methods=["GET"])
def fun(id):
    connection= con()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('select * from profile where id = %s',(id,))
    items = cursor.fetchone()
    cursor.close()
    connection.close()
    if items:
        return jsonify(dict(items))
    else:
        return jsonify({"error":"item not found"})
 
@app.route('/postitem',methods=["POST"])
def createitem():
    data = request.get_json()
    name=data.get('name')
    email=data.get('email')
    connection=con()
    cursor= connection.cursor()
    cursor.execute("insert into profile (name, email) values(%s,%s)",(name, email))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message":"item inserted to the database"})

@app.route('/items/<int:id>',methods=["PUT"])
def updateitem(id):
    data=request.get_json()
    name=data.get('name')
    email=data.get('email')
    connection =con()
    cursor = connection.cursor()
    cursor.execute("update profile set name=%s,email= %s where id=%s",(name,email,id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message":"item updated successfully"})

@app.route('/del/<int:id>',methods=["DELETE"])
def delitem(id):
    connection= con()
    cursor = connection.cursor()
    cursor.execute("delete from profile where id = %s",(id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message":"item is deleted"})

if __name__=="__main__":
    app.run()

