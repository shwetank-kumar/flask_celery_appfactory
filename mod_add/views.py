from flask import Blueprint

add = Blueprint('add', __name__, template_folder='templates')

@add.route('/<int:int1>/<int:int2>')
def main(int1, int2):
    sum = str(int1+int2)
    return sum
