"""add foreign key roles

Revision ID: 8944ccf58bba
Revises: 030d10d0d02c
Create Date: 2019-04-23 12:42:38.558810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8944ccf58bba'
down_revision = '030d10d0d02c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###