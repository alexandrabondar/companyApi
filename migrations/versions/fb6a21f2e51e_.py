"""empty message

Revision ID: fb6a21f2e51e
Revises: cad3862f124b
Create Date: 2021-07-08 14:44:35.714839

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fb6a21f2e51e'
down_revision = 'cad3862f124b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('first_name_employer', sa.String(length=80), nullable=True),
    sa.Column('last_name_employer', sa.String(length=80), nullable=True),
    sa.Column('salary_employer', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('auth')
    op.drop_constraint('department_user_id_fkey', 'department', type_='foreignkey')
    op.create_foreign_key(None, 'department', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'department', type_='foreignkey')
    op.create_foreign_key('department_user_id_fkey', 'department', 'auth', ['user_id'], ['id'])
    op.create_table('auth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('first_name_employer', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name_employer', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('salary_employer', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='user_role_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
