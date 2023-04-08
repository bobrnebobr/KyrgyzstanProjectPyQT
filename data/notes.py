import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Note(SqlAlchemyBase):
    __tablename__ = "notes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    text = sqlalchemy.Column(sqlalchemy.String)
    datetime = sqlalchemy.Column(sqlalchemy.DateTime)
    creator_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')
