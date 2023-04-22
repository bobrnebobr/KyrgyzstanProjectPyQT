import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Note(SqlAlchemyBase):
    __tablename__ = "notes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    salt = sqlalchemy.Column(sqlalchemy.LargeBinary)
    cipher_text = sqlalchemy.Column(sqlalchemy.LargeBinary)
    nonce = sqlalchemy.Column(sqlalchemy.LargeBinary)
    auth_tag = sqlalchemy.Column(sqlalchemy.LargeBinary)
    to_ask_master_password = sqlalchemy.Column(sqlalchemy.Boolean)
