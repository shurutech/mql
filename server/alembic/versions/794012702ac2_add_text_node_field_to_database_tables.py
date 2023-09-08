"""add text_node field to database_tables

Revision ID: 794012702ac2
Revises: cd660fe23c72
Create Date: 2023-08-11 17:02:36.631364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "794012702ac2"
down_revision = "cd660fe23c72"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("database_tables", sa.Column("text_node", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("database_tables", "text_node")
