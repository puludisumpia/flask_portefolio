from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="assets/templates/", static_folder="assets/static/")
app.secret_key = "lkjhgfgjyuhiomplikjhgfjuj"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


from applications.folio.views import folio
app.register_blueprint(folio)