from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
'''
set FLASK_APP=run.py
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
set FLASK_DEBUG=1
flask run
'''

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bihifqmu:bQVDAoxN9Wc8FHqIYoDVJDoR3bpO5QHx@rosie.db.elephantsql.com/bihifqmu'

db = SQLAlchemy(app)

db.init_app(app)
db.Model.metadata.reflect(db.engine)

from routes.add_route import bp as add_bp
from routes.search_route import bp as search_bp
from routes.recommend_route import bp as recommend_bp
app.register_blueprint(add_bp)
app.register_blueprint(search_bp)
app.register_blueprint(recommend_bp)

@app.route('/')
def index():
    return render_template('index.html'), 200


