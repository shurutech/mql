"""add table user-databases

Revision ID: da86d1e90141
Revises: bf224d84fb4d
Create Date: 2023-08-01 12:44:01.275690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "da86d1e90141"
down_revision = "bf224d84fb4d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_databases",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_databases_id"), "user_databases", ["id"], unique=True)
