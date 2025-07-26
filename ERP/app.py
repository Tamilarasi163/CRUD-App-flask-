from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tamil'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp.db'

db = SQLAlchemy(app)

from routes import *

with app.app_context():
    db.create_all()
    
if __name__=='__main__':
    app.run(debug=True)