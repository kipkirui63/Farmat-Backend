"""added vendor_id to order_products

Revision ID: 3085acfd70c2
Revises: 71e13f38565e
Create Date: 2023-11-06 16:16:56.377445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3085acfd70c2'
down_revision = '71e13f38565e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vendor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_order_products_vendor_id_vendors'), 'vendors', ['vendor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_products', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_order_products_vendor_id_vendors'), type_='foreignkey')
        batch_op.drop_column('vendor_id')

    # ### end Alembic commands ###
