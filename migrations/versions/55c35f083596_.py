"""empty message

Revision ID: 55c35f083596
Revises: 1ef7ffaf88d9
Create Date: 2015-03-02 15:01:43.985615

"""

# revision identifiers, used by Alembic.
revision = '55c35f083596'
down_revision = '1ef7ffaf88d9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sources', sa.Column('skip_lines', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sources', 'skip_lines')
    ### end Alembic commands ###
