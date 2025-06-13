from flask import Flask, jsonify

from tmf620 import tmf620_bp
from tmf637 import tmf637_bp
#from tmf620_dataa import catalogs


app = Flask(__name__)
#app.config['CATALOGS'] = catalogs

app.register_blueprint(tmf620_bp, url_prefix='/tmf620')
app.register_blueprint(tmf637_bp, url_prefix='/tmf637')


if __name__ == '__main__':
    app.run(debug=True)
