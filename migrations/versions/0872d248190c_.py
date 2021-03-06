"""empty message

Revision ID: 0872d248190c
Revises: eb9dfe4806d5
Create Date: 2015-12-29 12:38:23.960293

"""

# revision identifiers, used by Alembic.
revision = '0872d248190c'
down_revision = 'eb9dfe4806d5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    ### end Alembic commands ###
