import flask
import flask_sqlalchemy
import werkzeug.security as ws

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = flask_sqlalchemy.SQLAlchemy(app)

class UserTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)

with app.app_context():
    db.create_all()
    user1 = UserTable(username = "user1", password = ws.generate_password_hash("password1"))
    user2 = UserTable(username = "user2", password = ws.generate_password_hash("password2"))
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
