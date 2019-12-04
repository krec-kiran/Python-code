"""add department_employee_link

Revision ID: aa2607a6db5f
Revises: 50fefc4658f6
Create Date: 2019-10-13 22:17:51.012001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa2607a6db5f'
down_revision = '50fefc4658f6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'department_employee_new_link',
        sa.Column(
            'department_id', sa.Integer,
            sa.ForeignKey('department.id'), primary_key=True
        ),
        sa.Column(
            'employee_id', sa.Integer,
            sa.ForeignKey('employee.id'), primary_key=True
        )
    )


def downgrade():
    pass
