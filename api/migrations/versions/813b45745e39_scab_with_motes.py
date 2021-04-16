"""scab with motes

Revision ID: 813b45745e39
Revises: 
Create Date: 2021-03-31 18:04:53.512249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '813b45745e39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scab',
    sa.Column('timestamp', sa.Date(), nullable=False),
    sa.Column('N', sa.String(length=32), nullable=True),
    sa.Column('M', sa.String(length=32), nullable=True),
    sa.Column('E', sa.String(length=32), nullable=True),
    sa.Column('X', sa.String(length=32), nullable=True),
    sa.Column('S', sa.String(length=32), nullable=True),
    sa.Column('G', sa.String(length=32), nullable=True),
    sa.Column('A11', sa.String(length=32), nullable=True),
    sa.Column('Y', sa.String(length=32), nullable=True),
    sa.Column('A16', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('timestamp'),
    sa.UniqueConstraint('timestamp')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scab')
    # ### end Alembic commands ###