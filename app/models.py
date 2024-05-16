from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Password(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    # Optional because user can leave this field blanks
    url: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    password: so.Mapped[str] = so.mapped_column(sa.String(200), index=True, unique=True)

    def __repr__(self):
        return f"Title: {self.title}\nUsername: {self.username}"


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, new_password):
        self.password_hash = generate_password_hash(new_password)

    def check_password(self, other_password):
        return check_password_hash(self.password_hash, other_password)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
