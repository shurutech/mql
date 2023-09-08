"""add user_database_id column to embeddings table

Revision ID: 14c2ea88a9d6
Revises: 794012702ac2
Create Date: 2023-08-11 18:43:53.565859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "14c2ea88a9d6"
down_revision = "794012702ac2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "embeddings", sa.Column("user_database_id", sa.UUID(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column("embeddings", "user_database_id")
