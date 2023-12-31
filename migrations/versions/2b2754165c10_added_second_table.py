"""Added second table

Revision ID: 2b2754165c10
Revises: 
Create Date: 2023-06-20 14:36:25.709652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b2754165c10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_book', sa.String(), nullable=False),
    sa.Column('autor', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('page', sa.Integer(), nullable=False),
    sa.Column('pdf', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
