"""
Main Flask routes and app file for portfolio
"""
import sys
from flask import Flask, render_template, url_for
reload(sys)
sys.setdefaultencoding('utf-8')

APP = Flask(__name__)

@APP.route("/")
def home():
    """
    Homepage route, displays homepage
    """
    return render_template("home.html")

if __name__ == "__main__":
    APP.run(debug=True)
