"""added amount to cartItem table

Revision ID: 342376ba0a37
Revises: 3085acfd70c2
Create Date: 2023-11-08 18:37:12.365363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '342376ba0a37'
down_revision = '3085acfd70c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('amount', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_items', schema=None) as batch_op:
        batch_op.drop_column('amount')

    # ### end Alembic commands ###
