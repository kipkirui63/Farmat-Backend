"""remove cartitem id from orders table

Revision ID: 14d785a4135f
Revises: aedabc282cbd
Create Date: 2023-10-28 17:34:09.741728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14d785a4135f'
down_revision = 'aedabc282cbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint('fk_products_vendor_id_vendors', type_='foreignkey')
        batch_op.drop_constraint('fk_products_category_id_categories', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_products_category_id_categories'), 'categories', ['category_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_products_vendor_id_vendors'), 'vendors', ['vendor_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_products_vendor_id_vendors'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_products_category_id_categories'), type_='foreignkey')
        batch_op.create_foreign_key('fk_products_category_id_categories', 'categories', ['category_id'], ['id'])
        batch_op.create_foreign_key('fk_products_vendor_id_vendors', 'vendors', ['vendor_id'], ['id'])

    # ### end Alembic commands ###
