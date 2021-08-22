from flask_restful import Resource
from flask import render_template, make_response, request


    
class ParameterController(Resource):
    def get(self):
        
        x = request.args.get('x')
        y = request.args.get('y')
        error = "Salah satu parameter tidak diisi, harap diisi terlebih dahulu"

        if not x or y:
            x = 30
            y = 30
        else:
            return error
        
        view = render_template('latihan-parameter.html', x=x, y=y, error=error) 
        return  make_response(view)