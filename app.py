from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect,url_for
from sqlalchemy import(
        Column,
        Integer,
        String,
        Boolean,
        ForeignKey,
        DateTime,
        Sequence,
        Float
)
#import dateTime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://yog:1234@localhost/store'
db=SQLAlchemy(app)
app.debug=True

map_table=db.Table('map_table',
        db.Column('author_id',db.Integer,db.ForeignKey('author.id')),
        db.Column('book_id',db.Integer,db.ForeignKey('book.id'))
)
class Author(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    books=db.relationship('Book',secondary=map_table,backref=db.backref('map_table',lazy='dynamic'))

    def __repr__(self):
        return '<Author:{}>'.format(self.name)

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text)
    authors=db.relationship('Author',secondary=map_table,backref=db.backref('map_table',lazy='dynamic'))
    
    def __repr__(self):
        return '<Book:{}>'.format(self.title)



@app.route('/')
def index():
    #db.create_all()
    books=Book.query.all()
    return render_template('add_details.html',books=books)

@app.route('/add_details',methods=['POST'])
def add_details():
    print("yogi")
    book=Book(title=request.form['book'])
    author=request.form['author']
    print("yo")
    x=author.split(',')
    print(x)
    print("sharma")
    print("yogesh")
    db.session.add(book)
    book.authors=[]
    for i in x:
        a=Author(name=str(i))
        print(a)
        db.session.add(a)
        book.authors.append(a)
    print("loki")
    db.session.commit()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
