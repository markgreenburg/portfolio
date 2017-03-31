"""
Main Flask routes and app file for portfolio
"""
import sys
from flask import Flask, request, jsonify, render_template, url_for
reload(sys)
sys.setdefaultencoding('utf-8')

APP = Flask(__name__)

@APP.route("/")
def home():
    """
    Homepage route, displays homepage
    """
    return render_template("home.html")

@APP.route("/submit", methods=["POST"])
def submit():
    """
    Handles contact form submissions and responds back to client.
    """
    
    return jsonify({
        'message': "Email sent successfully",
        'data': {},
        'success': True
    }), 201

if __name__ == "__main__":
    APP.run(debug=True)
