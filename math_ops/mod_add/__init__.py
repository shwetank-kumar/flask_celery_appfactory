from flask import Blueprint

mod_add = Blueprint('mod_add', __name__, template_folder='templates')

from . import views
