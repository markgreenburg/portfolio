"""
Main Flask routes and app file for portfolio
"""
import sys
from flask import Flask, request, jsonify, render_template, url_for
import mail
reload(sys)
sys.setdefaultencoding('utf-8')

APP = Flask(__name__)

# Set up Amazon SES connection for contact form emails


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
    try:
        form = request.form
        mail.send_email(form.get('name'), form.get('email'), form.get('message'))
        return jsonify({
            'message': "Email sent successfully",
            'data': {},
            'success': True
        }), 201
    except:
        return jsonify({
            'message': "Email not sent",
            'data': {},
            'success': False
        }), 500

if __name__ == "__main__":
    APP.run(debug=True)
