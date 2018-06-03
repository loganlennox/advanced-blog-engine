from flask import Blueprint, render_template

mod_auth = Blueprint("auth", __name__, url_prefix="/login")

# Sign in page
@mod_auth.route("/", methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")
