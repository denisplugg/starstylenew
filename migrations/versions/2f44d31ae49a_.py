"""empty message

Revision ID: 2f44d31ae49a
Revises: 4cfe486fc68b
Create Date: 2025-04-11 14:26:34.768307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f44d31ae49a'
down_revision = '4cfe486fc68b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('all_stars', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nation', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('all_stars', schema=None) as batch_op:
        batch_op.drop_column('nation')

    # ### end Alembic commands ###
