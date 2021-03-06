"""empty message

Revision ID: 21104df68684
Revises: 847781e2c8e3
Create Date: 2015-12-28 09:34:10.826621

"""

# revision identifiers, used by Alembic.
revision = '21104df68684'
down_revision = '847781e2c8e3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=110), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
