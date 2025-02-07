"""empty message

Revision ID: c504e0139137
Revises: 96eca75f7fa8
Create Date: 2024-03-06 20:59:45.993407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c504e0139137'
down_revision = '96eca75f7fa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
