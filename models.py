from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, Index


class Users(Base):
    __tablename__ = 'users'

    __table_args__ = (
        Index('idx_username', 'username', unique=True),
        Index('idx_email', 'email', unique=True),
    )

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default='b2c')
    phone_number = Column(String)


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='SET NULL'))
