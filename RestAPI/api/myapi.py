from flask_restplus import Api

api = Api(version='0.1', title='My Demo API', description='Plese use this')


@api.errorhandler
def std_handler(e):
    return { 'message': ' Error, please contact support'}, 500
