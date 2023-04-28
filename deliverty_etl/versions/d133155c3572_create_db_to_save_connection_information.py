"""Create db to save connection information

Revision ID: d133155c3572
Revises: 
Create Date: 2023-04-16 10:48:15.632477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d133155c3572"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection_information_table = op.create_table(
        "connection_information",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column(
            "connection_name", sa.String(length=200), nullable=False, unique=True
        ),
        sa.Column("host", sa.String(length=200), nullable=False),
        sa.Column("port", sa.Integer(), nullable=False),
        sa.Column("user", sa.String(length=200), nullable=False),
        sa.Column("password", sa.String(length=200), nullable=False),
        sa.Column("header", sa.JSON(), nullable=True),
        sa.Column("extra", sa.JSON(), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("connceciont_info")
