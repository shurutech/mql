"""add table database-tables

Revision ID: 3fbd94be5602
Revises: da86d1e90141
Create Date: 2023-08-01 12:46:25.628021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3fbd94be5602"
down_revision = "da86d1e90141"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "database_tables",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("user_database_id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_database_tables_id"), "database_tables", ["id"], unique=True
    )
