"""Create query history table

Revision ID: 33633a5ee909
Revises: 14c2ea88a9d6
Create Date: 2023-08-14 13:43:54.954424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "33633a5ee909"
down_revision = "14c2ea88a9d6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "query_histories",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("nl_query", sa.String(), nullable=False),
        sa.Column("sql_query", sa.String(), nullable=True),
        sa.Column("user_database_id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_query_histories")),
    )


def downgrade() -> None:
    pass
