"""Added relationships

Revision ID: 04234fdaef18
Revises: 60e4ced344a8
Create Date: 2018-09-26 21:41:30.088930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04234fdaef18'
down_revision = '60e4ced344a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sellers', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sellers', 'categories', ['category_id'], ['id'])
    op.add_column('transactions', sa.Column('seller_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'transactions', 'sellers', ['seller_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.drop_column('transactions', 'seller_id')
    op.drop_constraint(None, 'sellers', type_='foreignkey')
    op.drop_column('sellers', 'category_id')
    # ### end Alembic commands ###
