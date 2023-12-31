"""remove cartitem id from orders table

Revision ID: bdaed81594e5
Revises: 89af9506c800
Create Date: 2023-10-28 15:45:27.039527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdaed81594e5'
down_revision = '89af9506c800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint('fk_orders_cart_item_id_cart_items', type_='foreignkey')
        batch_op.drop_column('cart_item_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cart_item_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_orders_cart_item_id_cart_items', 'cart_items', ['cart_item_id'], ['id'])

    # ### end Alembic commands ###
