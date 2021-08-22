from flask_restful import Resource
from flask import render_template, make_response, request

class MyViewController(Resource):
    def get(self):
        view = render_template('index.html')
        return make_response(view)
    
class MySecondViewController(Resource):
    def get(self):
        name = request.args.get('name')
        age = request.args.get('age')
        
        if not name or age: # Pengecekan kondisi apabila nama kosong, maka digantikan dengan default name yaitu Hudya
            name = "Eric"
            age = 20

        view = render_template('say-my-name.html', name=name, age=age)
        return make_response(view)