"""empty message

Revision ID: 6ee3777a7c30
Revises: b8cb37f0192a
Create Date: 2020-04-17 22:55:52.224153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ee3777a7c30'
down_revision = 'b8cb37f0192a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'musics', 'users', ['user_id'], ['id'])
    op.drop_column('musics', 'upload_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('musics', sa.Column('upload_type', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'musics', type_='foreignkey')
    # ### end Alembic commands ###
