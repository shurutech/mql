"""create_user_database_id and name_unique_constraint_as_unique

Revision ID: 7b50a83a45cd
Revises: af7438a7b330
Create Date: 2024-05-23 02:19:43.747312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b50a83a45cd'
down_revision = 'af7438a7b330'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint(
        "user_id_and_name_unique_constraint",
        "user_databases",
        ["user_id", "name"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "user_database_id_and_name_unique_constraint", "user_databases", type_="unique"
    )