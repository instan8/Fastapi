"""create post table

Revision ID: e5cb34557f19
Revises: 
Create Date: 2022-12-24 20:27:34.789193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5cb34557f19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('title',sa.String(),nullable=False))


def downgrade() -> None:
    pass
