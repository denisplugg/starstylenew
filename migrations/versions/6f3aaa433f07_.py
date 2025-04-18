"""empty message

Revision ID: 6f3aaa433f07
Revises: b8d74c6c3c36
Create Date: 2025-04-18 23:04:20.296124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f3aaa433f07'
down_revision = 'b8d74c6c3c36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ru_outfits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ru_outfits', schema=None) as batch_op:
        batch_op.drop_column('link')

    # ### end Alembic commands ###
