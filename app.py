from flask import Flask, render_template, request, redirect
from database import get_db, init_db

app = Flask(__name__)  # create Flask application

@app.route('/about')  # about page route
def about():
    return 'About page'

@app.route('/')  # main page route - GET request
def home():
    conn = get_db()  # connect to database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skills")  # get all skills
    skills = cursor.fetchall()  # fetch all results
    conn.close()  # close connection
    return render_template('index.html', skills=skills)  # render template with data

@app.route('/add', methods=['POST'])  # add skill route - POST request only
def add():
    skill = request.form['skill']  # get skill name from form
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO skills (name) VALUES (?)", (skill,))  # insert into database
    conn.commit()  # save changes
    conn.close()
    return redirect('/')  # redirect to main page

@app.route('/edit/<int:id>')  # edit skill route - id from URL
def edit(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skills WHERE id = ?", (id,))  # get skill by id
    skill = cursor.fetchone()  # fetch single result
    conn.close()
    return render_template('edit.html', skill=skill)  # render edit template

@app.route('/update/<int:id>', methods=['POST'])  # update skill route - POST request
def update(id):
    name = request.form['name']  # get new name from form
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE skills SET name = ? WHERE id = ?", (name, id))  # update in database
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')  # delete skill route - id from URL
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM skills WHERE id = ?", (id,))  # delete from database
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()  # create database and tables on startup
    app.run(debug=True)  # run development server