from flask import Blueprint, render_template, request, redirect, url_for, flash

from .forms import ContactForm
from .models import db, Contact

folio = Blueprint("folio", __name__)

@folio.route("/", methods=("GET", "POST"))
def index():
    form = ContactForm()
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        content = request.form.get("content")

        new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            content=content
        )
        db.session.add(new_contact)
        db.session.commit()

        flash("Votre message a été envoyé avec succès", "success")
        return redirect(url_for("folio.index"))
    else:
        form = ContactForm()
    return render_template("index.html", form=form)