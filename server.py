# using flask_restful
from flask import Flask, jsonify, request, redirect, session, make_response
from flask_restful import Resource, Api
# Postgre
import psycopg2 as psyco
import Database.db as db
 

app = Flask(__name__)
app.secret_key = 'techArtisans000'

api = Api(app)

class Root(Resource):
  
    def get(self):
        return jsonify({'message': 'hello TechArtisans', 'Page-details':'You have landed to the Root Page !'})
 

class Register(Resource):
  
    def get(self):
        return jsonify({'message': 'hello world'})
  
    def post(self):
        user_dict = request.get_json()     

        # ESTABLISH DB CONNECTION ############## 
        conn = db.connect_db()
        if conn == None:
            return make_response(jsonify({'error': 'Error connecting to db'}), 500)
        cur = conn.cursor()
        
        # CHECK IF USER EXISTS ################# 
        check_user_q = """
                       SELECT email, password
                       FROM student
                       WHERE email=%s
                       """
        cur.execute(check_user_q, (user_dict['email'],))

        if not (cur.rowcount == 0):
            db.close_db(cur, conn)
            return make_response(jsonify({'error':'User already exists'}),
                                 600)

        # INSERT USER DETAILS ################## 
        ins_user_q = """
                     INSERT INTO student
                     (name, email, phone, password, country)
                     VALUES
                     (%s, %s, %s, %s, %s)
                     """
        try:
            cur.execute(ins_user_q, (user_dict['name'],
                                     user_dict['email'],
                                     user_dict['phone'],
                                     user_dict['password'],
                                     user_dict['country']

            ))
            conn.commit()
            db.close_db(cur, conn)
            session['user'] = user_dict['email']
            return make_response(jsonify(
                {'success':'registered'}
            ), 201)

        except (Exception, psyco.DatabaseError) as e:
            print(e)
            db.close_db(cur, conn)
            return make_response(jsonify({'error':'Unable to create user'}), 601)

  
class Login(Resource):
  
    def get(self):
        return jsonify({'status': 200})

    def post(self):
        user_dict = request.get_json()

        # ESTABLISH DB CONNECTION ############## 
        conn = db.connect_db()
        if conn == None:
            return make_response(jsonify({'error': 'Error connecting to db'}), 500)
        cur = conn.cursor()

        # CHECK FOR USER IN DB ################# 
        check_user_q = """
                       SELECT email, password
                       FROM student
                       WHERE email=%s
                       """
        cur.execute(check_user_q, (user_dict['email'],))

        if cur.rowcount == 0:
            print("User not found ", user_dict['email'])
            db.close_db(cur, conn)
            return make_response(jsonify({'error': 'User not found'}), 600)

        # AUTHENTICATE ######################### 
        for username, pswd in cur.fetchall():
            if pswd == user_dict['password']:
                db.close_db(cur, conn)

                session['user'] = username
                return make_response(jsonify({'success': 'Login'}), 200)

        return make_response(jsonify({'error': 'Incorrect credentials'}), 601)
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Root, '/')
api.add_resource(Register, '/user/signup/')
api.add_resource(Login, '/user/login/')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug=True, port=5000)
