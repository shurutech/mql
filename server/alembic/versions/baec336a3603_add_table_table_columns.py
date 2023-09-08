"""add table table-columns

Revision ID: baec336a3603
Revises: 3fbd94be5602
Create Date: 2023-08-01 12:55:28.697091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "baec336a3603"
down_revision = "3fbd94be5602"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "table_columns",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("data_type", sa.String(), nullable=False),
        sa.Column("database_table_id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_table_columns_id"), "table_columns", ["id"], unique=True)
