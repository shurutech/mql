"""Rename query_histories to queries

Revision ID: af7438a7b330
Revises: 68b6ee05672c
Create Date: 2024-03-28 16:38:38.987895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af7438a7b330'
down_revision = '68b6ee05672c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('query_histories', 'queries')


def downgrade() -> None:
    op.rename_table('queries', 'query_histories')
