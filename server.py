from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("home.html")


@app.route("/login")
def login_form():
    """Render login form"""

    return render_template("login.html")

@app.route("/login_submission", methods=["POST"])
def login_submission():
    """Confirms username and password through database and sessions."""

    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter(User.email == email).first()
    if user:
        if password == user.password:
            session["current_user"] = email
            flash("Logged in as %s" % (email))
            return redirect("/") 
        else:
            flash("Incorrect password submitted")
            return redirect("/login")  
    else:
        new_user = User(email=email, password=password, age="NULL", zipcode="NULL")
        db.session.add(new_user)
        db.session.commit()
        flash("New user logged in as %s" % (email))
        return redirect("/")



if __name__ == "__main__":

    app.debug = True

    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()