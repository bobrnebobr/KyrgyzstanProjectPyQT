import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Password(SqlAlchemyBase):
    __tablename__ = "passwords"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)

    username_salt = sqlalchemy.Column(sqlalchemy.LargeBinary)
    username_cipher_text = sqlalchemy.Column(sqlalchemy.LargeBinary)
    username_nonce = sqlalchemy.Column(sqlalchemy.LargeBinary)
    username_auth_tag = sqlalchemy.Column(sqlalchemy.LargeBinary)

    password_salt = sqlalchemy.Column(sqlalchemy.LargeBinary)
    password_cipher_text = sqlalchemy.Column(sqlalchemy.LargeBinary)
    password_nonce = sqlalchemy.Column(sqlalchemy.LargeBinary)
    password_auth_tag = sqlalchemy.Column(sqlalchemy.LargeBinary)

    URL = sqlalchemy.Column(sqlalchemy.String)

    description_salt = sqlalchemy.Column(sqlalchemy.LargeBinary)
    description_cipher_text = sqlalchemy.Column(sqlalchemy.LargeBinary)
    description_nonce = sqlalchemy.Column(sqlalchemy.LargeBinary)
    description_auth_tag = sqlalchemy.Column(sqlalchemy.LargeBinary)

    to_ask_master_password = sqlalchemy.Column(sqlalchemy.Boolean)
