from flask import Flask
import settings


app = Flask(__name__)


def configure_app(app):
    app.config['SERVER_NAME'] =settings.FLASK_SERVER_NAME
    app.config['SWAGGER_UI_DOC_EXPENSION'] = settings.RESTPLUS_SWAGGER_EXTENSION
    app.config['SWAGGER_VALIDED'] = settings.RESTPLUS_VAL
    app.config['RESTPLUS_MASK_SWAGGER'] =settings.RESTPLUS_MASK_SWAGGER

def init_app(app):
    configure_app(app)

def main():
    init_app(app)
    app.run(debug=settings.FLASK_DEBUG, threaded=settings.FLASK_THREADED)
if __name__ == '__main__':
    main()