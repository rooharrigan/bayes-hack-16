from jinja2 import StrictUndefined

from helper import get_rec_areas
from googleprocess import gets_min_travel_to_location_from_user
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

@app.route('/search_results')
def show_search_results():
    """Shows search results from lat long"""

    lat = request.args.get("lat")

    lng = request.args.get("lng")

    rec_areas = get_rec_areas(lat, lng)

    final = gets_min_travel_to_location_from_user(lat, lng, rec_areas)

    return final





if __name__ == "__main__":

    app.debug = True

    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()