"""App's views."""
from flask import render_template, Blueprint

from app.models import Department

bp = Blueprint("departments", __name__)


@bp.route("/", methods=["GET"])
def get_departments():
    """list departments"""
    departments = Department.query.all()
    return render_template("departments.jinja2", departments=departments)
