"""add timestamps to tables

Revision ID: 45e10e526767
Revises: baec336a3603
Create Date: 2023-08-09 10:56:40.156275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "45e10e526767"
down_revision = "baec336a3603"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("created_at", sa.DateTime(), nullable=False))
    op.add_column("users", sa.Column("updated_at", sa.DateTime(), nullable=False))
    op.add_column(
        "user_databases", sa.Column("created_at", sa.DateTime(), nullable=False)
    )
    op.add_column(
        "user_databases", sa.Column("updated_at", sa.DateTime(), nullable=False)
    )
    op.add_column(
        "database_tables", sa.Column("created_at", sa.DateTime(), nullable=False)
    )
    op.add_column(
        "database_tables", sa.Column("updated_at", sa.DateTime(), nullable=False)
    )
    op.add_column(
        "table_columns", sa.Column("created_at", sa.DateTime(), nullable=False)
    )
    op.add_column(
        "table_columns", sa.Column("updated_at", sa.DateTime(), nullable=False)
    )


def downgrade() -> None:
    pass
