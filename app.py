from flask import Flask
from views import views
from models import db
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Config SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(views)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)