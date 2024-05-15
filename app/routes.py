from app import app, db
from flask import render_template, redirect, flash, url_for
from app.forms import MyForm
import sqlalchemy as sa
from app.models import Password


from random import choice
import string


def get_password(r: int) -> str:
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    symbols = ["!", "@", "#", "&", "%"]
    nums = [str(i) for i in range(1, 10)]

    new_pass = []

    for i in range(r):
        source = choice([upper, lower, symbols, nums])
        new_pass.append(choice(source))

    return "".join(new_pass)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        new_pass = get_password(form.characters.data)
        password = Password(
            title=form.app_name.data,
            username=form.username.data,
            url=form.url.data,
            password=new_pass,
        )
        db.session.add(password)
        db.session.commit()

        flash(f"{new_pass}")
        return redirect(url_for("index"))
    return render_template("index.html", title="KeyPast", form=form)
