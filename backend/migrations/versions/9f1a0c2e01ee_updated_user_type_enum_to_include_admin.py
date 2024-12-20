"""Updated user_type enum to include 'admin'

Revision ID: 9f1a0c2e01ee
Revises: 640d91bfbbed
Create Date: 2024-12-03 10:29:46.583326

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f1a0c2e01ee'
down_revision = '640d91bfbbed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=50),
               type_=sa.String(length=255),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=255),
               nullable=True)
        batch_op.alter_column('user_type',
               existing_type=mysql.ENUM('client', 'freelancer', 'admin', charset='utf8mb4', collation='utf8mb4_general_ci'),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               type_=sa.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('updated_at',
               existing_type=mysql.DATETIME(),
               type_=sa.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.TIMESTAMP(),
               type_=mysql.DATETIME(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
        batch_op.alter_column('created_at',
               existing_type=sa.TIMESTAMP(),
               type_=mysql.DATETIME(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('user_type',
               existing_type=mysql.ENUM('client', 'freelancer', 'admin', charset='utf8mb4', collation='utf8mb4_general_ci'),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=255),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(collation='utf8mb4_general_ci', length=50),
               nullable=False)

    # ### end Alembic commands ###
