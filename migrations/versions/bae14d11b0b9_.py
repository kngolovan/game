"""empty message

Revision ID: bae14d11b0b9
Revises: bbe6a60dd212
Create Date: 2020-11-23 18:41:45.779571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bae14d11b0b9"
down_revision = "bbe6a60dd212"
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=("departments", "employees"))

    departments_table = sa.Table("departments", meta)
    op.bulk_insert(
        departments_table,
        [
            {"name": "Департамент здоровья"},
            {"name": "Отдел по борьбе с невежеством"},
            {"name": "Стройбат"},
        ],
    )

    employees_table = sa.Table("employees", meta)
    op.bulk_insert(
        employees_table,
        [
            {"department_id": 1, "name": "Коля"},
            {"department_id": 1, "name": "Петр"},
            {"department_id": 2, "name": "Вася"},
        ],
    )


def downgrade():
    pass
