"""add connection_string in user_databases

Revision ID: 68b6ee05672c
Revises: 33633a5ee909
Create Date: 2023-09-13 13:40:27.700989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68b6ee05672c'
down_revision = '33633a5ee909'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user_databases", sa.Column("connection_string", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("user_databases", "connection_string")

