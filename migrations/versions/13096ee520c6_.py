"""empty message

Revision ID: 13096ee520c6
Revises: 21885269a419
Create Date: 2020-04-17 22:09:54.684169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13096ee520c6'
down_revision = '21885269a419'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('musics', 'upload_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('musics', sa.Column('upload_type', sa.VARCHAR(length=60), nullable=True))
    # ### end Alembic commands ###