"""empty message

Revision ID: 0d90840f01eb
Revises: 136bf4411930
Create Date: 2025-04-19 02:30:19.251532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d90840f01eb'
down_revision = '136bf4411930'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_ru_brands')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('avatar')

    op.create_table('_alembic_tmp_ru_brands',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('unique_id', sa.VARCHAR(length=100), nullable=False),
    sa.Column('celebrity_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('celebrity_img', sa.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unique_id', name='ru_brands')
    )
    # ### end Alembic commands ###
