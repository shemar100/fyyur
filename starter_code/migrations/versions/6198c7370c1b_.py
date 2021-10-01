"""empty message

Revision ID: 6198c7370c1b
Revises: 4207f023347d
Create Date: 2021-09-30 13:03:56.663731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6198c7370c1b'
down_revision = '4207f023347d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('website_link', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'seeking_talent')
    op.drop_column('venue', 'website_link')
    # ### end Alembic commands ###