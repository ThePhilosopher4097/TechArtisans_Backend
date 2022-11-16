# using flask_restful
from flask import Flask, jsonify, request, redirect
from flask_restful import Resource, Api
  

app = Flask(__name__)

api = Api(app)

class Root(Resource):
  
    def get(self):
        return jsonify({'message': 'hello TechArtisans', 'Page-details':'You have landed to the Root Page !'})
  

class Register(Resource):
  
    def get(self):
        return jsonify({'message': 'hello world'})
  
    def post(self):
        data = request.get_json()     
        return jsonify({'data': data}), 201

  
class Login(Resource):
  
    def get(self):
        return jsonify({'status': 200})
    def post(self):
        return jsonify({'status': 200})
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Root, '/')
api.add_resource(Register, '/user/signup/')
api.add_resource(Login, '/user/login/')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)