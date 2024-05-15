from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Password(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    # Optional because user can leave this field blanks
    url: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    password: so.Mapped[str] = so.mapped_column(sa.String(200), index=True, unique=True)

    def __repr__(self):
        return f"Title: {self.title}\nUsername: {self.username}"
