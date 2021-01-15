from flask import Flask,render_template, jsonify, request
import sqlite3
import forms


app = Flask(__name__)


@app.route('/')
def hello_world():
    form = forms.UsersForm()
    return render_template('form.html', form=form)

@app.route('/return_categories',methods=["POST","GET"])
def return_categories():
    query = "SELECT * FROM categories"
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    datas = cursor.execute(query).fetchall()
    return jsonify(datas)




if __name__ == '__main__':
    app.run()
