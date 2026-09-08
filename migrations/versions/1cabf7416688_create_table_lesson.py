"""Create table lesson

Revision ID: 1cabf7416688
Revises: 32d192cb259f
Create Date: 2026-09-08 20:20:29.223665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '1cabf7416688'
down_revision: Union[str, Sequence[str], None] = '32d192cb259f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('lessons',
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', 'now')"), nullable=False),
    sa.Column('update_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', 'now')"), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )


def downgrade() -> None:
    op.drop_table('lessons')
