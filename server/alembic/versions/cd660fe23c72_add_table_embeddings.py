"""add table embeddings

Revision ID: cd660fe23c72
Revises: 45e10e526767
Create Date: 2023-08-10 12:17:25.657217

"""
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision = "cd660fe23c72"
down_revision = "45e10e526767"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "embeddings",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("embeddings_vector", Vector(1536), nullable=False),
        sa.Column("database_table_id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    pass
