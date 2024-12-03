"""Updated user_type enum to include 'admin'

Revision ID: 640d91bfbbed
Revises: 
Create Date: 2024-12-03 10:26:43.242428

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '640d91bfbbed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('applications', schema=None) as batch_op:
        batch_op.alter_column('job_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('freelancer_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))

    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.alter_column('client_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               nullable=False)
        batch_op.alter_column('budget',
               existing_type=mysql.DECIMAL(precision=10, scale=2),
               nullable=False)
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('client_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('freelancer_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('message',
               existing_type=mysql.TEXT(collation='utf8mb4_general_ci'),
               nullable=False)
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               type_=sa.String(length=50),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               nullable=False)
        batch_op.alter_column('user_type',
               existing_type=mysql.ENUM('client', 'freelancer', 'admin', collation='utf8mb4_general_ci'),
               nullable=False)
        batch_op.alter_column('created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('updated_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('user_type',
               existing_type=mysql.ENUM('client', 'freelancer', 'admin', collation='utf8mb4_general_ci'),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               nullable=True)

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('message',
               existing_type=mysql.TEXT(collation='utf8mb4_general_ci'),
               nullable=True)
        batch_op.alter_column('freelancer_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('client_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('budget',
               existing_type=mysql.DECIMAL(precision=10, scale=2),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               nullable=True)
        batch_op.alter_column('client_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    with op.batch_alter_table('applications', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('freelancer_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('job_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
