"""replaced order_date with date_created

Revision ID: 71e13f38565e
Revises: 45e87e76d5e6
Create Date: 2023-11-05 14:44:07.422942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71e13f38565e'
down_revision = '45e87e76d5e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.drop_column('order_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###