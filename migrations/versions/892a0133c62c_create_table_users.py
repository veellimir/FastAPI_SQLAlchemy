"""Create table users

Revision ID: 892a0133c62c
Revises: 
Create Date: 2026-09-08 19:25:29.813766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '892a0133c62c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('role', sa.String(length=25), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', 'now')"), nullable=False),
    sa.Column('update_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', 'now')"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('users')
