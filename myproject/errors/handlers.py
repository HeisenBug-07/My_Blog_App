from flask import Blueprint, render_template

error_blueprint = Blueprint('errors', __name__, template_folder='templates/errors')


@error_blueprint.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404
