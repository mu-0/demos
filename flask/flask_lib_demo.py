from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://..."

db = SQLAlchemy(app)

class Files(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String, nullable = False)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String)
    year = db.Column(db.String)
    edition = db.Column(db.String)
    tags = db.Column(db.JSON)

if __name__ == "__main__":
    with app.app_context():

        results = Files.query.all()
        columns = [column.name for column in Files.__table__.columns]

        for result in results:
            row_data = {column: getattr(result, column) for column in columns}
            print(row_data)
