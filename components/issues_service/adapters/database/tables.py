from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Boolean,
    DateTime,
    BigInteger,
    Text
)
import datetime

# разобрать что за naming convention
naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=naming_convention)

issues = Table(
    'Issues',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('action', String(128), nullable=False),
    Column('object_type', String(128), nullable=False),
    Column('object_id', Integer, nullable=False),
    # Column('datetime', DateTime, default=datetime.datetime.now()),
)
