from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect

app = Flask(__name__)

all_posts = [
    {
    'title': 'Post 1',
    'Content': 'This is about something far greater than you imagine'
    },
    {
    'title': 'Post 2',
    'author': 'Tirth Patel',
    'Content': 'This is about something far smaller than you imagine'
    }
]


# app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql:///postgres:tirth177@localhost/blog'
# db = SQLAlchemy(app)
# session = db.session()
# cursor = session.execute(sql).cursor

# class BlogPost(db.Model):
engine = create_engine('postgresql://postgres:tirth177@localhost/blog')
# with engine.connect() as con:

#     rs = con.execute('SELECT * FROM posts')

#     for row in rs:
#         print(row)

#     def __repr__(self):
#         return 'Blog Post ' + str(self.id)



@app.route('/')
def index():
    # test = session.execute("SELECT * FROM posts;")
    con = engine.connect()
    rs = con.execute('SELECT * FROM posts')
    return render_template('index.html', test=rs)


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


@app.route('/<string:name>/<int:id>')
def hello(name, id):
    return "Hello "+ name+ ' ' + str(id*10) + " !"

@app.route('/onlyget', methods = ['POST','GET'])
def get_req():
    return 'Yoou can only get this webpage'

if __name__ == '__main__':
    app.run(debug=True)
