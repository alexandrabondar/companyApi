"""empty message

Revision ID: 6ea8a2d35b70
Revises: 70e2ecb06485
Create Date: 2021-07-08 16:06:06.719441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ea8a2d35b70'
down_revision = '70e2ecb06485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('office_id', sa.Integer(), nullable=False))
    op.drop_constraint('departments_user_id_fkey', 'departments', type_='foreignkey')
    op.create_foreign_key(None, 'departments', 'offices', ['office_id'], ['id'])
    op.drop_column('departments', 'user_id')
    op.drop_constraint('offices_department_id_fkey', 'offices', type_='foreignkey')
    op.drop_column('offices', 'department_id')
    op.add_column('users', sa.Column('department_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'users', 'departments', ['department_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'department_id')
    op.add_column('offices', sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('offices_department_id_fkey', 'offices', 'departments', ['department_id'], ['id'])
    op.add_column('departments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.create_foreign_key('departments_user_id_fkey', 'departments', 'users', ['user_id'], ['id'])
    op.drop_column('departments', 'office_id')
    # ### end Alembic commands ###
