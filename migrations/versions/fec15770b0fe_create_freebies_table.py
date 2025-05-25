"""create freebies table

Revision ID: fec15770b0fe
Revises: 0882b862ce57
Create Date: 2025-05-26 02:32:46.933064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fec15770b0fe'
down_revision: Union[str, None] = '0882b862ce57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        "freebies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_name", sa.String, nullable=False),
        sa.Column("value", sa.Integer, nullable=False),
        sa.Column("dev_id", sa.Integer, sa.ForeignKey("devs.id")),
        sa.Column("company_id", sa.Integer, sa.ForeignKey("companies.id")),
    )

def downgrade():
    op.drop_table("freebies")
