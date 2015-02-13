"""empty message

Revision ID: 1457566837a1
Revises: 4f6381a5d1ac
Create Date: 2015-02-13 13:46:12.721168

"""

# revision identifiers, used by Alembic.
revision = '1457566837a1'
down_revision = '4f6381a5d1ac'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buyers',
    sa.Column('buyer_uid', sa.Integer(), nullable=False),
    sa.Column('buyer_name', sa.String(), nullable=True),
    sa.Column('json', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('buyer_uid')
    )
    op.create_table('releases',
    sa.Column('ocid', sa.String(), nullable=False),
    sa.Column('language', sa.String(), nullable=True),
    sa.Column('json', postgresql.JSON(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['buyers.buyer_uid'], ),
    sa.PrimaryKeyConstraint('ocid')
    )
    op.create_table('awards',
    sa.Column('awardID', sa.String(), nullable=False),
    sa.Column('awardDate', sa.Date(), nullable=True),
    sa.Column('awardValue', sa.Integer(), nullable=True),
    sa.Column('json', postgresql.JSON(), nullable=True),
    sa.Column('release_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['release_id'], ['releases.ocid'], ),
    sa.PrimaryKeyConstraint('awardID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('awards')
    op.drop_table('releases')
    op.drop_table('buyers')
    ### end Alembic commands ###
