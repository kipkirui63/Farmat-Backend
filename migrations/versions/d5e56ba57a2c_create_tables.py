"""Create tables

Revision ID: d5e56ba57a2c
Revises: 3b90d901ba30
Create Date: 2023-10-27 01:45:16.519714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5e56ba57a2c'
down_revision = '3b90d901ba30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
