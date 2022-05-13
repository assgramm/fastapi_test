import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimedBaseModel(Base):
    """Основная модель с датой"""

    __abstract__ = True

    created_at = sa.Column(sa.DateTime(True), server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(True), default=sa.func.now(), onupdate=sa.func.now(),
                           server_default=sa.func.now())