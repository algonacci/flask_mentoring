from flask_restful import Resource
from flask import render_template, make_response, request

class ParameterController(Resource):
    def get(self):
        x = request.args.get('x')
        y = request.args.get('y')

        message = "Salah satu parameter tidak diisi, harap diisi terlebih dahulu"

        if x and y:
            message = "Kedua Parameter telah diisi, nilai tersebut adalah %s , %s" % (x, y)

        view = render_template('latihan-parameter.html', message=message)
        return  make_response(view)