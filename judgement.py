from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", user_list=user_list)

# = model.session.query(model.User). #filter by email = "f@gmail.com"

@app.route("/add_user")
def add_user():
    new_user = model.User(email = request.args.get("email"), password = request.args.get("password"),
       age = request.args.get("age"), zipcode = request.args.get("zipcode"), gender = request.args.get("gender"),
       profession = request.args.get("profession"))
    # print new_user.email
    model.session.add(new_user)
    model.session.commit()
    return "done"

    # print new_user.email

if __name__ == "__main__":
    app.run(debug = True)

