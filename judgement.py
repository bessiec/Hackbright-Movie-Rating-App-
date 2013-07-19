from flask import Flask, render_template, redirect, request, session
import model

app = Flask(__name__)
app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    index = model.session.query(model.User).limit(5).all()
    return render_template("index.html", index=index) 

@app.route("/add_user")
def add_user():
    new_user = model.User(email = request.args.get("email"), password = request.args.get("password"),
       age = request.args.get("age"), zipcode = request.args.get("zipcode"), gender = request.args.get("gender"),
       profession = request.args.get("profession"))

    model.session.add(new_user)
    model.session.commit()
    return "done"

@app.route("/login")
def process_login():
    email = request.args.get("email")
    password = request.args.get("password")

    user = model.session.query(model.User).filter_by(email=email, password=password).first() 

    if not user:
        return "You are wrong.  You cannot login."

    else: 
        session['user_id'] = user.id 
        return "Hell Yeah Fucking Right."

@app.route("/user_list")
def show_users():
    user_list = model.session.query(model.User).all()
    return render_template("user_list.html", user_list=user_list)

@app.route("/user_table")
def user_table():

    # not all_users in query here
    # not all_users in user_table.html
    # just want to show all movies and ratings that ONE user has done
    # user_table = model.session.query(model.User).limit(5).all()

    user_id = request.args.get("userid")

    #table = model.session.query(model.User).filter_by(id=user_table)
    user = model.session.query(model.User).get(user_id)

    # why isn't this below the same 
    # table = model.session.query(model.Rating).filter_by(user=user_table)

    # query ratings table on user.id which we're getting from the arguments to get movie title 

    # up here I'm trying to pass in userid as an argument variable to access the
    # database and match the id in the url to the actual id id in database.

    return render_template("user_table.html", user=user)
    # return table
    # return user_table

    # view list of movies that selected user has rated and corresponding ratings
    # pseudocode
    # user_table here corresponds to id in User, or user in Rating(?)
    # return corresponding movie and rating in Rating 

if __name__ == "__main__":
    app.run(debug = True)

