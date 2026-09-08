"""Create table users

Revision ID: 32d192cb259f
Revises:
Create Date: 2026-09-08 20:18:48.033720

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "32d192cb259f"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("username", sa.String(length=20), nullable=False),
        sa.Column("password", sa.String(length=15), nullable=False),
        sa.Column("role", sa.String(length=25), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', 'now')"),
            nullable=False,
        ),
        sa.Column(
            "update_at",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', 'now')"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    op.drop_table("users")
