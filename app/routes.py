from app import app, db
from flask import render_template, redirect, flash, url_for, request
from app.forms import MyForm, LoginForm, RegistrationForm
import sqlalchemy as sa
from app.models import Password, User
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit


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
@login_required
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


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)
        # handle next
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
        return redirect(url_for("index"))
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Congratulation {form.username.data}, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)
