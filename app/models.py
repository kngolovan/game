"""Models related to departments."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class Department(db.Model):
    """Table for departments."""

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now()
    )


class Employee(db.Model):
    """Table for employees."""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(
        db.Integer, db.ForeignKey("departments.id"), nullable=False
    )
    name = db.Column(db.String)
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now()
    )
