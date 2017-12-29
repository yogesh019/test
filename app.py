from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://yog:1234@localhost/book_store'
db=SQLAlchemy(app)

@app.route('/'):
    def index():
        return "<h1>Hello World</h1>"

if __name__=="__main__":
    app.run(debug=True)
