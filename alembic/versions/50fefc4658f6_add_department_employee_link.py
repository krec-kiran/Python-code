"""add department_employee_link

Revision ID: 50fefc4658f6
Revises: 
Create Date: 2019-10-13 21:52:08.297673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50fefc4658f6'
down_revision = None
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
    op.drop_table(
        'department_employee_link'
    )
