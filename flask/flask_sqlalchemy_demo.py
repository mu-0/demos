from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

db = SQLAlchemy(app)

class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String, nullable = False)
    data_json = db.Column(db.JSON, nullable = True)

def init_table():
    ### create table and add some dummy items
    db.create_all()
    new_item_1 = MyTable(data = "data1", data_json = ["a", "b"])
    new_item_2 = MyTable(data = "data2", data_json = [1, 2])
    db.session.add(new_item_1)
    db.session.add(new_item_2)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():

        ### find items in table

        print("All results:")
        results = MyTable.query.all()
        for result in results:
            print(result.id, result.data, result.data_json)

        print("Filtered results:")
        results = MyTable.query.filter_by(data="data1").all()
        for result in results:
            print(result.id, result.data, result.data_json)

        print("Gotten results:")
        result = db.session.get(entity=MyTable, ident=2)
        print(result.id, result.data, result.data_json)

        print("Like results:")
        s = ""
        results = MyTable.query.filter(MyTable.data.ilike(f"%{s}%")).all()
        for result in results:
            print(result.id, result.data, result.data_json)

        print("Editing a row:")
        result = db.session.get(entity=MyTable, ident=2)
        if not result:
            raise Exception
        print(result.id, result.data, result.data_json)
        result.data = "dataTemp"
        db.session.commit()
        result = db.session.get(entity=MyTable, ident=2)
        print(result.id, result.data, result.data_json)
        result.data = "data2"
        db.session.commit()
        result = db.session.get(entity=MyTable, ident=2)
        print(result.id, result.data, result.data_json)


    #app.run(debug=True)
